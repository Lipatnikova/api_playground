from pydantic import ValidationError
from faker import Faker

from services.users.models.user_model import PayloadCreateUser

fake = Faker()


class Payloads:

    @staticmethod
    def generate_fake_user():
        user_data = {
            "email": fake.email(),
            "password": fake.password(length=10),
            "name": fake.first_name(),
            "nickname": fake.user_name()
        }
        return PayloadCreateUser(**user_data).model_dump()

    try:
        fake_user = generate_fake_user()
    except ValidationError as e:
        print(e)
