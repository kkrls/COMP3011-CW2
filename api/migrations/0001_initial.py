# Generated by Django 4.2.1 on 2023-05-26 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_seats', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
