import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'postgresql://' + os.path.join(basedir, 'database_in.db')
    SQLALCHEMY_TRACK_MODIFICATION = False