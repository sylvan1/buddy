import django_filters
from users.models import Skill
from .models import Project


class ProjectFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', help_text='')
    description = django_filters.CharFilter(lookup_expr='icontains', help_text='')
    skills = django_filters.ModelMultipleChoiceFilter(queryset=Skill.objects, help_text='')

    class Meta:
        model = Project
        fields = ['name', 'description', 'skills']