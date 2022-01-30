class Config(object):
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SERVER_NAME = 'localhost:10001'

    PWD_HASH_SALT = '249y823r9v8238r9u'.encode("utf-8")
    PWD_HASH_ITERATIONS = 100_000
