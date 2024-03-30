import allure

from services.games.endpoints import Endpoints
from services.games.payloads import Payloads
from config.headers import Headers
from services.games.models.games_model import GameModel, GamesModel
from utils.http_handler import HTTPHandler


class GamesAPI(HTTPHandler):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    def get_game_by_id(self, uuid):
        with allure.step("Get game by ID"):
            response = HTTPHandler.get(
                url=self.endpoints.get_game(uuid),
                headers=self.headers.basic,
                model=GameModel
            )
            return response

    def get_all_games(self):
        with allure.step("Get all games"):
            response = HTTPHandler.get(
                url=self.endpoints.games,
                headers=self.headers.basic,
                model=GamesModel
            )
            return response

    def get_games_and_search(self, query):
        with allure.step("Get games and search"):
            response = HTTPHandler.get(
                url=self.endpoints.games_and_search,
                headers=self.headers.basic,
                model=GamesModel,
                params=query
            )
            return response
