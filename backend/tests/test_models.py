from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item=Menu.objects.create(title='pasta',price=20.00,inventory=10)
        self.assertEqual(str(item),'pasta : 20.00')