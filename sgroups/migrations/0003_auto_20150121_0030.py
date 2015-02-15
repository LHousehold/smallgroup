# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20150121_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='coordinator',
            field=models.CharField(max_length=64, null=b'True', blank=b'True'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='group_type',
            field=models.CharField(default=b'Men', max_length=8, choices=[(b'Men', b'Men'), (b'Women', b'Women'), (b'Couples', b'Couples'), (b'Mixed', b'Mixed')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='leader2',
            field=models.ForeignKey(related_name='leader2_group_related', blank=b'True', to='groups.Leader', null=b'True'),
            preserve_default=True,
        ),
    ]
