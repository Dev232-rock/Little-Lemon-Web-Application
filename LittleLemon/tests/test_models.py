from django.test import TestCase
from resturant.models import *

class MenuItemsTest (TestCase):
    def test_get_item(self):
        item = MenuItems.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(str(item), 'IceCream : 80')