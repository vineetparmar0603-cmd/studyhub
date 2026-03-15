from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    description = models.TextField()

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='study_groups')

    def __str__(self):
        return self.name

class Note(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='group_notes/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title