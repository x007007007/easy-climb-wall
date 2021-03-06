# Generated by Django 4.0.4 on 2022-05-22 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common_callback_proxy', '0002_configmodel_action'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('request', models.TextField()),
                ('header', models.JSONField()),
                ('params', models.TextField()),
                ('config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_callback_proxy.configmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ConfigAPISchemaItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('type', models.CharField(choices=[('BaseSerializer', 'BaseSerializer'), ('BooleanField', 'BooleanField'), ('CharField', 'CharField'), ('ChoiceField', 'ChoiceField'), ('DateField', 'DateField'), ('DateTimeField', 'DateTimeField'), ('DecimalField', 'DecimalField'), ('DictField', 'DictField'), ('DurationField', 'DurationField'), ('EmailField', 'EmailField'), ('Field', 'Field'), ('FileField', 'FileField'), ('FilePathField', 'FilePathField'), ('FloatField', 'FloatField'), ('HStoreField', 'HStoreField'), ('HiddenField', 'HiddenField'), ('HyperlinkedIdentityField', 'HyperlinkedIdentityField'), ('HyperlinkedModelSerializer', 'HyperlinkedModelSerializer'), ('HyperlinkedRelatedField', 'HyperlinkedRelatedField'), ('IPAddressField', 'IPAddressField'), ('ImageField', 'ImageField'), ('IntegerField', 'IntegerField'), ('JSONField', 'JSONField'), ('ListField', 'ListField'), ('ListSerializer', 'ListSerializer'), ('ManyRelatedField', 'ManyRelatedField'), ('ModelField', 'ModelField'), ('ModelSerializer', 'ModelSerializer'), ('MultipleChoiceField', 'MultipleChoiceField'), ('NullBooleanField', 'NullBooleanField'), ('PrimaryKeyRelatedField', 'PrimaryKeyRelatedField'), ('ReadOnlyField', 'ReadOnlyField'), ('RegexField', 'RegexField'), ('RelatedField', 'RelatedField'), ('Serializer', 'Serializer'), ('SerializerMethodField', 'SerializerMethodField'), ('SlugField', 'SlugField'), ('SlugRelatedField', 'SlugRelatedField'), ('StringRelatedField', 'StringRelatedField'), ('TimeField', 'TimeField'), ('URLField', 'URLField'), ('UUIDField', 'UUIDField')], max_length=64)),
                ('extra', models.JSONField(blank=True, default=dict, null=True)),
                ('config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_callback_proxy.configmodel')),
            ],
        ),
    ]
