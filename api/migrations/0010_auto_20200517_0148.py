# Generated by Django 3.0.4 on 2020-05-17 01:48

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20200515_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=33), blank=True, null=True, size=None),
        ),
    ]
