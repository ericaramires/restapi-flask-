from flask import Flask
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine

app = Flask(__name__)
api = Api(app)
db = MongoEngine(app)

app.config['MONGODB_SETTINGS'] = {
    'db': 'users',
    'host': 'mongodb',
    'port': 27017,
    "user": 'admin',
    "password": 'admin'
}

class UserModel(db.Document):
    cpf = db.StringField(required=True, unique=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.EmailField(required=True)
    birth_date = db.DateField(required=True) 
    

class Users(Resource):
    def get(self):
        return {"message": "Lista de usuários"}

class User(Resource):
    def post(self):
        return {"message": "Usuário criado com sucesso"}

    def get(self, cpf):
        return {"message": f"CPF {cpf}"}

class Home(Resource):
    def get(self):
        return {"message": "Bem-vindo à API!"}

api.add_resource(Users, '/users')
api.add_resource(User, '/user/<string:cpf>')
api.add_resource(Home, '/')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
