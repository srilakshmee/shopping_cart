from flask import request
from project.server import db
from project.server.models import cart,cart_item
import json
from project.server.restapi.appexception import CustomException
from project.server.discount.strategy import getdiscountstrategy
from project.server.shopping.cart import getcartdata

class cartbasket(object):

    def __init__(self,c_id):
        self.c_id = c_id
        self.items = []
        self.cart_total = 0
        self.disc_total = 0
        self.discount = {}
        self.final_price = 0

    def checkout(self):
        self.items , self.cart_total = getcartdata(self.c_id)
        disc_list = getdiscountstrategy(self)
        self.final_price = self.cart_total
        for temp_disc in disc_list :
            name , disc = temp_disc.applydiscount()
            self.disc_total += disc
            self.final_price = self.final_price - disc
            self.discount[name] = str(disc)

    def tojson(self):
        d = dict()
        i = []
        for c in self.items:
            i.append({'p_id': c.p_id,'quantity':c.quantity,'cost':str(c.cost)})
        d['items'] = i
        d['cart_total'] = str(self.cart_total)
        d.update(self.discount)
        d['disc_total'] =  str(self.disc_total)
        d['final_price'] = str(self.final_price)
        return d
