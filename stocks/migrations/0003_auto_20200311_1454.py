# Generated by Django 3.0.2 on 2020-03-11 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_auto_20200311_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='IsListed',
            field=models.BooleanField(default=False, verbose_name='IsListed'),
        ),
    ]
