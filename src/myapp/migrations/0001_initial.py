# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-08 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
    ]
