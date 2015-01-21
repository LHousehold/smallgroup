# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_group_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='topic',
        ),
    ]
