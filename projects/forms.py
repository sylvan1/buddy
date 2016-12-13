from django.forms import ModelForm, Textarea, TextInput, NumberInput
from django.forms.extras import SelectDateWidget
from django.forms import modelformset_factory

from tinymce.widgets import TinyMCE

from .models import Project
from users.models import Skill


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = (
            'name',
            'description',
            'expiration_date', 'number_of_users_required', 'opensource', 'url')
        widgets = {
            'name': Textarea(attrs={'rows': 2, 'cols': 50}),
            'description': TinyMCE(mce_attrs={'theme': "advanced"}),
            'expiration_date': SelectDateWidget(),
            'number_of_users_required': NumberInput(
                attrs={'style': 'text-align:right'}),
            'url': TextInput(attrs={'size': 54}),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ('programming_lang',)

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        self.fields['programming_lang'].required = False

    def validate_unique(self):
        return True


SkillFormSet = modelformset_factory(
    Skill, form=SkillForm, fields=('programming_lang',), extra=3)
