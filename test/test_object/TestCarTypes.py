from cars.models import CarTypes


class TestCarTypes:
    types = 'Limousine'

    def __init__(self):
        try:
            CarTypes.objects.get(types=self.types)
        except CarTypes.DoesNotExist:
            CarTypes.objects.create(
                types=self.types,
            )

    def get_test_cartypes(self):
        return CarTypes.objects.get(types=self.types)