
from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.

#category class
class Category(models.Model):
    name = models.CharField(max_length= 40)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self, update):
        self.name = update
        self.save() 

    @classmethod
    def get_category_id(cls, id):
        category = Category.objects.get(pk = id)
        return category

    def __str__(self):
        return self.name


    # location class

class Location(models.Model):
    
              

