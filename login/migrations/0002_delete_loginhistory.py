# Generated by Django 4.2.7 on 2024-01-25 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LoginHistory',
        ),
    ]