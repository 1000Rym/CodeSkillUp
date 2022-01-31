"""
화성 탐사 Page 388
[Description]
- Find shortest energy cost from source to destination from N*N map.

[Input Description]
1st line: Count of Testcase.
2nd line: Size N in N by N map.
3rd to N+3: map info.

[input]
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4

[output]
20
19
36
"""

import heapq
INF = int(1e9)

def find_nearby_positions(pos, n):
    """Find nearby pos"""
    nearby_list = []
    x, y = pos[0], pos[1]
     
    if  x + 1 < n :
        nearby_list.append((x+1, y))
    if  x-1 >=0:
        nearby_list.append((x-1, y))
    if  y +1 < n : 
        nearby_list.append((x, y+1))
    if  y -1 >= 0:
        nearby_list.append((x, y-1))
        
    return nearby_list     
         

def solution(n, map_info):
    """ Dijkstra Algorithm
    To solove this problem, we use dijkstra algorithm.
    - INF the All maps.
    - Push the item to heapq which is smaller than current item.
    - Finish until the q is empty.
    
    """
    start = (0, 0)
    graph_info = [[INF] * n for _ in range(n)]
    q = []
    
    heapq.heappush(q, (map_info[start[0]][start[1]], start))
    
    while q:
        rank, pos = heapq.heappop(q)
        nearby_list= find_nearby_positions(pos, n)
        
        for x, y in nearby_list:
            new_rank = rank + map_info[x][y]
            
            if new_rank < graph_info[x][y]: 
                graph_info[x][y] = new_rank
                heapq.heappush(q, (new_rank, (x, y)))
    
    return graph_info[n-1][n-1]
          

def main():
    case_count = int(input())
    answers = []
    
    for _ in range(case_count):
        n = int(input())
        
        map_info = []
        for _ in range(n):
            line_info = list(map(int, input().split()))
            map_info.append(line_info)
        answers.append(solution(n, map_info))
        
    for answer in answers: 
        print(answer)
    
    
if __name__ == '__main__':
    main()