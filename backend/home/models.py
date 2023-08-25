from django.db import models

class WeatherData(models.Model):
    Location = models.CharField(max_length=100)
    Temperature = models.FloatField()
    Humidity = models.FloatField()
    Conditions = models.CharField(max_length=100)
