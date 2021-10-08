from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.

#category class
class Category(models.Model):
    name = models.CharField(max_length= 30)

    def __str__(self):
        return self.name
