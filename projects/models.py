from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

from users.models import Skill, User


class Project(models.Model):
    users = models.ManyToManyField(User)
    skills = models.ManyToManyField(Skill, blank=True)
    name = models.CharField(
        _("Name of the project"), max_length=255, unique=True)
    description = models.TextField()
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
