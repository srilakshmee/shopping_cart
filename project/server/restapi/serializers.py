from flask_restful import fields


product = {"p_id": fields.Integer, "price": fields.Float,
           "name": fields.String }

productrows = {"entries": fields.List(fields.Nested(product),attribute="items")
                                   }
