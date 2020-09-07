from project.tests.base import BaseTestCase
from project.tests.helper.createdata import initializewithdata
import json


class TestCartCheckout(BaseTestCase):
    def test_checkout_case_basic(self):
        """ Test for cart checkout """
        initializewithdata(self.client)
        with self.client:
            response = self.client.get(
                '/cart/checkout/1')

            data = json.loads(response.data.decode())
            self.assertEqual(data["final_price"],'39.50')
            self.assertEqual(data["disc_total"],'20.50')
            self.assertEqual(data["cart_total"],'60.00')
            self.assertEqual(data["product_discount"],'0.50')
            self.assertEqual(data["basket_discount"],'20.00')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_checkout_case_discount(self):
        """ Test for cart checkout """
        initializewithdata(self.client, None ,[
                {"p_id":1,"quantity":10}],[],[]
        )
        with self.client:
            response = self.client.get(
                '/cart/checkout/1')

            data = json.loads(response.data.decode())
            self.assertEqual(data["final_price"],'45.12')
            self.assertEqual(data["product_discount"],'2.50')
            self.assertEqual(data["basket_discount"],'2.38')
            self.assertEqual(data["disc_total"],'4.88')
            self.assertEqual(data["cart_total"],'50.00')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_checkout_case_discount_multiples(self):
        """ Test for cart checkout """
        initializewithdata(self.client, None ,[
                {"p_id":1,"quantity":10}],[(1,5,None,3)],[(200,300,10,None)]
        )
        with self.client:
            response = self.client.get(
                '/cart/checkout/1')

            data = json.loads(response.data.decode())
            self.assertEqual(data["final_price"],'44.00')
            self.assertEqual(data["product_discount"],'6.00')
            self.assertEqual(data["basket_discount"],'0')
            self.assertEqual(data["disc_total"],'6.00')
            self.assertEqual(data["cart_total"],'50.00')

            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_checkout_case_discount_basket(self):
        """ Test for cart checkout """
        initializewithdata(self.client, None ,[
                {"p_id":1,"quantity":20}],[(3,5,None,3)],[(50,100,10,None)]
        )
        with self.client:
            response = self.client.get(
                '/cart/checkout/1')

            data = json.loads(response.data.decode())
            self.assertEqual(data["final_price"],'44.00')
            self.assertEqual(data["product_discount"],'6.00')
            self.assertEqual(data["basket_discount"],'0')
            self.assertEqual(data["disc_total"],'6.00')
            self.assertEqual(data["cart_total"],'50.00')

            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)
