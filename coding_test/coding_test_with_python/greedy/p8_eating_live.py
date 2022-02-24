"""
무지의 먹방 라이브
[I/O Description]
1. Amounts of the each food.
2. time
result: which food does eater eat after specific time

[Input]
3 1 2
5

[output]
1
"""

def solution(food_times, time):
    result = 0
    count = sum(food_times)
    
    while time:       
        if food_times[result] > 0: 
            food_times[result] -=1
            time -=1
    
        result = result + 1 if result < len(food_times)-1 else 0
        count -=1
        
        if count == 0 : 
            return -1
        
        
    return result+1
    

def main():
    food_times = list(map(int, input().split()))
    time = int(input())
    
    print(solution(food_times, time))

if __name__ == '__main__':
    main()