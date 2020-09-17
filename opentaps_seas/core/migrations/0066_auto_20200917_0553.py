# Generated by Django 2.2.10 on 2020-09-17 12:53

import cratedb.fields.array
import cratedb.fields.hstore
from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0065_auto_20200917_0502'),
    ]

    operations = [
        migrations.AddField(
            model_name='utility',
            name='division_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='utility',
            name='division_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
