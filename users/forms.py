# -*- coding: utf-8 -*

from django import forms
from django.core.exceptions import ObjectDoesNotExist

from .models import User, Skill, SkillUser


class UserUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        for field in self.fields:
            if isinstance(self.fields[field].widget, forms.TextInput):
                self.fields[field].widget.attrs['placeholder'] = self.fields[field].label.capitalize()

    class Meta:
        fields = ['username', 'first_name', 'last_name', 'email', 'about_me',
                  'avatar', 'my_project_experience', 'phone']
        model = User
