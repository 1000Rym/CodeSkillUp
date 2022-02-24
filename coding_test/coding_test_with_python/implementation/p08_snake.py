"""
뱀 문제
[입력]
1. 보드 길이(정사각형) N
2. 사과 개수 K
3~K, 사과 좌표
K+1, 뱀 방향 개수
K+1 ~ end. 시간 및 방향 정보(L)은 왼쪽, D는 오른쪽
[출력]
생존시간

예제 1: 
input:
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
output :
9

예제2:
input: 
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L

output:
21

예제3:
10
5
1 5
1 3
1 2
1 7
1 6
4
8 D
10 D
11 D
13 L

output
13

"""
from collections import deque
        
def change_direct(direct, direct_info):
    # direct 0 left, 1, down, 2, right, up 3
    if direct_info  == 'D' :
        return direct + 1 if direct <3 else 0 
    else : # 'L'
        return direct -1 if direct >0 else 3
        
        
def get_new_step(pos, direct):
    pos_x = [1, 0, -1, 0]
    pos_y = [0, 1, 0, -1]
    
    return pos[0] + pos_x[direct],  pos[1]+pos_y[direct]

        
def is_new_pos_valid(new_pos, snake, map_size):
    return 0<= new_pos[0] < map_size and 0<= new_pos[1] < map_size and new_pos not in snake
            
     

def solution(apples, directions, map_size):
    total_time = 0
    snake = deque()
    current = (0,0)
    snake.append((current))
    curr_direct = 0
    
    time, direct_info = directions.popleft()
    
    while True:      
        new_pos = get_new_step(current, curr_direct)
        total_time +=1
        
        print("time", total_time, "new_pos", new_pos, ",snake", snake, "apples", apples)
        
        
        if is_new_pos_valid(new_pos, snake, map_size):
            snake.append(new_pos)
            current = new_pos
            
            if new_pos in apples:
                apples.remove(new_pos)
            else:
                snake.popleft()
        else:
            break
        
        if total_time == time: 
            curr_direct = change_direct(curr_direct, direct_info)
            if directions: 
                time, direct_info = directions.popleft()
    
    return total_time
            
    

def main():
    N = int(input())
    K = int(input())
    
    apples = []
    directions = deque()
    
    for _ in range(K):
        x,y = map(int, input().split())
        apples.append((y-1,x-1))

    direction_count = int(input())
    
    for _ in range(direction_count):
        time, direction = input().split()
        directions.append((int(time), direction))
        
    print(solution(apples, directions, N))
    
    
    
if __name__ == '__main__':
    main()