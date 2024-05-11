# Generated by Django 5.0.6 on 2024-05-11 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spots', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sanisette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=10)),
                ('hours', models.CharField(max_length=50)),
                ('access_pmr', models.BooleanField(default=False)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='drinkingfountain',
            name='street_name',
        ),
        migrations.RemoveField(
            model_name='drinkingfountain',
            name='street_number',
        ),
        migrations.AddField(
            model_name='drinkingfountain',
            name='address',
            field=models.CharField(default='undefined', max_length=255),
            preserve_default=False,
        ),
    ]
