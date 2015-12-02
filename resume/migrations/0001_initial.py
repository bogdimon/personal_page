# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.IntegerField(default=1, choices=[(1, b'Job'), (2, b'Education'), (3, b'Skill')])),
                ('name', models.CharField(max_length=50)),
                ('level', models.IntegerField(default=70, choices=[(20, b'Basic'), (50, b'Good'), (70, b'Fluent'), (100, b'Godlike')])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
