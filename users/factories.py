# -*- coding: utf-8 -*-
import factory

from .models import User, Skill, SkillUser


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'user-{0}'.format(n))
    email = factory.Sequence(lambda n: 'user-{0}@example.com'.format(n))
    password = factory.PostGenerationMethodCall('set_password', 'test')

    class Meta:
        model = User
        django_get_or_create = ('username',)


class SkillFactory(factory.django.DjangoModelFactory):
    programming_lang = factory.Iterator([
        'Python', 'Java', 'Django', 'JavaScript', 'Scala', 'SQL',
        'JQuery', 'React', 'C++', 'C', 'C#', '.NET', 'Ajax'
    ])

    class Meta:
        model = Skill


class SkillUserFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    skill = factory.SubFactory(SkillFactory)
    level = factory.Iterator([1, 2, 3, 4, 5])

    class Meta:
        model = SkillUser
        django_get_or_create = ('user', 'skill', 'level')
