Public API
==========

.. automodule:: poloniex_aio.public
.. currentmodule:: poloniex_aio.public

Ticker
------
.. autofunction:: returnTicker(session)

24-hour volume
--------------
.. autofunction:: return24hVolume(session)

Order book
----------
.. autofunction:: returnOrderBook(session, *, currencyPair)

Trade history
-------------
.. autofunction:: returnTradeHistory(session, *, currencyPair, start=None, end=None)

Chart data
----------
.. autofunction:: returnChartData(session, *, currencyPair, start, end, period)

Currencies
----------
.. autofunction:: returnCurrencies(session)

Loan orders
-----------
.. autofunction:: returnLoanOrders(session, *, currency)
