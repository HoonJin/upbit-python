import hashlib
import logging
import time
import uuid
from urllib.parse import urlencode, urljoin

import jwt
import requests

from .const import *
from .quotation import Quotation


class Exchange(Quotation):
    def __init__(self, access_key, secret_key):
        super(self.__class__, self).__init__()
        self.__access_key = access_key
        self.__secret_key = secret_key

    # https://docs.upbit.com/reference#%EC%9E%90%EC%82%B0-%EC%A1%B0%ED%9A%8C
    # https://docs.upbit.com/reference#%EC%A0%84%EC%B2%B4-%EA%B3%84%EC%A2%8C-%EC%A1%B0%ED%9A%8C
    def get_accounts(self):
        return self.__get('accounts', headers=self.__make_headers())

    # https://docs.upbit.com/reference#%EC%A3%BC%EB%AC%B8
    # https://docs.upbit.com/reference#%EC%A3%BC%EB%AC%B8-%EA%B0%80%EB%8A%A5-%EC%A0%95%EB%B3%B4
    def get_orders_change(self, market=Order.DEFAULT_MARKET):
        params = {'market': market}
        return self.__get('orders/chance', params, self.__make_headers(params))

    # https://docs.upbit.com/reference#%EA%B0%9C%EB%B3%84-%EC%A3%BC%EB%AC%B8-%EC%A1%B0%ED%9A%8C
    def get_order(self, uid: str):
        params = {'uuid': uid}
        return self.__get('order', params, self.__make_headers(params))

    # https://docs.upbit.com/reference#%EC%A3%BC%EB%AC%B8-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%A1%B0%ED%9A%8C
    def get_orders(self, market: str, state: str = Order.State.WAIT, page: int = 1, order_by: str = Order.OrderBy.ASC):
        params = {
            'market': market,
            'state': state,
            'page': page,
            'order_by': order_by
        }
        return self.__get('orders', params, self.__make_headers(params))

    # https://docs.upbit.com/reference#%EC%A3%BC%EB%AC%B8%ED%95%98%EA%B8%B0-1
    def post_orders(self, market: str, side: str, volume, price, ord_type):
        payload = {
            'market': market,
            'side': side,
            'volume': volume,
            'price': price,
            'ord_type': ord_type,
        }
        return self.__post('orders', payload, self.__make_headers(payload))

    # https://docs.upbit.com/reference#%EC%A3%BC%EB%AC%B8-%EC%B7%A8%EC%86%8C
    def delete_order(self, market: str, uid: str):
        params = {
            'market': market,
            'uuid': uid
        }
        return self.__delete('order', params, self.__make_headers(params))

    def __make_token(self, query: dict = None) -> str:
        payload = {
            'access_key': self.__access_key,
            'nonce': str(uuid.uuid4())
        }
        if query is not None:
            query_bytes = urlencode(query).encode()
            m = hashlib.sha512()
            m.update(query_bytes)
            payload['query_hash'] = m.hexdigest()
            payload['query_hash_alg'] = 'SHA512'
        return jwt.encode(payload=payload, key=self.__secret_key).decode('utf-8')

    def __make_headers(self, query: dict = None) -> dict:
        return {'Authorization': f'Bearer {self.__make_token(query)}'}

    def __post(self, path: str, payload: dict = None, headers: dict = None):
        r = requests.get(urljoin(self.host, path), data=payload, headers=headers)
        if r.status_code in [200, 201]:
            self.__headers = r.headers
            return r.json()
        else:
            logging.error(f"path: {path}: status_code: {r.status_code}, headers: {r.headers} body: {r.text}")
            raise Exception("invalid_status_code")

    def __delete(self, path: str, params: dict = None, headers: dict = None):
        r = requests.delete(urljoin(self.host, path), params=params, headers=headers)
        if r.status_code in [200, 201]:
            self.__headers = r.headers
            return r.json()
        else:
            logging.error(f"path: {path}: status_code: {r.status_code}, headers: {r.headers} body: {r.text}")
            raise Exception("invalid_status_code")

    def __get(self, path: str, params: dict = None, headers: dict = None):
        return self._Quotation__get(path, params, headers)

    @property
    def nonce(self):
        return int(time.time() * 1000)
