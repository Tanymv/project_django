# Generated by Django 5.0.1 on 2024-02-02 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='number_views',
            field=models.IntegerField(verbose_name='количество просмотров'),
        ),
    ]
