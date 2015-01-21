# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_auto_20150121_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='topic',
            field=models.CharField(default=b'', max_length=b'32'),
            preserve_default=True,
        ),
    ]
