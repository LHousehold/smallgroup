# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0008_auto_20150124_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='book',
            field=models.CharField(blank=b'True', max_length=b'32', null=b'True'),
        ),
    ]
