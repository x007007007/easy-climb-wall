# Generated by Django 4.0.4 on 2022-05-18 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climb_wall_config', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proxyconfigmodel',
            name='pid',
            field=models.IntegerField(editable=False, null=True),
        ),
    ]
