"""
거스름 돈 
Assume that there coins in 500$, 100$ 50$, 10$. How to return minimum coins.

[input]
1260

[output]
6
"""
def return_coins(remain): 
    """Return 500$, 100$, 50$, 10$ with minimum count"""
    count = 0
    reduce_list = [500, 100, 50, 10]

    for coin in reduce_list: 
        count += remain//coin
        remain %= coin
    
    return count 
    
if __name__ == '__main__':
    print("Minimum coin count is ", return_coins(1260))