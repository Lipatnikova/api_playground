from config.base_host import BaseHost


class Endpoints:
    games = f"{BaseHost.HOST}/games"
    games_and_search = f"{BaseHost.HOST}/games/search"
    get_game = lambda self, uuid: f"{BaseHost.HOST}/games/{uuid}"
