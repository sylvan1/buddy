# -*- coding: utf-8 -*-
from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, DeleteView

from .models import User

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

    fields = ['username', 'email', 'about_me', 'avatar', 'my_project_experience', 'phone']
    model = User

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



