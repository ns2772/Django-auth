# Generated by Django 5.0.2 on 2024-02-16 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0007_remove_sitesetting_time_zone_customuser_time_zone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='time_zone',
            field=models.CharField(default='EST', max_length=100),
        ),
    ]
