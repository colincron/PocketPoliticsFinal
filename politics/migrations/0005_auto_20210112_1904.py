# Generated by Django 3.1.4 on 2021-01-13 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('politics', '0004_auto_20210112_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='politician',
            name='image_url',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]