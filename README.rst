Poloniex-aio
=================================

An async library for `Poloniex api <https://poloniex.com/support/api/>`_

This library is still exerimental.

.. image:: https://api.travis-ci.org/OlivierCazade/poloniex_aio.svg?branch=master
	   :target: https://travis-ci.org/OlivierCazade/poloniex_aio

Usage
-----

.. code:: python

   from poloniex_aio import public

   async def printTicker():
    async with aiohttp.ClientSession() as client:
        res = await public.returnTicker(client)
	print(res)
