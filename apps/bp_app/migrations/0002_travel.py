# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 22:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bp_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=500)),
                ('travelstart', models.DateTimeField()),
                ('travelend', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('join', models.ManyToManyField(related_name='jointravels', to='bp_app.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='bp_app.User')),
            ],
        ),
    ]