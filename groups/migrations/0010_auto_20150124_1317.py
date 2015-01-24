# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0009_group_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='book',
            field=models.CharField(blank=b'True', max_length=b'64', null=b'True'),
        ),
    ]
