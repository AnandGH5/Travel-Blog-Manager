# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-22 11:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authen', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('location', models.CharField(blank=True, max_length=500, null=True)),
                ('date', models.CharField(blank=True, max_length=500, null=True)),
                ('time', models.CharField(blank=True, max_length=500, null=True)),
                ('viewcount', models.IntegerField(default=0)),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authen.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='flyerphotos')),
                ('flyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='explore.Flyer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authen.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, null=True, upload_to='flyervideos')),
                ('flyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='explore.Flyer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authen.Profile')),
            ],
        ),
    ]