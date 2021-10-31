from django.db import models

# Create your models here

class MyModel(models.Model):
    param_name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
