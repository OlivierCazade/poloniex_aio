import hmac
import time
import urllib
import hashlib


def trading_request(func):
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
            async with session.post('https://poloniex.com/tradingApi',
                                    data=data,
                                    headers=headers) as resp:
                return await resp.json()
        return async_request


@trading_request
def returnBalances():
    pass


@trading_request
def returnCompleteBalances(*, account=None):
    pass


@trading_request
def returnDepositAddresses():
    pass


@trading_request
def generateNewAddress(*, currency):
    pass


@trading_request
def returnDepositsWithdrawals(*, start=None, end=None):
    pass


@trading_request
def returnOpenOrders(*, currencyPair):
    pass


@trading_request
def returnTradeHistory(*, currencyPair, start=None, end=None, limit=None):
    pass


@trading_request
def returnOrderTrades(*, orderNumber):
    pass


@trading_request
def buy(*,
        currencyPair,
        rate,
        amount,
        fillOrKill=None,
        immediateOrCancel=None,
        postOnly=None):
    pass


@trading_request
def sell(*,
         currencyPair,
         rate,
         amount,
         fillOrKill=None,
         immediateOrCancel=None,
         postOnly=None):
    pass


@trading_request
def cancelOrder(*, orderNumber):
    pass


@trading_request
def moveOrder(*,
              orderNumber,
              rate,
              amount=None,
              immediateOrCancel=None,
              postOnly=None):
    pass


@trading_request
def withdraw(*, currency, amount, address, paymentId=None):
    pass


@trading_request
def returnFeeInfo():
    pass


@trading_request
def returnAvailableAccountBalances(*, account=None):
    pass


@trading_request
def returnTradableBalances():
    pass


@trading_request
def transferBalance(*, currency, amount, fromAccount, toAccount):
    pass


@trading_request
def returnMarginAccountSummary():
    pass


@trading_request
def marginBuy(*, currencyPair, rate, amount, lendingRate=None):
    pass


@trading_request
def marginSell(*, currencyPair, rate, amount, lendingRate=None):
    pass


@trading_request
def getMarginPosition(*, currencyPair):
    pass


@trading_request
def closeMarginPosition(*, currencyPair):
    pass


@trading_request
def createLoanOffer(*, currency, amount, duration, autoRenew, lendingRate):
    pass


@trading_request
def cancelLoanOffer(*, orderNumber):
    pass


@trading_request
def returnOpenLoanOffers():
    pass


@trading_request
def returnActiveLoans():
    pass


@trading_request
def returnLendingHistory(*, start, end, limit=None):
    pass


@trading_request
def toggleAutoRenew(*, orderNumber):
    pass
