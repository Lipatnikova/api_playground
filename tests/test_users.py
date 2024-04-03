import allure
import pytest
from config.base_test import BaseUsersTest


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
            extract_uuids_all_users = self.conversion_data.extract_uuids(users_before)

        with allure.step("Выбрать рандомного пользователя по ID"):
            random_id = self.conversion_data.random_choice(extract_uuids_all_users)

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
    @allure.title("Создание пользователя в системе")
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
    данным введенным при его создании .
    Постусловия:
    1. Удалить созданного пользователя. """)
    def test_create_user(self):
        with allure.step("Создать пользователя"):
            payload = self.api_users.payloads.generate_fake_user()
            user = self.api_users.create_user(payload)

        with allure.step("Проверить, что новый пользователь был создан и существует в списке пользователей"):
            all_users = self.api_users.get_all_users()
            uuids_users = self.conversion_data.extract_uuids(all_users)
            self.assertions.check_word_in_list(str(user['uuid']), uuids_users)

        with allure.step("Проверить, что информация о пользователе соответствует информации при его создании"):
            data_user = self.api_users.get_user_by_id(user['uuid'])
            data_user = self.conversion_data.remove_uuid(data_user)
            self.conversion_data.remove_password(payload)
            assert data_user == payload, \
                "Data received in the response does not match the data entered when creating the user"

    @pytest.mark.regression
    @allure.title("Проверить невозможность обновления пользователя уже занятыми данными")
    @allure.testcase("API-4")
    @allure.description("""
        Цель задачи:
        Проверить невозможность обновления юзера уже занятыми данными.
        Предусловия:
        1. Создать тестовую среду.
        Шаги:
        1. Получить список пользователей.
        2. Сформировать тело запроса для обновления пользователя.
        3. Попытаться обновить данные пользователя данными уже занятыми другим пользователем.
        4. Проверить, что получен ответ со статус-кодом 409 и сообщением User email/nickname already taken 
        Ожидаемый результат:
        1. Данные пользователя необновлены.
        2. Статус-код ответа - 409.
        3. В ответе пристутсвует сообщение User ____ already exists/taken . """)
    def test_сheck_whether_it_is_impossible_to_update_a_user_with_data_different_user(self):
        with allure.step("Получить список пользователей"):
            users = self.api_users.get_all_users()
            extract_uuids_all_users = self.conversion_data.extract_uuids(users)

        with allure.step("Сформировать тело запроса для обновления пользователя"):
            random_id_1 = self.conversion_data.random_choice(extract_uuids_all_users)
            user_1 = self.api_users.get_user_by_id(random_id_1)
            data_for_update = self.conversion_data.random_key_nickname_or_email(user_1)
            users = self.api_users.get_all_users()
            extract_uuids_all_users = self.conversion_data.extract_uuids(users)
            random_id_2 = self.conversion_data.random_choice(extract_uuids_all_users)

        with allure.step("Попытаться обновить данные пользователя данными уже занятыми другим пользователем"):
            user_2_before = self.api_users.get_user_by_id(random_id_2)
            if random_id_1 == random_id_2:
                random_id_2 = self.conversion_data.random_choice(extract_uuids_all_users)
            resp = self.api_users.update_user_by_uuid(random_id_2, data_for_update)
            user_2_after = self.api_users.get_user_by_id(random_id_2)

        with allure.step("Проверить, что получен ответ со статус-кодом 409 и "
                         "сообщением User email/nickname already taken "):
            assert user_2_after == user_2_before, "User information has been updated"
            assert ("User" in resp["message"]) and ("already exists" in resp["message"]), \
                "The response from the server does not contain " \
                "the expected message 'User ____ already exists "
