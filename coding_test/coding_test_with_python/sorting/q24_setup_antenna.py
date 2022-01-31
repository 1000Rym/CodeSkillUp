"""
안테나 설치 문제 page360
[input]
4
5 1 7 9
[output]
5

"""
INF = int(1e9)

def solution(homes):
    dist = INF
    result = -1
    
    for antenna in homes:
        temp = 0
        for home in homes:
            temp += abs(antenna-home)
        
        if temp < dist:
            dist = temp
            result = antenna
        
    return result
        

def main():
    n = int(input())
    homes = list(map(int, input().split()))
    print(solution(homes))

if __name__ == '__main__':
    main()