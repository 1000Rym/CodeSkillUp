from random import randint
import time
import asyncio

def get_odds(start, end):
    """Generator is a producer."""
    """Sequence of odds from start point to end point"""
    odd_start = start if start%2==1 else start+1
    for odd in range(odd_start, end+1, 2):
        yield odd

async def get_random_number():
    """Something happenes in the  backgroud of python project"""
    # time.sleep(3)
    await asyncio.sleep(3)
    return randint(1,10)

async def get_square_odds(start, end):
    for odd in get_odds(start,end):
        await asyncio.sleep(2) # pretending do process on file swerver or database.
        yield odd**2

async def main():
    odd_values = [odd for odd in get_odds(3,15)] #List comprehension
    odd_values2 = tuple(get_odds(21, 29)) # Turn generator to tuple
    print(odd_values)
    print(odd_values2)

    start = time.perf_counter()
    #random_number = await get_random_number()
    #random_number = await asyncio.gather(get_random_number(),get_random_number(),get_random_number())
    random_number = await asyncio.gather(*(get_random_number() for _ in range(10)))
    elapsed = time.perf_counter() - start
    print(f'Time {elapsed:.2f} to get random number {random_number}')

    async for square_odd in get_square_odds(11, 17):
        print('Square Odds:', square_odd)


if __name__ == '__main__':
    asyncio.run(main())
