from django.db import models
from datetime import datetime
from django.conf import settings


# Create your models here.
class ToDoListModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    title = models.TextField()
    description = models.TextField()
    is_finished = models.BooleanField(default=False)