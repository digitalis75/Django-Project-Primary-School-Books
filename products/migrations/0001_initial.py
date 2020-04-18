# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-17 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('author', models.CharField(default='', max_length=254)),
                ('school_level', models.CharField(default='', max_length=40)),
                ('stage', models.CharField(default='', max_length=40)),
                ('subject', models.CharField(default='', max_length=40)),
                ('publisher', models.CharField(default='', max_length=50)),
                ('product', models.CharField(default='', max_length=20)),
                ('cover_format', models.CharField(default='', max_length=20)),
                ('language', models.CharField(default='', max_length=40)),
                ('pages', models.IntegerField()),
                ('publication_year', models.IntegerField()),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(upload_to='images')),
                ('status', models.CharField(choices=[('IN_STOCK', 'In Stock'), ('TEMP_OUT_OF_STOCK', 'Temporary Out of Stock')], max_length=40)),
            ],
        ),
    ]