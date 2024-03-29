import allure
import pytest
from config.base_test import BaseTest
from utils.conversion_data import ConversionData


@allure.epic("Administration")
@allure.feature("Users")
class TestUsers(BaseTest):

    @pytest.mark.regression
    @allure.title("Create new user")
    def test_create_user(self):
        user = self.api_users.create_user()
        self.api_users.get_user_by_id(user['uuid'])

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

    @pytest.mark.skip
    @allure.story("API-2 - Поиск игр по ключевым словам или фразе")
    @allure.description("""
        Предусловия:
        1. Авторизоваться в системе через Bearer token.
        2. Отправить POST запрос на эндпоинт /setup для настройки/сброса вашей тестовой среды
        Шаги:
        1. Отправить GET запрос на эндпоинт /games для получения списка всех игр.
        2. Выбрать любую игру и в качестве ключевого слова скопируйте часть её названия.
        3. Подготовить query-параметр для поискового запроса с использованием ранее скопированной части названия игры.
        4. Отправить GET запрос на эндпоинт /games/search с ранее подготовленным query-параметром.
        5. Проверить, что возвращается статус-код ответа - 200.
        6. Проверить, что поля ответа соответствуют полям из документации и содержат данные только с запрашиваемым 
        ключевым словом или фразой.
        Ожидаемый результат:
        1. Статус-код ответа - 200.
        2. Функция поиска возвращает результаты, основанные только на предоставленном ключевом слове или фразе.
        3. Система корректно обрабатывает пустые или невалидные поисковые запросы.
        4. Результаты поиска правильно отформатированы и содержат соответствующую информацию о запрашиваемых играх.
    
            """)
    def test_search_games_by_keywords_or_phrase(self):
        pass
