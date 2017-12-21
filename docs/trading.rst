Trading API
===========

.. automodule:: poloniex_aio.trading
.. currentmodule:: poloniex_aio.trading

Balances
--------
.. autofunction:: returnBalances(session, api_key, secret_key)

Complete balances
-----------------
.. autofunction:: returnCompleteBalances(session, api_key, secret_key, *, account=None)

Deposit Addresses
-----------------
.. autofunction:: returnDepositAddresses(session, api_key, secret_key)

Generate new address
--------------------
.. autofunction:: generateNewAddress(session, api_key, secret_key, *, currency)

Depoists and withdrawals history
--------------------------------
.. autofunction:: returnDepositsWithdrawals(session, api_key, secret_key, *, start=None, end=None)

Open orders
-----------
.. autofunction:: returnOpenOrders(session, api_key, secret_key, *, currencyPair)

Trade History
-------------
.. autofunction:: returnTradeHistory(session, api_key, secret_key, *, currencyPair, start=None, end=None, limit=None)

Trades involving an order
-------------------------
.. autofunction:: returnOrderTrades(session, api_key, secret_key, *, orderNumber)

Buy order
---------
.. autofunction:: buy(session, api_key, secret_key, *, currencyPair, rate, amount, fillOrKill=None, immediateOrCancel=None, postOnly=None)

Sell order
----------
.. autofunction:: sell(session, api_key, secret_key, *, currencyPair, rate, amount, fillOrKill=None, immediateOrCancel=None, postOnly=None)

Cancer an order
---------------
.. autofunction:: cancelOrder(session, api_key, secret_key, *, orderNumber)

Move an order
-------------
.. autofunction:: moveOrder(session, api_key, secret_key, *, orderNumber, rate, amount=None, immediateOrCancel=None, postOnly=None)

Withdraw
--------
.. autofunction:: withdraw(session, api_key, secret_key, *, currency, amount, address, paymentId=None)

Fee info
--------
.. autofunction:: returnFeeInfo(session, api_key, secret_key)

Balances sorted by account
--------------------------
.. autofunction:: returnAvailableAccountBalances(session, api_key, secret_key, *, account=None)

Tradable balances
-----------------
.. autofunction:: returnTradableBalances(session, api_key, secret_key)

Transfers
---------
.. autofunction:: transferBalance(session, api_key, secret_key, *, currency, amount, fromAccount, toAccount)

Margin account summary
----------------------
.. autofunction:: returnMarginAccountSummary(session, api_key, secret_key)

Margin buy order
----------------
.. autofunction:: marginBuy(session, api_key, secret_key, *, currencyPair, rate, amount, lendingRate=None)

Margin sell order
-----------------
.. autofunction:: marginSell(session, api_key, secret_key, *, currencyPair, rate, amount, lendingRate=None)

Margin position
---------------
.. autofunction:: getMarginPosition(session, api_key, secret_key, *, currencyPair)

Close margin position
---------------------
.. autofunction:: closeMarginPosition(session, api_key, secret_key, *, currencyPair)

Create a loan offer
-------------------
.. autofunction:: createLoanOffer(session, api_key, secret_key, *, currency, amount, duration, autoRenew, lendingRate)

Cancel a loan offer
-------------------
.. autofunction:: cancelLoanOffer(session, api_key, secret_key, *, orderNumber)

Open loan offers
----------------
.. autofunction:: returnOpenLoanOffers(session, api_key, secret_key)

Active loans
------------
.. autofunction:: returnActiveLoans(session, api_key, secret_key)

Lending history
---------------
.. autofunction:: returnLendingHistory(session, api_key, secret_key, *, start, end, limit=None)

Toggles the autoRenew setting
-----------------------------
.. autofunction:: toggleAutoRenew(session, api_key, secret_key, *, orderNumber)
