# Generated by Django 2.2.13 on 2020-06-09 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location_register', '0002_auto_20200602_1449_squashed_0010_auto_20200605_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drvstreet',
            name='code',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]