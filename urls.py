from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'),
        name="home"),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'),
        name="about"),

    # Django Admin, use {% url 'admin:index' %}

    url('^admin/', include(admin.site.urls)),

    # User management
    url(r'^users/', include("users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    # Project
    url(r'^projects/',
        include("projects.urls", namespace="projects")),

    # TinyMCE
    url(r'^tinymce/', include('tinymce.urls')),
]

# Let django serve media files with DEBUG = True
# if settings.DEBUG:
#     urlpatterns += [
#         url(
#             r'^media/(?P<path>.*)$', 'django.views.static.serve',
#             {'document_root': settings.MEDIA_ROOT, 'show_indexes': False}
#         ),
#     ]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
