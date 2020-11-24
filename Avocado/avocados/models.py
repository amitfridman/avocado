from django.db import models
import datetime


class Avocado(models.Model):
    total_volume = models.FloatField()
    total_bags = models.FloatField()
    small_bags = models.FloatField()
    large_bags = models.FloatField()
    x_large_bags = models.FloatField()
    type = models.CharField(max_length=15, choices=[('conventional', 0), ('organic', 1)])
    year = models.IntegerField(choices=[(i, i) for i in range(1950, datetime.datetime.now().year + 1)])
    region = models.CharField(max_length=20)
    t_4046 = models.FloatField()
    t_4225 = models.FloatField()
    t_4770 = models.FloatField()
    average_price = models.FloatField(default=0)




