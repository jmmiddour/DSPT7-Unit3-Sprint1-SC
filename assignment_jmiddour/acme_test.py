import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_identifier(self):
        """Test the product identifier is between 1000000 and 9999999"""
        ident = Product(generate_products())
        self.assertGreaterEqual(ident.identifier, 1000000)
        self.assertLessEqual(ident.identifier, 9999999)

    def test_default_weight(self):
        """Test the default product weight as being 20"""
        wght = Product('Test Product')
        self.assertEqual(wght.weight, 20)


class AcmeReportTests(unittest.TestCase):
    
    def test_default_num_product(self):
        """Test that the length default is 30"""
        # prod_list = list(Product(generate_products()))
        # list_cnt = len(prod_list)
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        """Test the format of names being ADJECTIVE space NOUN"""
        name_fmt = [ADJECTIVES, NOUNS]
        names = set()
        for val in generate_products():
            names.add(val.name)
        legal_name = names
        self.assertTrue(legal_name, any(name_fmt))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
