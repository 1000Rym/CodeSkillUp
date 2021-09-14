def decorator1(func):
    """Decorator Function1"""
    def decorate(*args):
        print("Decorator Function1")
        return func(*args)
    return decorate

def decorator2(func):
    """Decorator Function2"""
    def decorate(*args):
        print("Decorator Function2")
        return func(*args)
    return decorate

def decorator_with_tags(activate = True):
    def decorator3(func):
        """Decorator function3"""
        def decorate(*args):
            print("Decorator Function3 with activate ={activate}" )
            return func(*args)

        return decorate
    return decorator3


@decorator2
@decorator1
def func1(*args):
    print("func1(%r) called!" %([arg for arg in args]))

@decorator_with_tags(activate=True)
def func2(*args):
    print("func(%r) called!" %([arg for arg in args]))

if __name__ == '__main__':
    func1(1,2,3)
    func2(4,5,6)