# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-28 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=300)),
                ('image_location', models.CharField(max_length=500)),
                ('image_category', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]