from map.models import Map


class TestMap:
    plz = '8645'
    location = 'Jona'
    address = 'Erlenstrasse 109'
    country = 'Schweiz'

    def __init__(self):
        try:
            Map.objects.get(location=self.location)
        except Map.DoesNotExist:
            Map.objects.create(
                plz=self.plz,
                location=self.location,
                address=self.address,
                country=self.country
            )

    def get_test_location(self):
        return Map.objects.get(location=self.location)