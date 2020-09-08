from django.db import models


class Map(models.Model):
    plz = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    country = models.ImageField(upload_to='authors')

    def __str__(self):
        return '{}{}'.format(self.plz, self.location, self.address, self.country)
