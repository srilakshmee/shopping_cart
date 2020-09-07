from project.server import db
from sqlalchemy.orm import relationship

class product(db.Model):
    """ Model for storing product"""
    __tablename__ = "products"

    p_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), nullable=False)
    price = db.Column(db.Numeric(18,2), nullable=False)

class cart(db.Model):
    """ Model for cart details"""
    __tablename__ = "cart"

    c_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tot_price = db.Column(db.Numeric(18,2), nullable=False)
    tot_disc = db.Column(db.Numeric(18, 2), nullable=False)
    cart_data = relationship("cart_item", cascade="delete")

class cart_item(db.Model):
    """Model for storing cart items"""
    __tablename__ = "cart_item"

    ci_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    c_id = db.Column(db.Integer, db.ForeignKey(cart.c_id))
    p_id = db.Column(db.Integer, db.ForeignKey(product.p_id))
    quantity = db.Column(db.Integer,nullable=False)
    cost = db.Column(db.Numeric(18,2), nullable=False)
    __table_args__ = {'extend_existing': True}

class discount_multiples(db.Model):
    """Model for storing discount multiples"""
    __tablename__ = "discount_multiples"

    dm_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    p_id = db.Column(db.Integer, db.ForeignKey(product.p_id))
    quantity = db.Column(db.Integer,nullable=False)
    disc_perc = db.Column(db.Numeric(10,2))
    disc_amount = db.Column(db.Numeric(18,2))

class discount_cart_amount(db.Model):
    """Model for storing discount based on the range of total amount"""
    __tablename__ = "discount_cart_amount"

    dm_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    min_amount = db.Column(db.Numeric(10,2),nullable=False)
    max_amount = db.Column(db.Numeric(10,2),nullable=False)
    disc_perc = db.Column(db.Numeric(10,2))
    disc_amount = db.Column(db.Numeric(18,2))
