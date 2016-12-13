from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

from tinymce import models as tinymce_models

from users.models import Skill, User


class Project(models.Model):
    owner = models.ForeignKey(User, related_name='owner')
    members = models.ManyToManyField(User, related_name='member', blank=True)
    i_want_to_join = models.ManyToManyField(User, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    name = models.CharField(
        _("Name of the project"), max_length=255, unique=True)
    description = tinymce_models.HTMLField()
    expiration_date = models.DateField()
    number_of_users_required = models.PositiveSmallIntegerField()
    opensource = models.BooleanField()
    url = models.URLField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
            return self.name
