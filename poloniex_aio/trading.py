"""
To use the trading API, you will need to create an API key.

Please note that there is a default limit of 6 calls per second.
"""

import hmac
import time
import urllib
import hashlib
from functools import wraps
from .utils.Bucket import poloniex_bucket


def trading_request(func):
        @wraps(func)
        async def async_request(session, api_key, secret_key, *args, **kwargs):
            data = {
                'nonce': int(time.time()*1000),
                'command': func.__name__
                }
            func(*args, **kwargs)
            data.update(kwargs)
            post_data = urllib.parse.urlencode(data).encode()
            sign = hmac.new(secret_key.encode(),
                            post_data,
                            hashlib.sha512).hexdigest()
            headers = {
                'Sign': sign,
                'Key': api_key
            }
            await poloniex_bucket.get_token()
            async with session.post('https://poloniex.com/tradingApi',
                                    data=data,
                                    headers=headers) as resp:
                return await resp.json()
        return async_request


@trading_request
def returnBalances():
    """
    Returns all of your available balances

    :param session:  Aiohttp client session object

    :param String api_key:  The API key

    :param String secret_key:  The API secret key

    """
    pass


@trading_request
def returnCompleteBalances(*, account=None):
    """
    Returns all of your balances, including available balance, balance on
    orders,and the estimated BTC value of your balance.

    :param session:  Aiohttp client session object

    :param String api_key:  The API key

    :param String secret_key:  The API secret key

    :param String account: By default, this call is limited to your exchange
        account; set this parameter to "all" to include your margin and
        lending accounts.

    """
    pass


@trading_request
def returnDepositAddresses():
    """
    Returns all of your deposit addresses.

    :param session:  Aiohttp client session object

    :param String api_key:  The API key

    :param String secret_key:  The API secret key

    """
    pass


@trading_request
def generateNewAddress(*, currency):
    """
    Generates a new deposit address

    :param session:  Aiohttp client session object

    :param String api_key:  The API key

    :param String secret_key:  The API secret key

    :param String currency: The address will be generated for the
        currency specified here

    """
    pass


@trading_request
def returnDepositsWithdrawals(*, start=None, end=None):
    """
    Returns your deposit and withdrawal history within a range

    :param session:  Aiohttp client session object

    :param String api_key:  The API key

    :param String secret_key:  The API secret key

    :param String start:
        UNIX timestamp. Every returned value will have a timestamps
        greater or equal.

    :param String end:
        UNIX timestamp. Every returned value will have a timestamps
        lower or equal.
    """
    pass


@trading_request
def returnOpenOrders(*, currencyPair):
    """
    Returns your open orders for a given market.

    :param session:  Aiohttp client session object

    :param String api_key:  The API key

    :param String secret_key:  The API secret key

    :param String currencyPair: The currency pair. Set this to "all"
        to return open orders for all markets.
    """
    pass


@trading_request
def returnTradeHistory(*, currencyPair, start=None, end=None, limit=None):
    """
    Returns your trade history for a given market.

    If you do not specify a range, it will be limited to one day.

    :param session:  Aiohttp client session object

    :param String api_key:  The API key

    :param String secret_key:  The API secret key

    :param String currencyPair: The currency pair. Set this to "all"
        to return open orders for all markets.

    :param String start:
        UNIX timestamp. Every returned value will have a timestamps
        greater or equal.

    :param String end:
        UNIX timestamp. Every returned value will have a timestamps
        lower or equal.

    :param String limit:
        Maximum number of returned values. Default to 500, max 10 000
    """
    pass


@trading_request
def returnOrderTrades(*, orderNumber):
    """
    Returns all trades involving a given order

    :param session:  Aiohttp client session object

    :param String api_key:  The API key

    :param String secret_key:  The API secret key

    :param String orderNumber: The order id

    """
    pass


@trading_request
def buy(*,
        currencyPair,
        rate,
        amount,
        fillOrKill=None,
        immediateOrCancel=None,
        postOnly=None):
    """
    Places a limit buy order in a given market.

    :param session:  Aiohttp client session object

    :param String api_key:  the API key

    :param String secret_key:  the API secret key

    :param String currencyPair: the currency pair

    :param String rate: the rate to buy

    :param String amount: the amount to buy

    :param String fillOrKill: a fill-or-kill order will either fill
        in its entirety or be completely aborted

    :param String immediateOrCancel: an immediate-or-cancel order can
        be partially or completely filled, but any portion of the order
        that cannot be filled immediately will be canceled rather than
        left on the order book.

    :param String postOnly: a post-only order will only be placed if no
        portion of it fills immediately; this guarantees you will never
        pay the taker fee on any part of the order that fills.

    """
    pass


@trading_request
def sell(*,
         currencyPair,
         rate,
         amount,
         fillOrKill=None,
         immediateOrCancel=None,
         postOnly=None):
    """
    Places a sell order in a given market. Parameters and output are the same as for the buy method.
    """
    pass


@trading_request
def cancelOrder(*, orderNumber):
    """
    Cancels an order you have placed in a given market.

    :param session:  Aiohttp client session object

    :param String api_key:  The API key

    :param String secret_key:  The API secret key

    :param String orderNumber:  Order ID

    """
    pass


