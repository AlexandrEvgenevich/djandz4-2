# Generated by Django 4.0.1 on 2022-08-18 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='is_main',
            field=models.BooleanField(unique=True),
        ),
    ]
