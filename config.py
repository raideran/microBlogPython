import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'QWERTY321.'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                                'mysql://root:root@localhost/japsmcblog'  
                                #IMPORTANT: Run "pip install mysqlclient==1.3.12"
    SQLALCHEMY_TRACK_MODIFICATIONS = False