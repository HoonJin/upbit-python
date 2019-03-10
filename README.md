# upbit-python

You can get detail information of API in [API Reference](https://docs.upbit.com/v1.0.1/reference)


## Installation
Install from Git Repository
```sh
pip install git+https://github.com/HoonJin/upbit-python.git
```

## Basic Usage
You can use public API very easily.
```python
import upbit
upbit.ticker(['KRW-BTC', 'KRW-ETH'])
upbit.orderbook(['KRW-BTC', 'KRW-ETH', ])
```
