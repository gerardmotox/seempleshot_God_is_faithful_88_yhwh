# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from location_field.models.spatial import LocationField

from django.db import models
from multiselectfield import MultiSelectField

class Tags(models.Model):
    name = models.CharField(max_length = 200, null=True)

    def __str__(self):
        return self.name

class ImageUpload(models.Model):
    user_id = models.CharField(max_length = 200)
    username = models.CharField(max_length = 300)
    photo = models.ImageField(default='default.png', blank=True)
    image_location = models.CharField(max_length = 500)
    image_category = models.CharField(max_length = 200)
    tags = models.ManyToManyField(Tags)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.user_id +" "+ self.username

class MainCategories(models.Model):
    icon = models.ImageField(default='default.png', blank=False)
    category_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.category_name

# Create your models here.
