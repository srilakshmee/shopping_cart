from flask import request
from project.server.restapi.basket import cartbasket
from flask_restful import Resource, marshal_with

class CheckoutApi(Resource):

    def get(self,c_id):
        """Apply discount strategies and calculate discount"""
        basket = cartbasket(c_id)
        basket.checkout()
        return basket.tojson()
