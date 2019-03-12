import requests
from urllib.parse import urljoin
import logging


class Quotation:
    __DEFAULT_COUNT = 10

    def __init__(self):
        self.__host = 'https://api.upbit.com/v1/'
        self.__headers = {}

    def market(self):
        return self.__get('market/all')

    def candles_minutes(self, market: str, unit=1, to=None, count=__DEFAULT_COUNT):
        return self.__get(f'candles/minutes/{unit}', {
            'market': market,
            'to': to,
            'count': count
        })

    def trade_ticks(self, market: str, to=None, count=__DEFAULT_COUNT, cursor=None):
        return self.__get('trades/ticks', {
            'market': market,
            'to': to,
            'count': count,
            'cursor': cursor
        })

    def ticker(self, markets: list):
        return self.__get('ticker', {
            'markets': markets
        })

    def orderbook(self, markets: list):
        return self.__get('orderbook', {
            'markets': markets
        })

    def limits(self):
        return self.__headers['Remaining-Req']

    def __get(self, path: str, params: dict=None):
        r = requests.get(urljoin(self.__host, path), params=params)
        if r.status_code in [200, 201]:
            self.__headers = r.headers
            return r.json()
        else:
            logging.error(f"invalid_status_code: status_code: {r.status_code}, headers: {r.headers} body: {r.text}")
            raise Exception("invalid_status_code")
