from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    title = models.TextField()
    description = models.TextField()
    is_finished = models.BooleanField(default=False)