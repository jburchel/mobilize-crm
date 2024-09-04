# Generated by Django 5.0.7 on 2024-09-04 16:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ComLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('interaction_type', models.CharField(max_length=20)),
                ('communication_type', models.CharField(choices=[('email', 'Email'), ('phone', 'Phone'), ('text', 'Text'), ('meeting', 'Meeting'), ('video', 'Video Conference'), ('facebook', 'Facebook Messenger'), ('whatsapp', 'WhatsApp'), ('signal', 'Signal')], max_length=20)),
                ('subject', models.CharField(blank=True, max_length=255)),
                ('notes', models.TextField()),
                ('direction', models.CharField(choices=[('Incoming', 'Incoming'), ('Outgoing', 'Outgoing')], default='Outgoing', max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
