from project.server.restapi.product import ProductApi
from project.server.restapi.cart import CartApi,CreateCartApi
from project.server.restapi.checkout import CheckoutApi

def initialize_routes(api):
    api.add_resource(ProductApi , '/product')
    api.add_resource(CartApi, '/cart/<c_id>')
    api.add_resource(CreateCartApi, '/cart')
    api.add_resource(CheckoutApi, '/cart/checkout/<c_id>')
