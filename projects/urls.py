# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views
###
from .tests import ProjectAutocomplete
###


urlpatterns = [

    url(
        regex=r'^my_projects/$',
        view=views.user_projects_list,
        name='user_projects_list'
    ),

    url(
        regex=r'^project-autocomplete/$',
        view=ProjectAutocomplete.as_view(),
        name='project-autocomplete',
    ),

    url(
        regex=r'^$',
        view=views.ProjectListView.as_view(),
        name='list'
    ),

    url(
        regex=r'^new/$',
        view=views.ProjectCreateView.as_view(),
        name='create'
    ),

    url(
        regex=r'^(?P<slug>[-\w]+)/$',
        view=views.ProjectDetailView.as_view(),
        name='detail'
    ),

    url(
        regex=r'^(?P<slug>[-\w]+)/update/$',
        view=views.ProjectUpdateView.as_view(),
        name='update'
    ),

    url(
        regex=r'^(?P<slug>[-\w]+)/delete/$',
        view=views.ProjectDeleteView.as_view(),
        name='delete'
    ),

    
]
