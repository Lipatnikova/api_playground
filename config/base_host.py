import os


class BaseHost:
    HOST = "https://dev-gs.qa-playground.com/api/v1" if os.environ["STAGE"] == "qa" \
        else "https://release-gs.qa-playground.com/api/v1"


class APIRoutes:
    USERS = "/users"
    GAMES = "/games"
    SEARCH = "/ search"

