from project.server.discount.basediscount import discount
from project.server.models import discount_multiples
from project.server import db

class discount_item(object):

    def __init__(self,p_id,q,p,a):
        self.p_id = p_id
        self.quantity = q
        self.disc_perc = p
        self.disc_amount = a

class disc_multiples(discount):

    def __init__(self,cart):
        """ Fetch strategy for the passed items from db"""
        self.cartitems = cart.items
        self.disc_data = dict()

    def applydiscount(self):
        """ apply multiple discount strategy """
        discount.applydiscount(self)
        disc_amount = 0

        for cart_item in self.cartitems:
            disc_amount += self.getdiscountfor( cart_item  )
        return "product_discount" , disc_amount

    def fetch_dicount_fromdatasource(self):
        pids = []
        for t in self.cartitems:
            pids.append(t.p_id)

        temp = db.session.query(discount_multiples).filter(
            discount_multiples.p_id.in_(pids)).order_by(discount_multiples.p_id,
            discount_multiples.quantity).all()
        for r in temp :
            try:
                l = self.disc_data[r.p_id]
                l.append(discount_item(r.p_id,r.quantity,
                r.disc_perc,r.disc_amount) )
            except KeyError:
                self.disc_data[r.p_id] = [discount_item(r.p_id,
                r.quantity,r.disc_perc,r.disc_amount)]

    def getdiscountfor(self,cart_item):
        disc = 0
        try:
            temp = self.disc_data[cart_item.p_id]
            d = None
            for di in temp:
                if  cart_item.quantity >= di.quantity :
                    d = di
                else:
                    break
            if d:
                #Assuming disc % even when the cart quantity is > disc multiple
                disc = round(cart_item.cost * (d.disc_perc / 100) if d.disc_perc else d.disc_amount * (cart_item.quantity//d.quantity) ,2)

        except KeyError:
            disc = 0

        return disc
