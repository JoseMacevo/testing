import unittest
from shoping_cart import item, ShoppingCart


class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.Bread = item("Bread", 2.50)
        self.juice = item("orange_Juice", 3)
        self.ShoppingCart = ShoppingCart()
        self.ShoppingCart.add_item(self.Bread)

    def tearDown(self):
        pass

    def testing_method(self):
        assert 5 + 5 == 10

    def test_item_name_bread(self):
        self.assertEqual(self.Bread.name, "Bread")

    def test_item_not_name(self):
        self.assertNotEqual(self.juice.name, "Apple")

    def test_contains_elements(self):
        self.assertTrue(self.ShoppingCart.contains_items())

    def test_remove_elements(self):
        self.ShoppingCart.remove_items(self.Bread)
        self.assertFalse(self.ShoppingCart.contains_items())


if __name__ == '__main__':
    unittest.main()
