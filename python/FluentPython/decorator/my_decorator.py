#!/usr/bin/python3
"""
Made for Learning decorator.
"""
def deco_without_tags(func):
    """Decorator Function with out tag"""
    def decorated(*args):
        print("Decorated function.")
        return func(*args)
    
    return decorated

def deco_with_tags(tag1, tag2):
    """Decorated function with tags on it."""
    def deco(func):
        def decorated(*args):
            print(f"decorated function with tags: {tag1}, {tag2}")
        return decorated
    return deco


@deco_without_tags
def func1(arg1, arg2):
    print(f'{arg1}, {arg2}')


@deco_with_tags("t1", "t2")
def func2(arg1, arg2):
    print("This is function2")

if __name__=="__main__":
    func1("hello", "function1")
    func2("hello", "function2")