import random


class ConversionData:

    @staticmethod
    def extract_uuids(users_before):
        return [str(item['uuid']) for item in users_before['items']]

    @staticmethod
    def random_choice(items):
        return random.choice(items)
