from config.base_host import BaseHost


class Endpoints:
    create_user = f"{BaseHost.HOST}/users"
    get_all_users = f"{BaseHost.HOST}/users"
    get_user_by_id = lambda self, uuid: f"{BaseHost.HOST}/users/{uuid}"
