# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FirstLady',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('lady_name', models.CharField(max_length=80)),
                ('image', models.CharField(max_length=80)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='President',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('pres_name', models.CharField(max_length=80)),
                ('real1stlady', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='firstlady',
            name='president',
            field=models.ForeignKey(to='firstladyswap.President'),
        ),
    ]
