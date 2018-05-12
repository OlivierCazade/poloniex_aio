import asyncio
from time import time


class _Bucket:
    """
    Simplified token Bucket implementation.

    Used to add a rate limit
    """
    def __init__(self, rate, period=1.0, retry_interval=0.01):
        self.rate = rate
        self.token_period = period / rate
        self.token = 0
        self.retry_interval = retry_interval
        self.timestamp = time()

    async def get_token(self):
        while self.token <= 0:
            now = time()
            if now - self.timestamp > self.token_period:
                self.token += 1
                self.timestamp = now
            await asyncio.sleep(self.retry_interval)
        self.token -= 1
        return


poloniex_bucket = _Bucket(5)
