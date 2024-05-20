# Generated by Django 5.0.6 on 2024-05-11 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DrinkingFountain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_type', models.CharField(max_length=50)),
                ('street_number', models.CharField(max_length=10)),
                ('street_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('available', models.BooleanField(default=True)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
            ],
        ),
    ]
