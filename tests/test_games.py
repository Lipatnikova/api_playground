import allure
import pytest
from config.base_test import BaseGamesTest


@allure.epic("Administration")
@allure.feature("Games")
@pytest.mark.regression
class TestGames(BaseGamesTest):
    @pytest.mark.skip
    @allure.title("Поиск игр по ключевым словам или фразе")
    @allure.testcase("API-2")
    @allure.description("""
    Предусловия:
    1. Создать тестовую среду.
    Шаги:
    1. Получить список всех игр.
    2. Выбрать рандомную игру и в качестве ключевого параметра выбрать часть ее названия игры
    3. Осуществить поиск по ключевому слову.
    4. Проверить, что ответ содержит только игру у которой в заголовке содержится ключевое слово.
    Ожидаемый результат:
    1. Функция поиска возвращает результаты, основанные только на предоставленном ключевом слове или фразе. """)
    def test_search_games_by_keywords_or_phrase(self):
        with allure.step("Получить список всех игр"):
            game = self.api_games.get_all_games()
        with allure.step("Выбрать рандомную игру и в качестве ключевого параметра выбрать часть ее названия игры"):
            extract_part_titles_game = self.conversion_data.extract_part_of_title_game(game)
            random_part_title = self.conversion_data.random_choice(extract_part_titles_game)
            query_param = self.conversion_data.create_query_param(random_part_title)
        with allure.step("Осуществить поиск по ключевому слову"):
            game = self.api_games.get_games_and_search(query_param)
            response = self.conversion_data.extract_titles(game)
        with allure.step("Проверить, что ответ содержит только игру у которой в заголовке содержится ключевое слово"):
            self.assertions.check_word_in_list(random_part_title, response)
