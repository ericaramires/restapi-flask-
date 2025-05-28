import pytest
from application import create_app
from application.model import UserModel


class TestApplication():
    @pytest.fixture
    def client(self):
        app = create_app('config.MockConfig')
        with app.app_context():
            UserModel.objects().delete()
        return app.test_client()

    @pytest.fixture
    def valid_user(self):
        return {
            'name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'cpf': '641.396.500-28',
            'birth_date': '1990-01-01'
        }

    def test_get_users(self, client):
        response = client.get('/users')
        assert response.status_code == 200

    def test_post_user(self, client, valid_user):
        with client.application.app_context():
            UserModel.objects(cpf=valid_user['cpf']).delete()

        response = client.post('/users', json=valid_user)

        assert response.status_code == 200
        assert b"sucessfully" in response.data

        with client.application.app_context():
            UserModel.objects(cpf=valid_user['cpf']).delete()
