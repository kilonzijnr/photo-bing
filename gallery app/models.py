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


class Image(models.Model):
    image = models.ImageField(upload_to='photos/', default=None)
    name = models.CharField(max_length= 30)
    description = models.TextField()
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, default=None)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id_icontains = id)
        return image

    @classmethod
    def get_image_by_category(cls, category):
        image = cls.objects.filter(category_icontains=category)
        return image

    @classmethod
    def get_image_by_location(cls, location):
        image = cls.objects.filter(location_icontains=location)
        return image

    @classmethod
    def search_by_name(cls, search_term):
        images = cls.objects.filter(name_icontains= search_term)
        return images


