# Generated by Django 3.1.5 on 2021-01-28 03:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_standarduser_politician_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='standarduser',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
