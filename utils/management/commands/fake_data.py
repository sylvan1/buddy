# -*- coding: utf-8 -*-

import random

from copy import deepcopy
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from users.factories import UserFactory, SkillFactory, SkillUserFactory
from users.models import Skill
from projects.factories import ProjectFactory


class Command(BaseCommand):
    help = u'Generate fake data.'

    def add_arguments(self, parser):
        parser.add_argument('--users_number', nargs='+', type=int, default=10)
        parser.add_argument('--projects_number', nargs='+', type=int, default=5)

    def handle(self, *args, **options):
        call_command('migrate')
        call_command('makemigrations')
        users_number = options['users_number']
        projects_number = options['projects_number']
        users_list = []
        can_skill = True
        while can_skill:
            try:
                SkillFactory()
            except IntegrityError:
                can_skill = False

        skill_id_list = Skill.objects.values_list('id', flat=True)[::1]
        for idx in range(users_number):
            user = UserFactory()
            users_list.append(user)
            random_skill_ids = random.sample(skill_id_list, 2)
            level_list = random.sample([1, 2, 3, 4, 5], 2)
            SkillUserFactory(user=user, skill=Skill.objects.get(id=random_skill_ids[0]), level=level_list[0])
            SkillUserFactory(user=user, skill=Skill.objects.get(id=random_skill_ids[1]), level=level_list[1])

        for idx in range(projects_number):
            members = random.sample(users_list, 2)
            possible_owner = [user for user in users_list if user not in members]
            owner = random.choice(possible_owner)
            user_without_members = deepcopy(members)
            user_without_members.remove(members[0])
            user_without_members.remove(members[1])

            i_want_to_join = random.sample(
                user_without_members, 2 if len(user_without_members) else 0
            )
            skills = random.sample(skill_id_list, 2)
            ProjectFactory(
                members=members,
                owner=owner,
                i_want_to_join=i_want_to_join,
                skills=skills
            )
