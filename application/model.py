from mongoengine import Document, StringField, EmailField, DateField


class UserModel(Document):
    cpf = StringField(required=True, unique=True)
    name = StringField(required=True)
    last_name = StringField(required=True)
    email = EmailField(required=True)
    birth_date = DateField(required=True)
