"""
Page 322 Chiken Delivery
"""
from itertools import combinations
INF = int(1e9)

def get_min_dist(houses, shops):
    total = 0
    for house in houses:
        shortest_dist = INF
        for shop in shops: 
            shortest_dist = min(shortest_dist, abs(shop[0]-house[0]) + abs(shop[1]-house[1]))
        total += shortest_dist
    return total
        

def solution(shops, houses, count):
    shop_set = combinations(shops, count)
    result = INF
    
    for shops in shop_set:
        new_dist = get_min_dist(houses, shops)
        result = new_dist if result> new_dist else result
        
    return result
            

def main():
    N, count = map(int, input().split())
    shops = []
    houses = []
    
    for i in range(N):
        info = list(map(int, input().split()))
                    
        for j in range(len(info)):
            if info[j] == 1:
                houses.append((i, j))
            elif info[j] == 2:
                shops.append((i, j))
                
    print(solution(shops, houses, count))
    
    
if __name__ == '__main__':
    main()