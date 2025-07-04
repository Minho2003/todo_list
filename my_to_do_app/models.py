from django.db import models

# Create your models here.

class ToDo(models.Model):
    content = models.CharField(max_length=200)
    date_time= models.DateTimeField(auto_now_add=True)

class Trash(models.Model):
    content = models.CharField(max_length=200)
    date_time= models.DateTimeField(auto_now_add=True)

    