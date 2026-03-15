from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class PublicNote(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    file = models.FileField(upload_to='public_notes/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title