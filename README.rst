Poloniex-aio
=================================

An async library for `Poloniex api <https://poloniex.com/support/api/>`_ with builtin requests rate control.

This library is still exerimental.

.. image:: https://api.travis-ci.org/OlivierCazade/poloniex_aio.svg?branch=master
	   :target: https://travis-ci.org/OlivierCazade/poloniex_aio


Install
-------

A pip package is available.

.. code:: python

   pip3 install poloniex-aio


Usage
-----

Full documentation available at `readthedocs <https://poloniex-aio.readthedocs.io/en/stable/>`_

.. code:: python

   from poloniex_aio import public

   async def printTicker():
    async with aiohttp.ClientSession() as client:
        res = await public.returnTicker(client)
	print(res)
