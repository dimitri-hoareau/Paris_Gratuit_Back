# Generated by Django 5.0.2 on 2024-05-29 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_event_price_detail_event_price_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='price_detail',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
