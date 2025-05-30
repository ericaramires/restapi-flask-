import os


class DevConfig:
    MONGODB_SETTINGS = {
        'db': os.getenv('MONGODB_DB', 'users'),
        'host': os.getenv('MONGODB_HOST', 'mongodb'),
        'port': int(os.getenv('MONGODB_PORT', 27017)),
        'username': os.getenv('MONGODB_USERNAME', 'admin'),
        'password': os.getenv('MONGODB_PASSWORD', 'admin')
    }
    MONGODB_DB = os.getenv('MONGODB_DB', 'users')
    MONGODB_HOST = os.getenv('MONGODB_HOST', 'mongodb')
    MONGODB_PORT = int(os.getenv('MONGODB_PORT', 27017))
    MONGODB_USERNAME = os.getenv('MONGODB_USERNAME', 'admin')
    MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD', 'admin')

class ProdConfig:
    MONGODB_SETTINGS = {
        'host': os.getenv('MONGODB_URI', 'mongodb://localhost:27017/users')
    }
    
    MONGODB_DB = os.getenv('MONGODB_DB', 'users')
    MONGODB_HOST = os.getenv('MONGODB_HOST', 'localhost')
    MONGODB_PORT = int(os.getenv('MONGODB_PORT', 27017))
    MONGODB_USERNAME = os.getenv('MONGODB_USERNAME', 'admin')
    MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD', 'admin')

class MockConfig:
    MONGODB_DB = 'users_test'
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27018
    MONGODB_USERNAME = 'admin'
    MONGODB_PASSWORD = 'admin'

    MONGODB_SETTINGS = {
        'db': MONGODB_DB,
        'host': MONGODB_HOST,
        'port': MONGODB_PORT,
        'username': MONGODB_USERNAME,
        'password': MONGODB_PASSWORD
    }


class Config:
    MONGODB_DB = 'restapi_flask'
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27017
