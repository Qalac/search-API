# Generated by Django 3.0.4 on 2020-05-15 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200515_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='username',
            field=models.CharField(default='username', max_length=33, unique=True),
        ),
    ]
