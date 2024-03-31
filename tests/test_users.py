import allure
import pytest
from config.base_test import BaseUsersTest
from services.users.payloads import Payloads
from utils.assertions import Assertions
from utils.conversion_data import ConversionData


@allure.epic("Administration")
@allure.feature("Users")
class TestUsers(BaseUsersTest):

    @pytest.mark.regression
    @allure.title("Удаление юзера из списка")
    @allure.testcase("API-1")
    @allure.description("""
    Цель: Протестировать функциональность, которая позволяет 
    администраторам удалять существующих пользователей.
    Предусловия:
    1. Создать тестовую среду.
    Шаги:
    1. Получить список пользователей.
    2. Выбрать рандомного пользователя по ID.
    3. Удалить выбранного пользователя.
    4. Получить список пользователей.
    5. Проверить, что пользователь с выбранным ID удален из списка пользователей.
    6. Проверить, что информация о пользователе не возвращается. 
    при попытке удалить повторно пользователя. 
    Ожидаемый результат:
    1. Пользователь успешно удален. """)
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
        with allure.step("Проверить, что информация о пользователе не возвращается "
                         "при попытке удалить повторно пользователя"):
            self.api_users.re_del_user_by_uuid(random_id)

    @pytest.mark.regression
    @allure.story("Создание пользователя в системе")
    @allure.testcase("API-3")
    @allure.description("""
    Цель задачи:
    Протестировать функциональность, которая позволяет администраторам 
    создавать новых пользователей в системе.
    Предусловия:
    1. Создать тестовую среду.
    Шаги:
    1. Создать пользователя.
    2. Проверить, что новый пользователь был создан и существует в списке пользователей.
    3. Проверить, что информация о пользователе соответствует информации при его создании.
    Ожидаемый результат:
    1. Созданный пользователь отображается в списке пользователей.
    2. Информация у добавленного пользователя по его uuid соответствует 
    данным введенным при его создании .""")
    @allure.title("Create new user")
    def test_create_user(self):
        with allure.step("Создать пользователя"):
            user = self.api_users.create_user()
        with allure.step("Проверить, что новый пользователь был создан и существует в списке пользователей"):
            all_users = self.api_users.get_all_users()
            uuids_users = ConversionData.extract_uuids(all_users)
            Assertions.check_word_in_list(str(user['uuid']), uuids_users)
        with allure.step("Проверить, что информация о пользователе соответствует информации при его создании"):
            data_user = self.api_users.get_user_by_id(user['uuid'])
            data_user = ConversionData.remove_uuid(data_user)
            # assert data_user ==

