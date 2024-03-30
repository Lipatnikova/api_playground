from services.users.api_users import UsersAPI
from services.games.api_games import GamesAPI


class BaseUsersTest:

    def setup_method(self):
        self.api_users = UsersAPI()


class BaseGamesTest:

    def setup_method(self):
        self.api_games = GamesAPI()


class BaseTest:
    def setup_method(self):
        self.api_users = UsersAPI()
        self.api_games = GamesAPI()

