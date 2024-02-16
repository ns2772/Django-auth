# Generated by Django 5.0.2 on 2024-02-16 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0005_emailverificationtoken_time_zone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailverificationtoken',
            name='time_zone',
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='time_zone',
            field=models.CharField(default='UTC', max_length=100),
        ),
    ]