# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-31 10:39
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HauteurHelice', models.IntegerField(default=70, validators=[django.core.validators.MaxValueValidator(125), django.core.validators.MinValueValidator(65)], verbose_name="Hauteur de l'hélice (mm)")),
            ],
        ),
    ]
