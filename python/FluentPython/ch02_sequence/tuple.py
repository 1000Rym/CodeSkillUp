from collections import namedtuple

def tuple_as_recorder():
    print("Test tuple as the record.")
    user_info = [('woody', 31), ('airin', 30), ('tom', 28)]

    for user in user_info:
        print('name: %s, age: %d' %user) # % can automatically understand the tuple.

def tuple_unpacking():
    print("Test tuple unpacking")
    params = 20, 3
    div, mod = divmod(*params) # add '*' to unpacking the tuples.
    print(f"divmod{params} div={div}, mod ={mod}") 

def named_tuple_print():
    UserInfo = namedtuple('UserInfo', ['name','age','phone_number'])
    lin = UserInfo("Woody", 31, '010-6705-0724')
    print(f"Woody's name is {lin.name}, and his age is {lin[1]}") # use two way to print named tuple


if __name__ == '__main__':
    tuple_as_recorder()
    tuple_unpacking()
    named_tuple_print()
