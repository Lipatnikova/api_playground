import allure
import json
import random
from allure_commons.types import AttachmentType
from pydantic import ValidationError


class Helper:

    @staticmethod
    def random_choice(items):
        return random.choice(items)

    @staticmethod
    def attach_response(response):
        response = json.dumps(response, indent=4)
        allure.attach(body=response, name="API Response", attachment_type=AttachmentType.JSON)

    @staticmethod
    def validate_model(response_json, model):
        try:
            validated_data = model.model_validate(response_json)
        except ValidationError as e:
            print(e.json())
            raise Exception("API response is incorrect")

        return validated_data.model_dump()
