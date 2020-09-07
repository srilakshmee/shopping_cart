from project.server.shopping.product import getproducts
from flask_restful import Resource, marshal_with
from project.server.restapi.serializers import productrows

class ProductApi(Resource):

    def __init__(self):
        pass

    @marshal_with(productrows)
    def get(self):
        """Returns a list of products with price and name"""
        products = getproducts()
        return {"items" : products}
