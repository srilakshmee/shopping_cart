from project.server.discount.basediscount import discount
from project.server.models import discount_cart_amount
from project.server import db

class disc_basket_amount(discount):

    def fetch_dicount_fromdatasource(self):
        disc = 0
        print(self.cart.final_price)
        d = db.session.query(discount_cart_amount).filter(
            (self.cart.final_price >= discount_cart_amount.min_amount)  &
            (self.cart.final_price <= discount_cart_amount.max_amount)  ).first()
        if d :
            disc = round(self.cart.final_price * (d.disc_perc / 100) if d.disc_perc else d.disc_amount ,2)
        return "basket_discount", disc
