import unittest
from shoping_cart import item

class TestShoppingCart(unittest.TestCase):
    def testing_method(self):
        assert 5 + 5 == 10


    def test_item_name(self):
        Item = item("Apple", 12.0)
        self.assertEqual(Item.name, "Apple")
    

    def test_item_not_name(self):
        Item = item("whitebread", 15.0)
        self.assertNotEqual(Item.name, "Apple")


if __name__ == '__main__':
    unittest.main()


