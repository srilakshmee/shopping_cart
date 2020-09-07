from project.server import db
from project.server.models import cart,cart_item,product
from project.server.restapi.appexception import CustomException


class cartitem(object):
    def __init__(self,p_id,q,c):
        self.p_id = p_id
        self.quantity = q
        self.cost = c

def createcart():
    c = cart(tot_price=0,tot_disc=0)
    db.session.add(c)
    db.session.flush()
    db.session.commit();
    return str(c.c_id)

def getprice(data):
    p = [x['p_id'] for x in data ]
    res = db.session.query(product).filter(product.p_id.in_(p)).all()
    if not res:
        raise CustomException(
            'Invalid p_id.Product not found in the database')
    pricedict = { a.p_id : float(a.price)  for a in res}
    return pricedict

def addtocart(item_list,c_id):
    try:
        data = item_list["items"]
        tot_price = 0
        ca = db.session.query(cart).filter(cart.c_id == c_id).first()
        if not ca:
            raise CustomException(
                'Invalid Cartid '+c_id)

        price_list = getprice(data)

        for i in range(0,len(data)):
            #todo check if cart id exists and pid exists in the tables
            q = data[i]['quantity']
            p = data[i]['p_id']
            for ci in ca.cart_data:
                if ci.p_id ==  data[i]['p_id']:
                    ci.quantity = ci.quantity + q
                    ci.cost =  (ci.quantity) * price_list[data[i]['p_id']]
                    pr = ci.cost
                    break
            else:
                pr =  q * price_list[data[i]['p_id']]
                db.session.add(cart_item(c_id=c_id,p_id=p,quantity=q,
                cost = pr))
            tot_price += pr
        ca.tot_price = tot_price
    except KeyError:
        db.session.rollback()
        raise CustomException(
            'Input should be in json format-{items: [{p_id:1,quantity:2},{p_id:2,quantity:3}]}')
    db.session.commit()

def getcartdata(c_id):
    c_items = []
    tot_price = 0
    row = db.session.query(cart).filter(cart.c_id==c_id).first()
    if row:
        tot_price = row.tot_price
        for ci in row.cart_data:
            c_items.append(cartitem(ci.p_id,ci.quantity,ci.cost))
    return c_items, tot_price
