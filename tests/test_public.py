from poloniex_aio import public
import aiohttp
import pytest
import asyncio
import time


_test_pair = "BTC_ETH"
_test_currency = "BTC"


@pytest.mark.asyncio
async def test_returnTicker():
    async with aiohttp.ClientSession() as client:
        res = await public.returnTicker(client)
        assert _test_pair in res


@pytest.mark.asyncio
async def test_return24hVolume():
    async with aiohttp.ClientSession() as client:
        res = await public.return24hVolume(client)
        assert _test_pair in res


@pytest.mark.asyncio
async def test_returnOrderBook():
    async with aiohttp.ClientSession() as client:
        res = await public.returnOrderBook(client, currencyPair=_test_pair)
        assert "asks" in res
        assert len(res['asks']) > 0
        assert "bids" in res
        assert len(res['bids']) > 0


@pytest.mark.asyncio
async def test_returnTradeHistory():
    async with aiohttp.ClientSession() as client:
        res = await public.returnTradeHistory(client, currencyPair=_test_pair)
        assert len(res) > 0


@pytest.mark.asyncio
async def test_returnChartData():
    async with aiohttp.ClientSession() as client:
        res = await public.returnChartData(client,
                                           currencyPair=_test_pair,
                                           start="1483228800",
                                           end="1485907200",
                                           period="86400")
        assert len(res) > 0


@pytest.mark.asyncio
async def test_returnCurrencies():
    async with aiohttp.ClientSession() as client:
        res = await public.returnCurrencies(client)
        assert len(res) > 0
        assert _test_currency in res


@pytest.mark.asyncio
async def test_returnLoanOrders():
    async with aiohttp.ClientSession() as client:
        res = await public.returnLoanOrders(client, currency=_test_currency)
        assert "offers" in res
        assert len(res["offers"]) > 0


@pytest.mark.asyncio
async def test_requestRate():
    async with aiohttp.ClientSession() as client:
        start = time.time()
        tasks = [public.returnCurrencies(client)
                 for i in range(6)]
        await asyncio.wait(tasks)
        end = time.time()
        assert end - start > 1
