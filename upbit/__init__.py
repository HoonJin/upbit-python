from .quotation import Quotation
from .exchange import Exchange
from .const import *


__quotation = Quotation()
market_all = __quotation.market_all
candles_minutes = __quotation.candles_minutes
ticker = __quotation.ticker
orderbook = __quotation.orderbook
