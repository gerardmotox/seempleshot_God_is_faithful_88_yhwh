# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from location_field.models.spatial import LocationField

from django.db import models

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

class PostJob(models.Model):
    user_id = models.CharField(max_length = 200)
    username = models.CharField(max_length = 300)
    looking_for = models.CharField(max_length = 50)
    job_category = models.CharField(max_length = 50)
    job_location = models.CharField(max_length = 500)
    job_location_details = models.TextField()
    job_start_date_time = models.DateTimeField(auto_now_add = True)
    job_days = models.CharField(max_length = 50)
    job_length = models.FloatField(null = True)
    job_showcase = models.CharField(max_length = 50)

    def __str__(self):
        return self.looking_for

class Pro_Business_Info(models.Model):
    USERTYPE = (
        ('Photographer', 'Photographer'),
        ('Videographer', 'Videographer'),
        ('Both', 'Both'),
    )
    TEXTCHOICE = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    user_id = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    phone_number = models.FloatField(null = True)
    enable_text = models.CharField(max_length = 200, choices = TEXTCHOICE)
    moto = models.TextField()
    line_of_work = models.CharField(max_length = 200, choices = USERTYPE)
    business_address = models.CharField(max_length = 200)
    street_num = models.CharField(max_length = 200)
    street_name = models.CharField(max_length = 500)
    city = models.CharField(max_length = 200)
    state = models.CharField(max_length = 200)
    zip = models.CharField(max_length = 200)
    country = models.CharField(max_length = 200)


    def __str__(self):
        return self.username

class Pro_Available_Days(models.Model):
    DAYS = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednsday', 'Wednsday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    user_id = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200)
    days_to_work = models.CharField(max_length = 50, null = True, choices = DAYS)


    def __str__(self):
        return self.username

class Pro_Package_Offer(models.Model):
    PACKAGE = (
        ('Portrait', 'Portrait'),
        ('Family', 'Family'),
        ('Graduation', 'Graduation'),
    )
    user_id = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200)
    # username = models.ForeignKey(ImageUpload, null=True, on_delete = models.SET_NULL)
    package_name = models.CharField(max_length = 200, choices = PACKAGE)
    package_price = models.FloatField(null = True)
    package_details = models.TextField()

    def __str__(self):
        return self.username

# Create your models here.
