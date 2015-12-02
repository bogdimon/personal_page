# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='subcategory',
            field=models.CharField(default='', max_length=4, choices=[(b'LANG', b'Language'), (b'TECH', b'Technical (?)')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='skill',
            name='level',
            field=models.IntegerField(default=70, blank=True, choices=[(20, b'Basic'), (50, b'Good'), (70, b'Fluent'), (100, b'Godlike')]),
        ),
    ]
