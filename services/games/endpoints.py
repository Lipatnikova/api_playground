from config.base_host import BaseHost, APIRoutes


class Endpoints:
    games = f"{BaseHost.HOST}{APIRoutes.GAMES}"
    games_and_search = f"{BaseHost.HOST}{APIRoutes.GAMES}{APIRoutes.SEARCH}"
    get_game = lambda self, uuid: f"{BaseHost.HOST}{APIRoutes.GAMES}{uuid}"
