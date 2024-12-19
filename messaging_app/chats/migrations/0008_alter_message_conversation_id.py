# Generated by Django 5.1.4 on 2024-12-19 17:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0007_remove_conversation_participants_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='conversation_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chats.conversation'),
        ),
    ]
