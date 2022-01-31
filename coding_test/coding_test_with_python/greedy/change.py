def return_coins(remain): 
    """Return 500$, 100$, 50$, 10$ with minimum count"""
    count = 0
    reduce_list = [500, 100, 50, 10]

    for coin in reduce_list: 
        count += remain//coin
        remain %= coin
    
    return count 
    
if __name__ == '__main__':
    print("Count is ", return_coins(1260))