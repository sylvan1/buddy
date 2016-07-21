from django.contrib import admin
from projects.models import Project

@admin.register(Project)
class ProjectsAdmin(admin.ModelAdmin):
	exclude = ('slug',)

