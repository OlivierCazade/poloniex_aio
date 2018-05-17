from .public import returnTradeHistory
import time


async def tradeHistory(session, currencyPair, start, end):
    last_id = -1
    while start < end:
        tmp_time = end - (3600 * 24 * 10)
        dup_found = False
        res = await returnTradeHistory(session,
                                       currencyPair=currencyPair,
                                       start=tmp_time,
                                       end=end + 3600)

        for trade in res:
            if last_id == -1 or last_id <= trade["globalTradeID"]:
                # This function assume Ids values always increase
                dup_found = True
                continue
            yield trade
        if dup_found is False:
            raise Exception('Missed some trades')
        end = int(time.mktime(time.strptime(res[-1]["date"] + " UTC",
                                            "%Y-%m-%d %H:%M:%S %Z")))
        last_id = res[-1]["globalTradeID"]
