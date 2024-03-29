from config.status_code import StatusCode
# from services.users.api_users import UsersAPI


class Assertions:
    @staticmethod
    def check_response_is_200(response) -> None:
        """The method to check if the response status code is 200 (OK)"""
        status_code = response.status_code
        assert status_code == StatusCode.OK, \
            f'Response status code is incorrect, actual: {status_code}, expected : {StatusCode.OK}'

    @staticmethod
    def check_response_is_204(response) -> None:
        """The method to check if the response status code is 204 (No Content)"""
        status_code = response.status_code
        assert status_code == StatusCode.NO_CONTENT, \
            f'Response status code is incorrect, actual: {status_code}, expected : {StatusCode.NO_CONTENT}'

    @staticmethod
    def check_response_are_200_or_204(response) -> None:
        """The method to check if the response status code are 200 (OK) or 204 (No Content)"""
        status_code = response.status_code
        assert status_code == StatusCode.OK or StatusCode.NO_CONTENT, \
            f'Response status code is incorrect, actual: {status_code}'

    @staticmethod
    def check_response_is_404(response) -> None:
        """The method to check if the response status code is 404 (Not found)"""
        status_code = response.status_code
        assert status_code == StatusCode.NOT_FOUND, \
            f'Response status code is incorrect, actual: {status_code}, expected : {StatusCode.NOT_FOUND}'
