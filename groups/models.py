from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    description = models.TextField()

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='study_groups')

    def _str_(self):
        return self.name
