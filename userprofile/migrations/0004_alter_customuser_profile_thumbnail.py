# Generated by Django 5.0.7 on 2024-10-25 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_remove_customuser_google_refresh_token_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='profile_thumbnails'),
        ),
    ]
