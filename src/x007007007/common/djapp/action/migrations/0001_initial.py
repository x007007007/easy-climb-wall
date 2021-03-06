# Generated by Django 4.0.4 on 2022-05-20 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiHookCfgModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('action_func', models.CharField(max_length=254)),
                ('url', models.CharField(max_length=254)),
                ('method', models.CharField(choices=[('HEAD', 'HEAD'), ('GET', 'GET'), ('POST', 'POST'), ('DELETE', 'DELETE'), ('PUT', 'PUT'), ('PATCH', 'PATCH'), ('OPTIONAL', 'OPTIONAL')], max_length=8)),
                ('header', models.JSONField(blank=True, null=True)),
                ('body_template', models.TextField(blank=True, default=None, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CeleryCfgModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('action_func', models.CharField(max_length=254)),
                ('task_name', models.CharField(max_length=254)),
                ('queue_name', models.CharField(max_length=254)),
                ('broken_url', models.CharField(max_length=254)),
                ('backend', models.CharField(max_length=254)),
                ('task_args', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReferModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('config_id', models.PositiveIntegerField()),
                ('enable', models.BooleanField(default=True)),
                ('config_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'unique_together': {('config_type', 'config_id')},
            },
        ),
    ]
