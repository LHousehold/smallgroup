# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaders', '0009_auto_20150108_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leader',
            name='picture',
            field=models.ImageField(default=b'/static/images/blank_avatar.jpg', upload_to=b'leaders/static/images/'),
            preserve_default=True,
        ),
    ]
