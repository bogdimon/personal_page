# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_education'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='enddate',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='education',
            old_name='startdate',
            new_name='start_date',
        ),
    ]
