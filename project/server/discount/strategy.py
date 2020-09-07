from project.server.discount.discount_multiples import disc_multiples
from project.server.discount.discount_basket_amount import disc_basket_amount

def getdiscountstrategy(cart):
    strategy = [disc_multiples(cart),disc_basket_amount(cart)]
    return strategy
