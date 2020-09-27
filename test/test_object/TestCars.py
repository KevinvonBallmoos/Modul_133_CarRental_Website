from cars.models import Cars
from test.test_object.TestMap import TestMap
from test.test_object.TestCarTypes import TestCarTypes


class TestCars:
    brand = 'Audi'
    model = 'A3'
    ps = '200'
    details = 'Ledersitze'
    image = 'AudiA3.jpg'
    test_location = TestMap()
    test_cartypes = TestCarTypes()

    def __init__(self):
        try:
            Cars.objects.get(brand=self.brand)
        except Cars.DoesNotExist:
            Cars.objects.create(
                brand=self.brand,
                model=self.model,
                ps=self.ps,
                details=self.details,
                image=self.image,
                location=self.test_location.get_test_location(),
                types=self.test_cartypes.get_test_cartypes()
            )

    def get_test_cars(self):
        return Cars.objects.get(brand=self.brand)