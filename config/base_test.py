from services.users.api_users import UsersAPI
from services.games.api_games import GamesAPI
from utils.assertions import Assertions
from utils.conversion_data import ConversionData


class BaseUsersTest:

    def setup_method(self):
        self.api_users = UsersAPI()
        self.conversion_data = ConversionData()
        self.assertions = Assertions()


class BaseGamesTest:

    def setup_method(self):
        self.api_games = GamesAPI()


class BaseTest:
    def setup_method(self):
        self.api_users = UsersAPI()
        self.api_games = GamesAPI()

