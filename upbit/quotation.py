from .const import *
import requests
from urllib.parse import urljoin
import logging


class Quotation:
    def __init__(self):
        self.__host = 'https://api.upbit.com/v1/'

    # https://docs.upbit.com/v1.0.1/reference#%EC%8B%9C%EC%84%B8-%EC%A2%85%EB%AA%A9-%EC%A1%B0%ED%9A%8C
    def market_all(self):
        return self.__get('market/all')

    # https://docs.upbit.com/v1.0.1/reference#%EB%B6%84minute-%EC%BA%94%EB%93%A4-1
    def candles_minutes(self, market: str=Order.DEFAULT_MARKET, unit=1, to=None, count=Order.DEFAULT_COUNT):
        return self.__get(f'candles/minutes/{unit}', {
            'market': market,
            'to': to,
            'count': count
        })

    # https://docs.upbit.com/v1.0.1/reference#%EB%8B%B9%EC%9D%BC-%EC%B2%B4%EA%B2%B0-%EB%82%B4%EC%97%AD
    def trades_ticks(self, market: str=Order.DEFAULT_MARKET, to=None, count=Order.DEFAULT_COUNT, cursor=None):
        return self.__get('trades/ticks', {
            'market': market,
            'to': to,
            'count': count,
            'cursor': cursor
        })

    # https://docs.upbit.com/v1.0.1/reference#ticker%ED%98%84%EC%9E%AC%EA%B0%80-%EB%82%B4%EC%97%AD
    def ticker(self, markets: list):
        return self.__get('ticker', {'markets': markets})

    # https://docs.upbit.com/v1.0.1/reference#%EC%8B%9C%EC%84%B8-%ED%98%B8%EA%B0%80-%EC%A0%95%EB%B3%B4orderbook-%EC%A1%B0%ED%9A%8C
    def orderbook(self, markets: list):
        return self.__get('orderbook', {'markets': markets})

    def __get(self, path: str, params: dict=None, headers: dict = None):
        r = requests.get(urljoin(self.host, path), params=params, headers=headers)
        if r.status_code in [200, 201]:
            return r.json()
        else:
            logging.error(f"path: {path}: status_code: {r.status_code}, headers: {r.headers} body: {r.text}")
            raise Exception("invalid_status_code")

    @property
    def host(self):
        return self.__host
