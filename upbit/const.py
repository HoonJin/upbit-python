class Order:
    DEFAULT_MARKET = 'KRW-BTC'
    DEFAULT_COUNT = 10

    class State:
        WAIT = 'wait'
        DONE = 'done'
        CANCEL = 'cancel'

    class OrderBy:
        ASC = 'asc'
        DESC = 'desc'
