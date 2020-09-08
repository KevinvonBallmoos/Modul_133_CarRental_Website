from django.db import models
from map.models import Map


class Cars(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    ps = models.IntegerField(max_length=255)
    details = models.ImageField(max_length=255)
    image = models.ImageField(upload_to='cars')
    map = models.ManyToOneRel(Map)

    def __str__(self):
        return '{}{}'.format(self.brand, self.model, self.ps, self.details, self.image,self.map)

