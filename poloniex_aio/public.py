def public_request(func):
        async def async_request(session, *args, **kwargs):
            func(*args, **kwargs)
            params = {
                'command': func.__name__
                }
            params.update(kwargs)
            async with session.get('https://poloniex.com/public',
                                   params=params) as resp:
                return await resp.json()
        return async_request


@public_request
def returnTicker():
    pass


@public_request
def return24hVolume():
    pass


@public_request
def returnOrderBook(*, currencyPair):
    pass


@public_request
def returnTradeHistory(*, currencyPair, start=None, end=None):
    pass


@public_request
def returnChartData(*, currencyPair, start, end, period):
    pass


@public_request
def returnCurrencies():
    pass


@public_request
def returnLoanOrders(*, currency):
    pass
