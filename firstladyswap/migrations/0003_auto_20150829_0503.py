# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstladyswap', '0002_auto_20150825_0256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firstlady',
            name='president',
        ),
        migrations.DeleteModel(
            name='FirstLady',
        ),
        migrations.DeleteModel(
            name='President',
        ),
    ]
