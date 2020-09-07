# project/server/__init__.py
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
import sqlalchemy

app = Flask(__name__ ,static_folder='../client/src/build/static',
               template_folder='../client/src/build')

app_settings = os.getenv(
    'APP_SETTINGS',
    'project.server.config.DevelopmentConfig'
)
from flask_cors import CORS
CORS(app)

app.config.from_object(app_settings)
temp = app.config['SQLALCHEMY_DATABASE_URI']
engine = sqlalchemy.create_engine(temp[0:temp.rfind("/")])  # connect to server
engine.execute("CREATE SCHEMA IF NOT EXISTS " +
               app.config['DB_NAME']+";")  # create db
engine.execute("USE "+app.config['DB_NAME']+";")  # select new db

db = SQLAlchemy(app)

api = Api(app)


from project.server.routes import initialize_routes
initialize_routes(api)


from project.server.restapi.appexception import CustomException
@app.errorhandler(CustomException)
def handle_custom_exception(error):
    return {'message': error.message}, error.status_code
