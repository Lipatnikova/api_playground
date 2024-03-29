import allure

from services.users.endpoints import Endpoints
from services.users.payloads import Payloads
from config.headers import Headers
from services.users.models.user_model import UserModel, UsersModel
from utils.http_handler import HTTPHandler


class UsersAPI(HTTPHandler):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    def create_user(self):
        with allure.step("Create user"):
            response = HTTPHandler.post(
                url=self.endpoints.create_user,
                headers=self.headers.basic,
                json_data=self.payloads.create_user,
                model=UserModel
            )
            return response

    def get_user_by_id(self, uuid):
        with allure.step("Get users by ID"):
            response = HTTPHandler.get(
                url=self.endpoints.get_user_by_id(uuid),
                headers=self.headers.basic,
                model=UserModel
            )
            return response

    def get_all_users(self):
        with allure.step("Get all users"):
            response = HTTPHandler.get(
                url=self.endpoints.get_all_users,
                headers=self.headers.basic,
                model=UsersModel
            )
            return response

    def del_user_by_uuid(self, uuid):
        with allure.step("Delete user by ID"):
            response = HTTPHandler.delete(
                url=self.endpoints.get_user_by_id(uuid),
                headers=self.headers.basic,
            )
            return response

    def re_del_user_by_uuid(self, uuid):
        with allure.step("Re-delete user by ID"):
            response = HTTPHandler.double_delete(
                url=self.endpoints.get_user_by_id(uuid),
                headers=self.headers.basic,
            )
            return response
