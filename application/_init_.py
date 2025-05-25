from flask import Flask
from flask_restful import Api



def create_app(config):
    app = Flask(__name__) 
    api = Api(app)
    app.config.from_object(config)
