import allure
import pytest
from config.base_test import BaseGamesTest
from utils.conversion_data import ConversionData
from utils.assertions import Assertions


@allure.epic("Administration")
@allure.feature("Games")
@pytest.mark.regression
class TestGames(BaseGamesTest):
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
        with allure.step("Получить список всех игр"):
            game = self.api_games.get_all_games()
        with allure.step("Выбрать рандомную игру и в качестве ключевого параметра выбрать часть ее названия игры"):
            extract_part_titles_game = ConversionData.extract_part_of_title_game(game)
            random_part_title = ConversionData.random_choice(extract_part_titles_game)
            query_param = ConversionData.create_query_param(random_part_title)
        with allure.step("Осуществить поиск по ключевому слову"):
            game = self.api_games.get_games_and_search(query_param)
            response = ConversionData.extract_titles(game)
        with allure.step("Проверить, что ответ содержит только игру у которой в заголовке содержится ключевое слово"):
            Assertions.check_word_in_list(random_part_title, response)
