from flask_restful import Resource
from flask import make_response,render_template

class HomeApi(Resource):
    def get(self):
        response = make_response(render_template('index.html'))
        return response
