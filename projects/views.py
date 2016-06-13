from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Project
from .forms import ProjectForm


class ProjectListView(ListView):
    model = Project

class ProjectDetailView(DetailView):
    model = Project

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    def get_success_url(self):
        return reverse_lazy('projects:detail', args=(self.object.slug,)) 

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    subform_class = SkillForm

    def post(self, request, *args, **kwargs):
            self.object = self.get_object()
            form = self.form_class(request.POST, instance=self.object)
            subform = self.subform_class(request.POST)
            if form.is_valid() and subform.is_valid():
                print subform.cleaned_data
                this_project = form.save(commit=False)
                a_lang = subform.data['programming_lang'].lower()
                if a_lang:
                    skill, created = Skill.objects.get_or_create(programming_lang=a_lang)
                    this_project.skills.add(skill)
                this_project.save()
                return HttpResponseRedirect(self.get_success_url())
            else:
                return self.render_to_response(
                    self.get_context_data(form=form, subform=subform))

    def get_context_data(self, **kwargs):
        context = super(ProjectUpdateView, self).get_context_data(**kwargs)
        context['subform'] = self.subform_class(self.request.GET)
        return context

    def get_success_url(self):
        return reverse_lazy('projects:detail', args=(self.object.slug,)) 

class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('projects:list')
