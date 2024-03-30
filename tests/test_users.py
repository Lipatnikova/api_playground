import allure
import pytest
from config.base_test import BaseUsersTest
from utils.conversion_data import ConversionData


@allure.epic("Administration")
@allure.feature("Users")
class TestUsers(BaseUsersTest):

    @pytest.mark.regression
    @allure.title("Create new user")
    def test_create_user(self):
        user = self.api_users.create_user()
        self.api_users.get_user_by_id(user['uuid'])

    @pytest.mark.regression
    @allure.story("API-1 - Удаление юзера из списка")
    @allure.description("""
    Предусловия:
    1. Авторизоваться в системе через Bearer token.
    2. Отправить POST запрос на эндпоинт /setup для настройки/сброса вашей тестовой среды
    Шаги:
    1. Отправить GET запрос на эндпоинт /users для получения списка пользователей.
    2. Выбрать любого пользователя из списка и взять его uuid.
    3. Отправить DELETE запрос на эндпоинт /users/{uuid} с ранее взятым uuid пользователя в качестве параметра.
    4. Убедиться, что получен ответ со статусом 204.
    5. Подтвердить, что пользователь был удален из списка пользователей, отправив GET запрос на эндпоинт /users.
    6. Проверить, что информация о пользователе не возвращается, отправив GET запрос с uuid пользователя 
    на эндпоинт /user/{uuid}.
    Ожидаемый результат:
    1. Код статуса ответа после удаления — 204.
    2. Пользователь не отображается в списке пользователей.
    3. Информация о пользователе не отображается при запросе по его uuid.
                        """)
    def test_delete_user_by_uuid(self):
        with allure.step("Получить список пользователей"):
            users_before = self.api_users.get_all_users()
            extract_uuids_all_users = ConversionData.extract_uuids(users_before)
        with allure.step("Выбрать рандомного пользователя по ID"):
            random_id = ConversionData.random_choice(extract_uuids_all_users)
        with allure.step("Удалить выбранного пользователя"):
            self.api_users.del_user_by_uuid(random_id)
        with allure.step("Получить список пользователей"):
            users_after = self.api_users.get_all_users()
        with allure.step("Проверить, что пользователь с выбранным ID удален из списка пользователей"):
            assert (random_id in users_after) is False, \
                'The user with the selected ID was not deleted'
        with allure.step("Проверить, что информация о пользователе не возвращается"):
            self.api_users.re_del_user_by_uuid(random_id)
