from django.db import models


class Map(models.Model):
    """
    map model
    return: location as string
    """
    plz = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.location)
