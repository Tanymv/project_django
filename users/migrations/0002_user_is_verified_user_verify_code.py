# Generated by Django 5.0.1 on 2024-02-06 10:25

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='Верификация'),
        ),
        migrations.AddField(
            model_name='user',
            name='verify_code',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Код вeрификации'),
        ),
    ]