# -*- coding: utf-8 -*

from django import forms
from django.core.exceptions import ObjectDoesNotExist

from .models import User, Skill, SkillUser


SKILL_CHOICES = (
    (0, '----------'),
    (1, 'base'),
    (2, 'pre-intermediate'),
    (3, 'intermediate'),
    (4, 'upper-intermediate'),
    (5, 'expert')
)


class UserUpdateForm(forms.ModelForm):

    programming_lang = forms.CharField(label='programming lang', max_length=255, required=False)
    level = forms.ChoiceField(label='level', choices=SKILL_CHOICES, required=False)

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        for field in self.fields:
            if isinstance(self.fields[field].widget, forms.TextInput):
                self.fields[field].widget.attrs['placeholder'] = self.fields[field].label.capitalize()

    def save(self, commit=True):
        instance = super(UserUpdateForm, self).save(commit=True)
        # lang, lang_created = Skill.objects.get_or_create(programming_lang=self.cleaned_data['programming_lang'])
        # level = SkillUser.objects.get_or_create(user=instance,
        #                                         skill=lang,
        #                                         level=self.cleaned_data['level'])
        # level.save()
        return instance

    class Meta:
        fields = ['username', 'first_name', 'last_name', 'email', 'about_me',
                  'avatar', 'my_project_experience', 'phone', 'programming_lang', 'level']
        model = User
