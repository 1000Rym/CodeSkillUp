def deco(func):
    print("deco function")
    return func

@deco
def my_function():
    print("my function")


if __name__ == '__main__':
    my_function()

