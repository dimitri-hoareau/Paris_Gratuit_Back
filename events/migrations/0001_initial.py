# Generated by Django 5.0.6 on 2024-05-28 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=255)),
                ('lead_text', models.TextField()),
                ('description', models.TextField()),
                ('date_start', models.DateTimeField(blank=True, null=True)),
                ('date_end', models.DateTimeField(blank=True, null=True)),
                ('occurrences', models.JSONField(blank=True, null=True)),
                ('date_description', models.TextField(blank=True, null=True)),
                ('cover_url', models.URLField(blank=True, null=True)),
                ('cover_alt', models.CharField(blank=True, max_length=255, null=True)),
                ('cover_credit', models.CharField(blank=True, max_length=255, null=True)),
                ('tags', models.JSONField(blank=True, null=True)),
                ('address_name', models.CharField(max_length=255)),
                ('address_street', models.CharField(max_length=255)),
                ('address_zipcode', models.CharField(max_length=10)),
                ('address_city', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
    ]
