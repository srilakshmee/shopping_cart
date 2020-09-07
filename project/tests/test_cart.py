# project/tests/test_auth.py

from project.tests.base import BaseTestCase
from project.tests.helper.createdata import add_products,initializewithdata
import json


class TestCart(BaseTestCase):
    def test_create_cart(self):
        """ Test for create cart """
        add_products([{'name':'A','price':5},
                    {'name':'B','price':10},
                    {'name':'C','price':15}
                    ])
        with self.client:
            response = self.client.post(
                '/cart',
                data=json.dumps({"items":[
                    {"p_id":1,"quantity":2},
                    {"p_id":2,"quantity":5},]
                }),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(data["cartid"],'1')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_addtocart_invalidpid(self):
        with self.client:
            response = self.client.post(
                '/cart',
                data=json.dumps({"items":[{"p_id":1,"quantity":2}]
                }),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(data["message"],'Invalid p_id.Product not found in the database')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

    def test_addtocart(self):
        add_products([{'name':'A','price':5},
                    {'name':'B','price':10},
                    {'name':'C','price':15}
                    ])
        with self.client:
            response = self.client.post(
                '/cart',
                data=json.dumps({"items":[
                            {"p_id":1,"quantity":2}]
                            }),
                content_type='application/json'
              )
            data = json.loads(response.data.decode())
            self.assertTrue(data["cartid"],'1')
            response = self.client.post(
                '/cart/1',
                data=json.dumps({"items":[
                    {"p_id":2,"quantity":5}]
                }),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(data,'Added successfully.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_getcart(self):
        """ Test for get items from cart """
        initializewithdata(self.client)
        with self.client:
            response = self.client.get(
                '/cart/1')

            data = json.loads(response.data.decode())
            self.assertEqual(len(data["items"]),2)
            self.assertEqual(data["cart_total"],'60.00')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_addtocart_invalidcartod(self):
        add_products([{'name':'A','price':5},
                    {'name':'B','price':10},
                    {'name':'C','price':15}
                    ])
        with self.client:
            response = self.client.post(
                '/cart',
                data=json.dumps({"items":[
                            {"p_id":1,"quantity":2}]
                            }),
                content_type='application/json'
              )
            data = json.loads(response.data.decode())
            self.assertTrue(data["cartid"],'1')
            response = self.client.post(
                '/cart/2',
                data=json.dumps({"items":[
                    {"p_id":2,"quantity":5}]
                }),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(data['message'],'Invalid Cartid 2')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)
