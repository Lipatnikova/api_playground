import requests
from utils.assertions import Assertions
from utils.helper import Helper


class HTTPHandler(Helper):
    @staticmethod
    def get(url, headers, model):
        response = requests.get(url=url, headers=headers)
        Assertions.check_response_is_200(response)
        Helper.attach_response(response.json())
        return Helper.validate_model(response.json(), model)

    @staticmethod
    def post(url, headers, json_data, model):
        response = requests.post(url=url, headers=headers, json=json_data)
        Assertions.check_response_are_200_or_204(response)
        Helper.attach_response(response.json())
        return Helper.validate_model(response.json(), model)

    @staticmethod
    def delete(url, headers):
        response = requests.delete(url=url, headers=headers)
        Assertions.check_response_is_204(response)
        return response

    @staticmethod
    def double_delete(url, headers):
        response = requests.delete(url=url, headers=headers)
        Assertions.check_response_is_404(response)
        return response
