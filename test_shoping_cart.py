import unittest
from shoping_cart import Item, ShoppingCart


class TestShoppingCart(unittest.TestCase):
    def testing_method(self):
        assert 5 + 5 == 10

    def test_item_name(self):
        item = Item("Apple", 12.0)
        self.assertEqual(item.name, "Apple")

    def test_item_not_name(self):
        item = Item("whitebread", 15.0)
        self.assertNotEqual(item.name, "Apple")


if __name__ == '__main__':
    unittest.main()
