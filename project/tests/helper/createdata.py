from project.server import db
from project.server.models import product,discount_multiples,discount_cart_amount
import json

def add_products(prods):
    for i in prods:
        db.session.add(product(name=i['name'],price=i['price']))
    db.session.commit()

def add_discount_amount(min,max,perc=None,amount=None):
    db.session.add(discount_cart_amount(
    min_amount=min,max_amount=max,
    disc_perc = perc,disc_amount =amount)
    )
    db.session.commit()

def add_discount_multiples(p_id,quantity,perc=None,amount=None):
    db.session.add(discount_multiples(
    p_id=p_id,quantity=quantity,
    disc_perc = perc,disc_amount =amount)
    )
    db.session.commit()

def initializewithdata(client,prod=None,cartitems=None,dm=None,da=None):
    if not prod :
        prods = [{'name':'A','price':5},
                    {'name':'B','price':10},
                    {'name':'C','price':15}
                    ]
    if not cartitems:
        cartitems = [
                {"p_id":1,"quantity":2},
                {"p_id":2,"quantity":5}
                ]
    add_products(prods)
    with client:
        response = client.post(
            '/cart',
            data=json.dumps({"items":cartitems}),
            content_type='application/json'
        )
        data = json.loads(response.data.decode())
    if not dm:
        dm = [(1,2,5,0)]
    [add_discount_multiples(t[0],t[1],t[2],t[3]) for t in dm]
    if not da:
        da = [(40,50,5,None),(51,70,None,20)]
    [add_discount_amount(t[0],t[1],t[2],t[3]) for t in da]
