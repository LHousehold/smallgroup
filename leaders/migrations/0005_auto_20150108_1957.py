# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaders', '0004_auto_20150108_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leader',
            name='picture',
            field=models.ImageField(default=b'/static/images/blank_avatar.jpg', height_field=b'300', width_field=b'300', upload_to=b''),
            preserve_default=True,
        ),
    ]
