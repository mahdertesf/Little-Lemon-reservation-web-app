from django.test import TestCase 
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework import status
class MenuViewTest(TestCase):
    def setUp(self):
        self.menu_item1=Menu.objects.create(title='Pizza',price=10.00,inventory=10)
        self.menu_item2=Menu.objects.create(title='Pasta',price=12.00,inventory=10)
        self.menu_item3=Menu.objects.create(title='Salad',price=8.00,inventory=10)
        
        
        self.client=APIClient()
        
    def test_get_all(self):
        response = self.client.get('/api/menu/')
        expected_data = MenuSerializer(Menu.objects.all(), many=True).data
        
        self.assertEqual(response.data, expected_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)