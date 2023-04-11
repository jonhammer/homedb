from django.test import TestCase

from .models import House


class HouseTestCase(TestCase):
    def setUp(self):
        House.objects.create(name="Test House")

    def test_house_name(self):
        house = House.objects.get(name="Test House")
        self.assertEqual(house.name, "Test House")
