"""
만들수 없는 금액
[I/O Description]
1st: count of various of coins
2nd: value of the coins
result: minimum money that can not be makable.

[Input]
5
3 2 1 1 9

[output]
8
"""

def solution(coins):
    coins.sort()
    target = 1
    
    for coin in coins: 
        if target < coin: break
        else : 
            target += coin
    
    return target
        
    
def main():
    _ = int(input())
    coins = list(map(int, input().split()))
    print(solution(coins))

if __name__ == '__main__':
    main()