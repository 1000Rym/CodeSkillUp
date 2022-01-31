""" 공유기 설치 Page369
"""
from itertools import combinations
INF = int(1e9)

def solution(numbers, count):
    result = 0
    
    for routers in combinations(numbers, count):
        last_router = routers[0]
        dist = INF
        
        for router in routers[1:]:
            dist = min(dist, router-last_router)
            last_router = router     
        
        result = max(result, dist)
    
    return result


def main():
    n, c = map(int, input().split())
    numbers = []
    for _ in range(n):
        numbers.append(int(input()))
    
    numbers.sort()    
    
    print(solution(numbers, c))


if __name__ == '__main__':
    main()