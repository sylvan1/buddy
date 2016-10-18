from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

from .models import Project
from users.models import Skill, User
from .forms import ProjectForm, SkillFormSet


class ProjectListView(ListView):
    model = Project


class ProjectDetailView(DetailView):
    model = Project

    def post(self, request, *args, **kwargs):
        project = self.get_object()
        user = request.user    

        if 'join' in request.POST:
            project.i_want_to_join.add(user)
        elif 'accept_candidate' in request.POST:
            if user == project.owner:
                candidate_name = request.POST['accept_candidate']
                candidate = User.objects.get(username=candidate_name)
                project.members.add(candidate)
                project.i_want_to_join.remove(candidate)
        elif 'reject_candidate' in request.POST:
            if user == project.owner:
                candidate_name = request.POST['reject_candidate']
                candidate = User.objects.get(username=candidate_name)
                project.i_want_to_join.remove(candidate)
        elif 'remove_member' in request.POST:
            if user == project.owner:
                member_name = request.POST['remove_member']
                member = User.objects.get(username=member_name)
                project.members.remove(member)

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('projects:detail', args=(self.get_object().slug,))


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    subform_class = SkillFormSet

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.form_class(request.POST)
        skill_subform = self.subform_class(request.POST)
        if form.is_valid() and skill_subform.is_valid():
            created_project = form.save(commit=False)
            user = None
            if request.user.is_authenticated():
                user = request.user
            created_project.owner = user
            created_project.save()
            for subform in skill_subform:
                programming_lang = subform.cleaned_data.get('programming_lang')
                if programming_lang:
                    programming_lang = programming_lang.lower()
                    skill, created = Skill.objects.get_or_create(
                        programming_lang=programming_lang)
                    created_project.skills.add(skill)
            created_project.save()
            self.object = Project.objects.get(slug=created_project.slug)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(
                self.get_context_data(form=form, subform=skill_subform))

    def get_context_data(self, **kwargs):
        context = super(ProjectCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['subform'] = self.subform_class(self.request.POST)
        else:
            context['subform'] = self.subform_class(
                queryset=Skill.objects.none())
        return context

    def get_success_url(self):
        return reverse_lazy('projects:detail', args=(self.object.slug,))


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    subform_class = SkillFormSet

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST, instance=self.object)
        skill_subform = self.subform_class(request.POST)
        if form.is_valid() and skill_subform.is_valid():
            updated_project = form.save(commit=False)
            updated_project.skills.clear()
            for subform in skill_subform:
                programming_lang = subform.cleaned_data.get('programming_lang')
                if programming_lang:
                    programming_lang = programming_lang.lower()
                    skill, created = Skill.objects.get_or_create(
                        programming_lang=programming_lang)
                    updated_project.skills.add(skill)
            updated_project.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(
                self.get_context_data(form=form, subform=skill_subform))

    def get_context_data(self, **kwargs):
        context = super(ProjectUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['subform'] = self.subform_class(self.request.POST)
        else:
            context['subform'] = self.subform_class(
                queryset=self.get_object().skills.all())
        return context

    def get_success_url(self):
        return reverse_lazy('projects:detail', args=(self.object.slug,))


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('projects:list')
