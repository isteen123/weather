# Generated by Django 4.2.4 on 2023-08-25 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('Temperature', models.FloatField()),
                ('Humidity', models.FloatField()),
                ('Conditions', models.CharField(max_length=100)),
            ],
        ),
    ]
