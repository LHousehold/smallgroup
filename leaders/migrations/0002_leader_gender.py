# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leader',
            name='gender',
            field=models.CharField(default=b'Male', max_length=12, choices=[(b'Male', b'Male'), (b'Female', b'Female')]),
            preserve_default=True,
        ),
    ]
