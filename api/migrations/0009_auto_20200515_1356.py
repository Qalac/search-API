# Generated by Django 3.0.4 on 2020-05-15 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200515_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.CharField(default='example.com', max_length=44),
        ),
    ]
