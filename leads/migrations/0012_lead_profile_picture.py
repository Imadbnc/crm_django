# Generated by Django 3.1.4 on 2022-11-14 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0011_auto_20221009_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]