from flask_restful import Resource, reqparse
from flask import request
import json
from project.server.restapi.appexception import CustomException
from project.server.shopping.cart import createcart,addtocart,getcartdata

class CreateCartApi(Resource):
    def post(self):
        c_id = createcart()
        item_list = request.get_json()
        addtocart(item_list , c_id)
        return { "cartid" : c_id }

class CartApi(Resource):

    def get(self,c_id):
        """"Returns the list of cart items"""
        items , cart_total = getcartdata(c_id)
        return self.tojson( items , cart_total)

    def post(self,c_id):
        """ Adds the product and quantity to the cart"""
        item_list = request.get_json()
        addtocart(item_list , c_id)
        return 'Added successfully.', 201

    def tojson(self,items,cart_total):
        d = dict()
        i = []
        for c in items:
            i.append({'p_id': c.p_id,'quantity':c.quantity,'cost':str(c.cost)})
        d['items'] = i
        d['cart_total'] = str(cart_total)
        return d
