def sum(a, b):
    a =1
    print(id(a))
    return a 

if __name__ == '__main__':
    
    a =[2,3]
    b =[3,4] 
    value = sum(a,b)
    print(id(a))
    print(value)
    print(a)