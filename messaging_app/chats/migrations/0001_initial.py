# Generated by Django 5.1.4 on 2024-12-19 02:08

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password_hash', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('role', models.CharField(choices=[('guest', 'Guest'), ('host', 'Host'), ('admin', 'Admin')], default='guest', max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('message_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('message_body', models.TextField()),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('sender_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='chats.user')),
            ],
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('conversation_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('participants_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='chats.user')),
            ],
        ),
    ]
