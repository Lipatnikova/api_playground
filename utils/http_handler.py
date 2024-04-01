import requests
from utils.assertions import Assertions
from utils.helper import Helper


class HTTPHandler(Helper):

    @staticmethod
    def get(url, headers, model, params=None):
        response = requests.get(url=url, headers=headers, params=params)
        Assertions.check_response_is_200(response)
        Helper.attach_response(response.json())
        return Helper.validate_model(response.json(), model)

    @staticmethod
    def post(url, headers, model, payload):
        response = requests.post(url=url, headers=headers, json=payload)
        Assertions.check_response_are_200_or_204(response)
        Helper.attach_response(response.json())
        return Helper.validate_model(response.json(), model)

    @staticmethod
    def post_headers(url, headers):
        response = requests.post(url=url, headers=headers)
        Assertions.check_response_is_205(response)

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
