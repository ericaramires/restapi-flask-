from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from flask_mongoengine import MongoEngine
import re
from config import DevConfig

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = DevConfig.MONGODB_SETTINGS

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('name',
                        type=str,
                        required=True,
                        help='This field cannot be blank')
_user_parser.add_argument('last_name',
                        type=str,
                        required=True,
                        help='This field cannot be blank')
_user_parser.add_argument('cpf',
                        type=str,
                        required=True,
                        help='This field cannot be blank')
_user_parser.add_argument('email',
                        type=str,
                        required=True,
                        help='This field cannot be blank')
_user_parser.add_argument('birth_date',
                        type=str,
                        required=True,
                        help='This field cannot be blank')

api = Api(app)
db = MongoEngine(app)


class UserModel(db.Document):
    cpf = db.StringField(required=True, unique=True)
    name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.EmailField(required=True)
    birth_date = db.DateField(required=True)


class Users(Resource):
    def get(self):
        try:
            users = UserModel.objects.all()
            return jsonify({
                "message": "Lista de usuários",
                "data": [{
                    "cpf": user.cpf,
                    "name": user.name,
                    "last_name": user.last_name,
                    "email": user.email,
                    "birth_date": str(user.birth_date)
                } for user in users]
            })
        except Exception as e:
            return {"message": f"Error: {str(e)}"}, 500

    def validate_cpf(self, cpf):
        """
        Validates a CPF number.
        Returns True if the CPF is valid, False otherwise.
        """
        cpf = str(cpf)  # Ensures CPF is a string

        # Checks if the mask is correct (format XXX.XXX.XXX-XX)
        if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
            return False

        # Removes dots and dashes for validation
        cpf_digits = re.sub(r'[^0-9]', '', cpf)

        # Checks if it has 11 digits
        if len(cpf_digits) != 11:
            return False

        # Checks if all digits are the same (e.g., 111.111.111-11)
        if len(set(cpf_digits)) == 1:
            return False

        # Validation of the two verifier digits
        def calculate_verifier_digit(cpf_part, factor):
            total = 0
            for digit in cpf_part:
                total += int(digit) * factor
                factor -= 1
            remainder = total % 11
            return 0 if remainder < 2 else 11 - remainder

        # First verifier digit
        first_part = cpf_digits[:9]
        first_verifier = calculate_verifier_digit(first_part, 10)
        if int(cpf_digits[9]) != first_verifier:
            return False

        # Second verifier digit
        second_part = cpf_digits[:10]
        second_verifier = calculate_verifier_digit(second_part, 11)
        if int(cpf_digits[10]) != second_verifier:
            return False

        return True

    def post(self):
        try:
            data = _user_parser.parse_args()

            if not self.validate_cpf(data['cpf']):
                return {"message": "CPF invalid"}, 400

            # Check if user already exists
            if UserModel.objects(cpf=data['cpf']).first():
                return {"message": "User with this CPF already exists"}, 400

            user = UserModel(**data).save()
            return {
                "message": f"User {user.name} successfully created!",
                "data": {
                    "cpf": user.cpf,
                    "name": user.name,
                    "last_name": user.last_name,
                    "email": user.email,
                    "birth_date": str(user.birth_date)
                }
            }, 201
        except Exception as e:
            return {"message": f"Error: {str(e)}"}, 500


class User(Resource):
    def get(self, cpf):
        try:
            user = UserModel.objects(cpf=cpf).first()
            if not user:
                return {"message": "User not found"}, 404
            return {
                "message": "User found",
                "data": {
                    "cpf": user.cpf,
                    "name": user.name,
                    "last_name": user.last_name,
                    "email": user.email,
                    "birth_date": str(user.birth_date)
                }
            }
        except Exception as e:
            return {"message": f"Error: {str(e)}"}, 500


class Home(Resource):
    def get(self):
        return {"message": "Bem-vindo à API!"}


api.add_resource(Users, '/users')
api.add_resource(User, '/user/<string:cpf>')
api.add_resource(Home, '/')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001) 