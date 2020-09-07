# project/server/config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))
mysql_conn = 'mysql://root:root123@'+os.environ.get("APP_DB_HOST","localhost")+'/'


class BaseConfig:
    """Base configuration."""
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    DB_NAME = 'shopping_cart'
    SQLALCHEMY_DATABASE_URI = mysql_conn + DB_NAME


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    DB_NAME = 'shopping_cart_test'
    SQLALCHEMY_DATABASE_URI = mysql_conn + DB_NAME


class ProductionConfig(BaseConfig):
    """Production configuration."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql_conn:///example'
