from project.server import db
from project.server.models import product

def getproducts():
    return db.session.query(product).order_by(product.p_id).all();
