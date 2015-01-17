# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'New Smallgroup', max_length=64)),
                ('group_type', models.CharField(default=b'Men', max_length=8, choices=[(b'Men', b'Men'), (b'Women', b'Women'), (b'Couples', b'Couples')])),
                ('picture', models.ImageField(default=b'images/empty_room.jpg', upload_to=b'images/')),
                ('location', models.CharField(max_length=b'32')),
                ('day', models.CharField(max_length=b'12', choices=[(b'Mon', b'Monday'), (b'Tue', b'Tuesday'), (b'Wed', b'Wednesday'), (b'Thu', b'Thursday'), (b'Fri', b'Friday'), (b'Sat', b'Saturday'), (b'Sun', b'Sunday')])),
                ('time', models.DateTimeField()),
            ],
            options=None,
            bases=None,
        ),
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(default=b'Male', max_length=12, choices=[(b'Male', b'Male'), (b'Female', b'Female')])),
                ('picture', models.ImageField(default=b'images/blank_avatar.gif', upload_to=b'images/')),
            ],
            options=None,
            bases=None,
        ),
        migrations.AddField(
            model_name='group',
            name='leader',
            field=models.ForeignKey(to='groups.Leader'),
            preserve_default=True,
        ),
    ]
