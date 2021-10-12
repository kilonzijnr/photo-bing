from os import name
from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length= 30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Category(models.Model):
    name = models.CharField(max_length= 30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_caategory(self):
        self.delete()

