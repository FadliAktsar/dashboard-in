import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'b4a0dd67a068148cc0acf448ddf493a4499eebab21224656')
    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set for Flask application.")
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'postgresql://postgres:Duapuluhenam0299@localhost:5432/database_in')
    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("No SQLALCHEMY_DATABASE_URI set for Flask application.")
    
    SQLALCHEMY_TRACK_MODIFICATION = False

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True