# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0010_auto_20150124_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_style',
            field=models.CharField(max_length=32, null=b'True', blank=b'True'),
        ),
        migrations.AddField(
            model_name='group',
            name='leader3',
            field=models.ForeignKey(related_name='leader3_group_related', blank=b'True', to='groups.Leader', null=b'True'),
        ),
    ]
