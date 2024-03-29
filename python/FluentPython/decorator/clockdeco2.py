import time
import functools

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_list = []

        if args is not None:
            arg_list.extend([repr(arg) for arg in args])
        
        if kwargs is not None: 
            arg_list.extend(f'{key}, {value}' for key, value in kwargs.items())

        arg_str = ','.join(arg_list)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked

@functools.lru_cache()
@clock
def fibonacci(n): 
    if n<2: return n
    else : return fibonacci(n-2) + fibonacci(n-1)


if __name__=='__main__': 
    print(fibonacci(6))