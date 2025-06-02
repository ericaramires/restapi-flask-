from flask import Response
from flask_restful import Resource, reqparse
from mongoengine import NotUniqueError
from .model import UserModel
import re


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


class Users(Resource):
    def get(self):
        users_json = UserModel.objects().to_json()
        return Response(users_json, mimetype="application/json", status=200)

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
        data = _user_parser.parse_args()

        if not self.validate_cpf(data['cpf']):
            return {"message": "CPF invalid"}, 400

        try:
            response = UserModel(**data).save()
            return {"message": "User %s sucessfully created!" %
                    response.id}
        except NotUniqueError:
            return {"message": "CPF already exists in database"}, 400


class User(Resource):
    def get(self, cpf):
        user = UserModel.objects(cpf=cpf).first()
        if user:
            return Response(user.to_json(), mimetype="application/json",
                            status=200)
        else:
            return {"message": "User not found"}, 404


class Home(Resource):
    def get(self):
        return {"message": "Welcome to the API!"}
