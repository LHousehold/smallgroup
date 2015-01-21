# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='coordinator',
            field=models.CharField(max_length=64, null=b'True'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='description',
            field=models.CharField(default=b'smallgroup', max_length=b'1280'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='leader2',
            field=models.ForeignKey(related_name='leader2_group_related', to='groups.Leader', null=b'True'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='leader',
            field=models.ForeignKey(related_name='leader_group_related', to='groups.Leader'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(default=b'New smallgroup', max_length=64),
            preserve_default=True,
        ),
    ]
