# Generated by Django 5.0.7 on 2024-09-03 12:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('com_log', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comlog',
            options={'ordering': ['-date_created']},
        ),
        migrations.RenameField(
            model_name='comlog',
            old_name='date',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='comlog',
            old_name='summary',
            new_name='notes',
        ),
        migrations.AddField(
            model_name='comlog',
            name='direction',
            field=models.CharField(choices=[('Incoming', 'Incoming'), ('Outgoing', 'Outgoing')], default='Outgoing', max_length=10),
        ),
        migrations.AddField(
            model_name='comlog',
            name='interaction_type',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comlog',
            name='subject',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='comlog',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comlog',
            name='content_type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comlog',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]