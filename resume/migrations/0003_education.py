# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20151202_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.IntegerField(default=1, choices=[(1, b'Job'), (2, b'Education'), (3, b'Skill')])),
                ('name', models.CharField(max_length=50)),
                ('institution', models.CharField(max_length=50)),
                ('level', models.IntegerField(choices=[(1, b"Master's"), (2, b"Bachelor's")])),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
