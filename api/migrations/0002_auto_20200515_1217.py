# Generated by Django 3.0.4 on 2020-05-15 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='username',
            field=models.CharField(default='username', max_length=33, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='api.Author', to_field='username'),
        ),
    ]
