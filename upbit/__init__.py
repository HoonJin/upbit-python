from .quotation import Quotation
from .exchange import Exchange
from .const import *


__quotation = Quotation()
market = __quotation.market
candles_minutes = __quotation.candles_minutes
ticker = __quotation.ticker
orderbook = __quotation.orderbook
