# project/tests/test_auth.py

from project.tests.base import BaseTestCase
from project.tests.helper.createdata import add_products
import json


class TestProductList(BaseTestCase):
    def test_product_list(self):
        """ Test for product list """
        add_products([{'name':'A','price':5},
                    {'name':'B','price':10},
                    {'name':'C','price':15}
                    ])
        with self.client:
            response = self.client.get(
                '/product')

            data = json.loads(response.data.decode())
            self.assertEqual(len(data["entries"]),3)
            self.assertEqual(data["entries"][0]["name"],'A')
            self.assertEqual(data["entries"][1]["name"],'B')
            self.assertEqual(data["entries"][2]["name"],'C')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)
