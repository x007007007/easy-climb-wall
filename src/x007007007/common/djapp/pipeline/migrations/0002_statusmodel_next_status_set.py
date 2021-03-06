# Generated by Django 4.0.4 on 2022-05-18 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_pipeline', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusmodel',
            name='next_status_set',
            field=models.ManyToManyField(related_name='pre_status_set', through='common_pipeline.AvailableNextStatusModel', to='common_pipeline.statusmodel'),
        ),
    ]
