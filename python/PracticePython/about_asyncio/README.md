# asyncio 

## Abstract
In this page, we are going to learn the follwoing things related with asyncio.

- Definition of asyncio. 
- Generators
- Coroutines
- Aynchronous Generators

## Knowledge
- asiyncio
    - A library write concurrent(could be run in parrarle) code using the async/await syntax.
    - Used in __IO-bounded and high level structured network__ code.
        - (__cpu__: Use multiprocessing library)
    
    - Requests : Only one process, In one thread.
    - EventLoop: Sent out request to external interface.
    - Intensive Operation: The process could be ran in parrarles. 
    - Keyword expression: 
        - `async def`: The function is calling async process on it
        - `await func_name` Wait for the async function finished
        - `await asyncio.gather(func1, func2...)`: Gather and call multiple async function. 
        - `async for`: Call async function in for loop.
    - Easy Example: [simple_odds.py](simple_odds.py)
    - Realword Example: [async_request_ex.py](async_request_ex.py)