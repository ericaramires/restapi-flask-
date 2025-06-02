import os


class DevConfig:
    """
    Development configuration - Uses environment variables
    All sensitive data must be provided via .env file
    """
    MONGODB_SETTINGS = {
        'db': os.getenv('MONGODB_DB', 'users'),
        'host': os.getenv('MONGODB_HOST', 'mongodb'),
        'port': int(os.getenv('MONGODB_PORT', 27017)),
        'username': os.getenv('MONGODB_USERNAME'),
        'password': os.getenv('MONGODB_PASSWORD')
    }
    MONGODB_DB = os.getenv('MONGODB_DB', 'users')
    MONGODB_HOST = os.getenv('MONGODB_HOST', 'mongodb')
    MONGODB_PORT = int(os.getenv('MONGODB_PORT', 27017))
    MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
    MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')


class ProdConfig:
    """
    Production configuration - Uses environment variables
    All sensitive data must be provided via .env file
    """
    MONGODB_SETTINGS = {
        'host': os.getenv('MONGODB_URI', 'mongodb://localhost:27017/users')
    }
    
    MONGODB_DB = os.getenv('MONGODB_DB', 'users')
    MONGODB_HOST = os.getenv('MONGODB_HOST', 'localhost')
    MONGODB_PORT = int(os.getenv('MONGODB_PORT', 27017))
    MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
    MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
    SECRET_KEY = os.getenv('SECRET_KEY')


class MockConfig:
    """
    Testing configuration - Uses safe test credentials
    Only for automated testing - not for production
    """
    MONGODB_DB = 'users_test'
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27018
    MONGODB_USERNAME = os.getenv('MONGODB_TEST_USERNAME', 'test_user')
    MONGODB_PASSWORD = os.getenv('MONGODB_TEST_PASSWORD', 'test_pass')

    MONGODB_SETTINGS = {
        'db': MONGODB_DB,
        'host': MONGODB_HOST,
        'port': MONGODB_PORT,
        'username': MONGODB_USERNAME,
        'password': MONGODB_PASSWORD
    }


class Config:
    """
    Base configuration class
    """
    MONGODB_DB = 'restapi_flask'
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27017
    SECRET_KEY = os.getenv('SECRET_KEY')
