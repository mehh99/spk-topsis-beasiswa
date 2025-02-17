# Generated by Django 4.2.7 on 2023-11-23 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('economic_condition', models.IntegerField()),
                ('house_condition', models.IntegerField()),
                ('parent_occupation', models.IntegerField()),
                ('parent_income', models.IntegerField()),
                ('parent_status', models.IntegerField()),
                ('parent_dependents', models.IntegerField()),
            ],
        ),
    ]
