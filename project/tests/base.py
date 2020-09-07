from flask_testing import TestCase

from project.server import app, db
import sqlalchemy


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        app.config.from_object('project.server.config.TestingConfig')
        temp = app.config['SQLALCHEMY_DATABASE_URI']
        engine = sqlalchemy.create_engine(temp[0:temp.rfind("/")])
        # connect to server
        engine.execute("CREATE SCHEMA IF NOT EXISTS " +
                       app.config['DB_NAME']+";")  # create db
        engine.execute("USE "+app.config['DB_NAME']+";")  # select new db
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
