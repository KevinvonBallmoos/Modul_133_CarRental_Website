from map.models import Map


class TestLocation:
    plz = '8000'
    location = 'st-gallen'
    address = 'sdjfa'
    country = 'Schweiz'

    def __init__(self):
        try:
            Map.objects.get(plz=self.plz)
        except Map.DoesNotExist:
            Map.objects.create(
                plz=self.plz,
                location=self.location,
                address=self.address,
                country=self.country
            )

    def get_test_location(self):
        return Map.objects.get(plz=self.plz)
