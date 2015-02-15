# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_remove_group_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='address',
            field=models.CharField(default=b'', max_length=b'64'),
            preserve_default=True,
        ),
    ]
