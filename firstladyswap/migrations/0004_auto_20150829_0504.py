# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstladyswap', '0003_auto_20150829_0503'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstLady',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('lady_name', models.CharField(max_length=80)),
                ('image', models.CharField(max_length=80)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='President',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('pres_name', models.CharField(max_length=80)),
                ('presimg', models.CharField(max_length=80)),
                ('realfirstlady', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='firstlady',
            name='president',
            field=models.ForeignKey(to='firstladyswap.President'),
        ),
    ]
