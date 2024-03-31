from utils.helper import Helper


class ConversionData(Helper):

    @staticmethod
    def create_query_param(query_string):
        return {"query": query_string}

    @staticmethod
    def extract_uuids(users):
        return [str(item['uuid']) for item in users['items']]

    @staticmethod
    def extract_titles(games):
        return [str(item['title']) for item in games['items']]

    @staticmethod
    def extract_part_of_title_game(games):
        return [str(item['title'][4:10]) for item in games['items']]

    @staticmethod
    def remove_uuid(data):
        del data['uuid']
        return data
