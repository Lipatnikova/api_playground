from config.base_host import BaseHost, APIRoutes


class Endpoints:
    create_user = f"{BaseHost.HOST}{APIRoutes.USERS}"
    get_all_users = f"{BaseHost.HOST}{APIRoutes.USERS}"
    get_user_by_id = lambda self, uuid: f"{BaseHost.HOST}{APIRoutes.USERS}/{uuid}"
