# Generated by Django 3.0 on 2019-12-08 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cores', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='config',
            options={'verbose_name': 'config', 'verbose_name_plural': 'configs'},
        ),
    ]