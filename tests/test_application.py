import pytest
from application import create_app
from application.model import UserModel
import json

class TestApplication():
    @pytest.fixture
    def client(self):
        app = create_app('config.MockConfig')
        with app.app_context():
            UserModel.objects().delete()
        return app.test_client()

    @pytest.fixture
    def valid_user_data(self):
        return {
            'name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'cpf': '641.396.500-28',
            'birth_date': '1990-01-01'
        }

    @pytest.fixture
    def non_existent_user_cpf(self):
        return "123.456.789-99"

    def test_get_users(self, client):
        response = client.get('/users')
        assert response.status_code == 200
        assert response.get_data(as_text=True) == "[]"

    def test_post_user(self, client, valid_user_data):
        with client.application.app_context():
            UserModel.objects(cpf=valid_user_data['cpf']).delete()

        response = client.post('/users', json=valid_user_data)
        assert response.status_code == 200
        assert b"sucessfully created" in response.data

        with client.application.app_context():
           assert UserModel.objects(cpf=valid_user_data['cpf']).count() == 1
        with client.application.app_context():
            UserModel.objects(cpf=valid_user_data['cpf']).delete()

    def test_get_specific_user(self, client, valid_user_data, non_existent_user_cpf):
        with client.application.app_context():
            UserModel.objects(cpf=valid_user_data['cpf']).delete()

        create_response = client.post('/users', json=valid_user_data)
        assert create_response.status_code == 200

        get_response_existing = client.get(f'/user/{valid_user_data["cpf"]}')
        assert get_response_existing.status_code == 200

        user_data = json.loads(get_response_existing.data)
        assert user_data['name'] == valid_user_data['name']
        assert user_data['last_name'] == valid_user_data['last_name']
        assert user_data['email'] == valid_user_data['email']
        assert user_data['cpf'] == valid_user_data['cpf']
        assert isinstance(user_data['birth_date']['$date'], (int, float))

        get_response_non_existent = client.get(f'/user/{non_existent_user_cpf}')
        assert get_response_non_existent.status_code == 404
        response_data_non_existent = json.loads(get_response_non_existent.data)
        assert "User not found" in response_data_non_existent["message"]

        with client.application.app_context():
            UserModel.objects(cpf=valid_user_data['cpf']).delete()