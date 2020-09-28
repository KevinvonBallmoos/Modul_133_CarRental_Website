from django.db import models
from map.models import Map


class Cars(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    ps = models.IntegerField()
    details = models.CharField(max_length=255)
    image = models.ImageField(upload_to='cars')
    location = models.ForeignKey(Map, on_delete=models.RESTRICT)
    types = models.CharField(max_length=255)

    def __str__(self):
        return '{}{}'.format(self.brand, self.model)
