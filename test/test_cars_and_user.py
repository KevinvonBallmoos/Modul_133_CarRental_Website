from django.test import TestCase
from .test_object.TestCars import TestCars
from .test_object.TestUser import TestUser
from .test_object.TestMap import TestMap
from django.urls import reverse


class CarsAndMapViews(TestCase):
    def setUp(self):
        self.test_user = TestUser()
        self.test_location = TestMap()
        self.test_cars = TestCars()

    def login_user(self):
        self.client.login(username=self.test_user, password=self.test_user.password)

    def check_template_use_base(self, response):
        self.assertTemplateUsed(response, 'base_home/base.html')

    def check_login_parts(self, response):
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertContains(response, 'name="username"')
        self.assertContains(response, 'name="password"')

    def test_check_redirect_to_login(self):
        for link in ['list_cars', 'list_map']:
            response = self.client.get(reverse(link), follow=True)
            self.check_login_parts(response)
        response = self.client.get(reverse('show_cars', args=[self.test_cars.get_test_cars().id]), follow=True)
        self.check_login_parts(response)
        response = self.client.get(reverse('show_cars', args=[self.test_location.get_test_location().id]),
                                   follow=True)
        self.check_login_parts(response)

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.check_login_parts(response)

    def test_list_cars(self):
        self.login_user()
        response = self.client.get(reverse('list_cars'))
        self.check_template_use_base(response)
        self.assertTemplateUsed(response, 'functions/list_cars.html')
        self.assertContains(response, self.test_cars.brand)
        self.assertContains(response, self.test_cars.test_location.get_test_location())
        self.assertContains(response, 'Create new Car')

    def test_list_map(self):
        self.login_user()
        response = self.client.get(reverse('list_map'))
        self.assertRedirects(response, 'functions/list_cars')
        self.assertContains(response, self.test_location.location)
        self.assertContains(response, 'Create new Location')
