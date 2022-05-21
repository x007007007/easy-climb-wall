# Generated by Django 4.0.4 on 2022-05-21 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common_pipeline', '0005_changestatusstrategymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='changestatusactionmodel',
            name='group',
            field=models.CharField(choices=[('pre_changed', 'pre_changed'), ('post_changed', 'post_changed')], default='post_changed', max_length=16),
        ),
        migrations.AddField(
            model_name='changestatusactionmodel',
            name='strategy',
            field=models.CharField(choices=[('requisite', 'requisite'), ('optional', 'optional')], default='optional', max_length=16),
        ),
        migrations.AddField(
            model_name='processmodel',
            name='change_action',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common_pipeline.changestatusactionmodel'),
        ),
        migrations.AlterField(
            model_name='changestatusstrategymodel',
            name='sub_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common_pipeline.templatemodel'),
        ),
        migrations.AlterField(
            model_name='processmodel',
            name='current_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common_pipeline.statusmodel'),
        ),
        migrations.AlterField(
            model_name='templatemodel',
            name='start_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common_pipeline.statusmodel'),
        ),
        migrations.CreateModel(
            name='StatusChangeLogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=254)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_pipeline.processmodel')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common_pipeline.statusmodel')),
            ],
        ),
        migrations.AddField(
            model_name='processmodel',
            name='change',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common_pipeline.statuschangelogmodel'),
        ),
    ]
