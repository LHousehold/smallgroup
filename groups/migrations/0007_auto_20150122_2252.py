# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0006_group_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='address',
            field=models.CharField(default=b'', max_length=b'32'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.CharField(default=b'', max_length=b'1280'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='group_type',
            field=models.CharField(default=b'Men', max_length=8, choices=[(b'Men', b'Men'), (b'Women', b'Women'), (b'Couples', b'Couples'), (b'Co-ed', b'Co-ed')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(default=b'', max_length=64),
            preserve_default=True,
        ),
    ]
