from django.test import TestCase
from .test_object.TestCars import TestCars
from .test_object.TestUser import TestUser
from .test_object.TestLocation import TestLocation
from .test_object.TestCarTypes import TestCarTypes
from django.urls import reverse


class BookManagerViews(TestCase):
    def setUp(self):
        self.test_user = TestUser()
        self.test_cars = TestCars()
        self.test_location = TestLocation()
        self.test_cartypes = TestCarTypes()

    def login_user(self):
        self.client.login(username=self.test_user, password=self.test_user.password)

    def check_template_use_base(self, response):
        self.assertTemplateUsed(response, 'base.html')

    def check_login_parts(self, response):
        self.assertTemplateUsed(response, 'registration/login.html')
        self.check_template_use_base(response)
        self.assertContains(response, 'name="username"')
        self.assertContains(response, 'name="password"')

    def test_check_redirect_to_login(self):
        for link in ['cars', 'map']:
            response = self.client.get(reverse(link), follow=True)
            self.check_login_parts(response)
        response = self.client.get(reverse('show_cars', args=[self.test_cars.get_test_cars().id]), follow=True)
        self.check_login_parts(response)

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.check_login_parts(response)

    def test_list_cars(self):
        self.login_user()
        response = self.client.get(reverse('cars'))
        self.check_template_use_base(response)
        self.assertTemplateUsed(response, 'cars/list_cars.html')
        self.assertContains(response, self.test_cars.brand)
        self.assertContains(response, self.test_cars.test_location.get_test_location())
        self.assertContains(response, self.test_cars.test_cartypes.get_test_cartypes())
        self.assertContains(response, 'Create new Car')

    def test_list_map(self):
        self.login_user()
        response = self.client.get(reverse('map'))
        self.check_template_use_base(response)
        self.assertTemplateUsed(response, 'map/list_cars.html')
        self.assertContains(response, self.test_location.plz)
        self.assertContains(response, 'Create new Location')
