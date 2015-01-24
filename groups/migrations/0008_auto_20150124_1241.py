# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0007_auto_20150122_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='location',
            field=models.CharField(blank=b'True', max_length=b'32', null=b'True'),
        ),
        migrations.AlterField(
            model_name='group',
            name='time',
            field=models.CharField(max_length=b'8'),
        ),
    ]
