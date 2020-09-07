class discount(object):

    def __init__(self,cart):
        """ Fetch strategy for the passed items from db"""
        self.cart = cart

    def applydiscount(self):
        """ apply multiple discount strategy """
        return self.fetch_dicount_fromdatasource()

    def fetch_dicount_fromdatasource():
        pass
