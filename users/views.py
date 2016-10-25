# -*- coding: utf-8 -*-
from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, DeleteView

from django.shortcuts import render
from random import shuffle

from .models import User, Skill, SkillUser
from .forms import UserUpdateForm

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    form_class = UserUpdateForm

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('projects:list')

    def get_object(self):
        return User.objects.get(username=self.request.user.username)

def UserSearchView(request):

    language = None
    user_list = []
    if request.method == 'POST' and 'language' in request.POST:
        language = request.POST['language']
        skill = Skill.objects.filter(programming_lang=language).first()
        if skill:
            user_list = list(User.objects.filter(skilluser__skill=skill))
            shuffle(user_list)

    context_dict={
        "searched_for": language,
        "users": user_list,
    }
    return render(request, 'users/user_search.html', context_dict)
