import asyncio
import json # turn json to dic
import time
from typing import Text

import aiohttp 

async def worker(name, number, session):
    print(f'worker - {name}')
    url = f'https://qrng.anu.edu.au/API/jsonI.php?length={number}&type=uint16'
    response = await session.request(method='GET', url = url)
    value = await response.text()
    value = json.loads(value) # Turn class string to dictionry
    return sum(value['data'])


async def main():
    async with aiohttp.ClientSession() as session:
        #response = await worker('bob', 3, session)
        sums = await asyncio.gather(*(worker(f'worker{i}', n, session) for i, n in enumerate(range(2,30))))
        print('sums:', sums)
        #print('response is ', response, type(response))

if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"The process is finished in {elapsed :.2f} seconds.")