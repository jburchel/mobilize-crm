# Generated by Django 5.0.7 on 2024-08-28 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='signature_logo',
            field=models.ImageField(blank=True, null=True, upload_to='signature_logos/'),
        ),
    ]
