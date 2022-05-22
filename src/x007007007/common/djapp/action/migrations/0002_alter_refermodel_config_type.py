# Generated by Django 4.0.4 on 2022-05-20 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('common_action', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refermodel',
            name='config_type',
            field=models.ForeignKey(limit_choices_to={'model__endswith': 'cfgmodel'}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]