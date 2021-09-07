def factorial(number):
    '''n! = n*(n-1)*...*1'''
    return number*factorial(number-1) if number>2 else 2

if __name__ == '__main__':
    # Print the documents files.
    print(f"Test Factorial Function:{factorial.__doc__}")
    number = int(input('Please input factorial number:'))
    print(f"Result is {factorial(number)}")
    # Assign fucntion object to variable.
    fact = factorial
    # Using map to run multiple functions.
    a_list = list(map(fact, range(10)))
    print(a_list)

    