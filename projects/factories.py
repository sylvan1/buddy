# -*- coding: utf-8 -*-

import datetime
import factory

from .models import Project
from users.factories import UserFactory


class ProjectFactory(factory.DjangoModelFactory):
    owner = factory.SubFactory(UserFactory)
    name = factory.Sequence(lambda n: 'project-{0}'.format(n))
    description = factory.Sequence(lambda n: 'project-{0} is about...'.format(n))
    expiration_date = factory.LazyFunction(datetime.datetime.now)
    number_of_users_required = 3
    opensource = factory.Iterator([True, False])
    url = factory.Sequence(lambda n: 'www.project-{0}.pl'.format(n))

    @factory.post_generation
    def members(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for member in extracted:
                self.members.add(member)

    @factory.post_generation
    def i_want_to_join(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for joined_person in extracted:
                self.i_want_to_join.add(joined_person)

    @factory.post_generation
    def skills(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for skill in extracted:
                self.skills.add(skill)

    class Meta:
        model = Project
        django_get_or_create = ('name',)
