import allure
import requests

from utils.helper import Helper
from services.games.endpoints import Endpoints
from services.games.payloads import Payloads
from config.headers import Headers
from services.games.models.game_model import GameModel, GamesModel, GamesSearchModel


class UsersAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Get game by ID")
    def get_game_by_id(self, uuid):
        response = requests.get(
            url=self.endpoints.get_game(uuid),
            headers=self.headers.basic,
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = GameModel(**response.json())
        return model

    @allure.step("Get all games")
    def get_all_games(self):
        response = requests.get(
            url=self.endpoints.games,
            headers=self.headers.basic,
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = GamesModel(**response.json())
        return model.model_dump()

    @allure.step("Get all games by search")
    def get_all_games(self):
        response = requests.get(
            url=self.endpoints.games_and_search,
            headers=self.headers.basic,
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = GamesSearchModel(**response.json())
        return model.model_dump()
