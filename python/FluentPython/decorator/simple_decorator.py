def decorator1(func):
    def decorated_function1(*args):
        print("[decorator1]Previously decorated before %s" %func.__name__)
        return_func= func(*args)
        print("[decorator1]Decorated after the %s" %func.__name__) 
        return return_func
    return decorated_function1

def decorator2(func):
    def decorated_function2(*args):
        print("[decorator2]Previously decorated before %s" %func.__name__)
        return_func= func(*args)
        print("[decorator2]Decorated after the %s" %func.__name__) 
        return return_func
    return decorated_function2



@decorator1
def function2decorate(*args):
    print("function2decorate({0})called!".format(args))

class SampleClass():
    def __init__(self):
        print("Sample Class is called.")
    
    @decorator1
    def method2decorate(self, *args):
        print("method2decorate{0} is called".format(args))

def decorator_with_tags(*tags, **kwtags):
    def decorator_function(func):
        def decorated_function(*args):
            print("[function decorator with tag]Previously decorated before %s, %s, %s" %(func.__name__, tags, kwtags))
            return_func= func(*args)
            print("[function decorator with tag]Decorated after the %s" %func.__name__)
            return return_func
        return decorated_function
    return decorator_function

@decorator_with_tags("a","b", key0="value0", key1="value1")
def function2decorate2(*args):
    print("function2decorate2(%r) called!" %([arg for arg in args]))

@decorator2
@decorator1
def function2decorate3(*args):
    print("function2decorate3(%r) called!" %([arg for arg in args]))


if __name__ == "__main__" :
    sep_line = lambda x: print("{0:=^100}".format(x))
    sep_line("Start")
    sep_line("Method")
    sample = SampleClass()
    sample.method2decorate("method_arg1", "method_arg2")
    sep_line("Function")
    function2decorate("function1", "function2")
    sep_line("Decorator with tags")
    function2decorate2("arg1", "arg2")
    sep_line("Stack Decorator")
    function2decorate3("stack_deco_arg1", "stack_deco_arg2")