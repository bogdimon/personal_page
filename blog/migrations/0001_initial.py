# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('publish_date', models.DateField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('url', models.URLField()),
                ('thumbnail', models.CharField(max_length=200)),
            ],
        ),
    ]
