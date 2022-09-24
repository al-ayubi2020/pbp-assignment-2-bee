from django.db import models
import datetime

# Create your models here.
class ToDoListModel(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    date = models.DateField(_("Date"), default=datetime.datetime().now())
    title = models.TextField()
    description = models.TextField()