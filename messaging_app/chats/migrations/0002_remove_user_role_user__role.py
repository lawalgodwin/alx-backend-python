# Generated by Django 5.1.4 on 2025-01-20 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
        migrations.AddField(
            model_name='user',
            name='_role',
            field=models.CharField(choices=[('guest', 'GUEST'), ('host', 'HOST'), ('admin', 'ADMIN')], default='guest', max_length=5),
        ),
    ]
