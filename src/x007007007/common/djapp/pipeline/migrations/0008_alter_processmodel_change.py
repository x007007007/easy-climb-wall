# Generated by Django 4.0.4 on 2022-05-21 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common_pipeline', '0007_alter_processmodel_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processmodel',
            name='change',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common_pipeline.availablenextstatusmodel'),
        ),
    ]
