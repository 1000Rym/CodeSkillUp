"""
Unmakable Money
[Input]
5
3 2 1 1 9
"""

def solution(coins):
    coins.sort()
    target = 1
    
    for coin in coins: 
        if target < coin: break
        else : 
            target += coin
            print(target)
    
    return target
        
    
def main():
    coin_count = int(input())
    coins = list(map(int, input().split()))
    print(solution(coins))

if __name__ == '__main__':
    main()