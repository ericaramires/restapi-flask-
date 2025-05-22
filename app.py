from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

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
