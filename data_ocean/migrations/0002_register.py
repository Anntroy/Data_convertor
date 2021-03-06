# Generated by Django 2.0.9 on 2020-06-01 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_ocean', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('name', models.CharField(max_length=500, unique=True)),
                ('source_name', models.CharField(max_length=300)),
                ('source_register_id', models.URLField(max_length=300, unique=True)),
                ('url_address', models.URLField(max_length=500)),
                ('api_address', models.URLField(max_length=500, null=True)),
                ('source_last_update', models.DateTimeField(default=None, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