@trading_request
def moveOrder(*,
              orderNumber,
              rate,
              amount=None,
              immediateOrCancel=None,
              postOnly=None):
    """
    Cancels an order and places a new one of the same type in a single atomic
    transaction, meaning either both operations will succeed or both will fail.

    :param session:  Aiohttp client session object

    :param String api_key:  The API key

    :param String secret_key:  The API secret key

    :param String orderNumber: The order id

    :param String rate: the new rate

    :param String amount: the new amount

    :param String immediateOrCancel: an immediate-or-cancel order can
        be partially or completely filled, but any portion of the order
        that cannot be filled immediately will be canceled rather than
        left on the order book.

    :param String postOnly: a post-only order will only be placed if no
        portion of it fills immediately; this guarantees you will never
        pay the taker fee on any part of the order that fills.

    """
    pass


@trading_request
def withdraw(*, currency, amount, address, paymentId=None):
    """
    Immediately places a withdrawal for a given currency

    :param session:  Aiohttp client session object

    :param String api_key:  The API key

    :param String secret_key:  The API secret key

    :param String currency: The currency to withdraw

    :param String amount: The amount to withdraw

    :param String address: The destination address

    :param String paymentId: XMR only

    """
    pass


@trading_request
def returnFeeInfo():
    """
    If you are enrolled in the maker-taker fee schedule,
    returns your current trading fees and trailing 30-day volume in BTC.

    This information is updated once every 24 hours.

    :param session:  Aiohttp client session object

    :param String api_key:  The API key

    :param String secret_key:  The API secret key

    """
    pass


@trading_request
def returnAvailableAccountBalances(*, account=None):
    """
    Returns your balances sorted by account.

    :param session:  Aiohttp client session object

    :param String api_key:  The API key

    :param String secret_key:  The API secret key

    :param String account:
        if you wish to fetch only the balances of one account, set the account here.

    """
    pass


@trading_request
def returnTradableBalances():
    """
    Returns your current tradable balances for each currency in each market
    for which margin trading is enabled.

    :param session:  Aiohttp client session object

    :param String api_key:  The API key

    :param String secret_key:  The API secret key

    """
    pass


@trading_request
def transferBalance(*, currency, amount, fromAccount, toAccount):
    """
    Transfers funds from one account to another.

    :param session:  Aiohttp client session object

    :param String api_key:  The API key

    :param String secret_key:  The API secret key

    :param String fromAccount:  Source account

    :param String toAccount:  Destination account

    """
    pass


@trading_request
def returnMarginAccountSummary():
    """
    Returns a summary of your entire margin account.

    :param session:  Aiohttp client session object

    :param String api_key:  The API key

    :param String secret_key:  The API secret key

    """
    pass


@trading_request
def marginBuy(*, currencyPair, rate, amount, lendingRate=None):
    """
    Places a margin buy order in a given market.

    :param session:  Aiohttp client session object

    :param String api_key:  The API key

    :param String secret_key:  The API secret key

    :param String currencyPair: The currency pair

    :param String rate: The order rate.

    :param String amount: The order amount.

    :param String lendingRate: Maximum lending rate.


    """
    pass


@trading_request
def marginSell(*, currencyPair, rate, amount, lendingRate=None):
    """
    Places a margin sell order in a given market. Parameters and output are
    the same as for the marginBuy method.
    """
    pass


@trading_request
def getMarginPosition(*, currencyPair):
    """
    Returns information about your margin position in a given market.

    :param session:  Aiohttp client session object

    :param String api_key:  The API key

    :param String secret_key:  The API secret key

    :param String currencyPair: The currency pair. Set this to "all"
        if you wish to fetch all of your margin positions at once.
    """
    pass


@trading_request
def closeMarginPosition(*, currencyPair):
    """
    Closes your margin position in a given market.

    :param session:  Aiohttp client session object

    :param String api_key:  The API key

    :param String secret_key:  The API secret key

    :param String currencyPair: The currency pair.

    """
    pass


@trading_request
def createLoanOffer(*, currency, amount, duration, autoRenew, lendingRate):
    """
    Creates a loan offer for a given currency.

    :param session:  Aiohttp client session object

    :param String api_key:  The API key

    :param String secret_key:  The API secret key

    :param String currency: The currency to lend

    :param String amount: Amount of currency to lend

    :param String duration: Lending duration

    :param String autoRenew: Should the loan offer auto renew.

    :param String lendingRate: The lending rate

    """
    pass


@trading_request
def cancelLoanOffer(*, orderNumber):
    """
    Cancels a loan offer

    :param session:  Aiohttp client session object

    :param String api_key:  The API key

    :param String secret_key:  The API secret key

    :param String orderNumber: The loan offer ID

    """
    pass


@trading_request
def returnOpenLoanOffers():
    """
    Returns your open loan offers for each currency.

    :param session:  Aiohttp client session object

    :param String api_key:  The API key

    :param String secret_key:  The API secret key

    """
    pass


@trading_request
def returnActiveLoans():
    """
    Returns your active loans for each currency.

    :param session:  Aiohttp client session object

    :param String api_key:  The API key

    :param String secret_key:  The API secret key

    """
    pass


@trading_request
def returnLendingHistory(*, start, end, limit=None):
    """
    Returns your lending history within a time range.

    :param session:  Aiohttp client session object

    :param String api_key:  The API key

    :param String secret_key:  The API secret key

    :param String start:
        UNIX timestamp. Every returned value will have a timestamps
        greater or equal.

    :param String end:
        UNIX timestamp. Every returned value will have a timestamps
        lower or equal.

    :param String limit:
        Maximum number of returned values.

    """
    pass


@trading_request
def toggleAutoRenew(*, orderNumber):
    """
    Toggles the autoRenew setting on an active.

    :param session:  Aiohttp client session object

    :param String api_key:  The API key

    :param String secret_key:  The API secret key

    :param String orderNumber:  The loan ID

    """
    pass
