import requests
from urllib.parse import urljoin


class Quotation:
    def __init__(self):
        self.host = 'https://api.upbit.com/v1/'

    def market(self):
        return self.__get('market/all')

    def __get(self, path, params: dict=None):
        return requests.get(urljoin(self.host, path), params=params)
