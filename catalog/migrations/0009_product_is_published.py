# Generated by Django 5.0.1 on 2024-02-03 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_rename_name_product_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='положительно опубликованы'),
        ),
    ]
