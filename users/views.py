# -*- coding: utf-8 -*-
from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, ListView, RedirectView, UpdateView, DeleteView

from .models import User
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


class UserUpdateView(LoginRequiredMixin, FormView, UpdateView):

    model = User
    form_class = UserUpdateForm

    def get_success_url(self):
        username = self.request.POST.get('username') if self.request.POST else self.request.user.username
        return reverse("users:detail", kwargs={"username": username})

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
