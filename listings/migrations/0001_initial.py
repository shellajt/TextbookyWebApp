# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('ISBN', models.CharField(max_length=17)),
                ('location', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('listed_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
