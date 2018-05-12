"""
Public API does not require any Poloniex account.

Note that making
more than 6 calls per second to the public API, or repeatedly and
needlessly fetching excessive amounts of data, can result in your
IP being banned.
"""

from functools import wraps
from .utils.Bucket import poloniex_bucket


def public_request(func):
        @wraps(func)
        async def async_request(session, *args, **kwargs):
            func(*args, **kwargs)
            params = {
                'command': func.__name__
                }
            params.update(kwargs)
            await poloniex_bucket.get_token()
            async with session.get('https://poloniex.com/public',
                                   params=params) as resp:
                return await resp.json()
        return async_request


@public_request
def returnTicker():
    """
    Returns the ticker for all markets.

    :param session:  Aiohttp client session object

    """
    pass


@public_request
def return24hVolume():
    """
    Returns the 24-hour volume for all markets,
    plus totals for primary currencies.

    :param session:  Aiohttp client session object

    """
    pass


@public_request
def returnOrderBook(*, currencyPair):
    """
    Returns the order book for a given market,
    as well as a sequence number for use with the Push API and an indicator
    specifying whether the market is frozen.

    :param session:  Aiohttp client session object

    :param String currencyPair:  Market identifier, example : BTC_ETH

    """
    pass


@public_request
def returnTradeHistory(*, currencyPair, start=None, end=None):
    """
    Returns the past 200 trades for a given market, or up to 50,000 trades
    between a range specified in UNIX timestamps by the "start" and "end"
    parameters.

    :param session:  Aiohttp client session object

    :param String currencyPair:  Market identifier, example : BTC_ETH

    :param String start:
        UNIX timestamp. Every returned trade will have a timestamps
        greater or equal.

    :param String end:
        UNIX timestamp. Every returned trade will have a timestamps
        lower or equal.

    """
    pass


@public_request
def returnChartData(*, currencyPair, start, end, period):
    """
    Returns candlestick chart data.

    :param session:  Aiohttp client session object

    :param String currencyPair:  Market identifier, example : BTC_ETH

    :param String start:
        UNIX timestamp. Every returned trade will have a timestamps
        greater or equal.

    :param String end:
        UNIX timestamp. Every returned trade will have a timestamps
        lower or equal.

    :param String period:
        candlestick period in seconds; valid values are 300, 900, 1800,
        7200, 14400, and 86400

    """
    pass


@public_request
def returnCurrencies():
    """

    :param session:  Aiohttp client session object

    Returns information about currencies.
    """
    pass


@public_request
def returnLoanOrders(*, currency):
    """
    Returns the list of loan offers and demands for a given currency,
    specified by the "currency" GET parameter.

    :param session:  Aiohttp client session object

    :param String currency:  Currency identifier, example : BTC

    """
    pass
