# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstladyswap', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='president',
            old_name='real1stlady',
            new_name='presimg',
        ),
        migrations.AddField(
            model_name='president',
            name='realfirstlady',
            field=models.CharField(default='.jpg', max_length=80),
            preserve_default=False,
        ),
    ]
