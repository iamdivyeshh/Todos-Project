from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Todos(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL, blank=True, null=True)
    todo_name = models.CharField(max_length=100)
    todo_description = models.TextField()