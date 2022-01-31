""" 연구소  page 341
[input]
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

[output]
27

[input]
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
[output]
9

[input]
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
[output]
3

"""

from itertools import combinations
from copy import deepcopy

def get_empty_spaces(graph, pos_x, pos_y, n, m):
    empty_spaces = []
    
    directions = [(1,0),(-1, 0),(0,-1),(0,1)]
    
    for x, y in directions:
        check_pos_x = pos_x + x
        check_pos_y = pos_y + y
        
        if  0<=check_pos_x< n and 0 <= check_pos_y < m :
            if graph[check_pos_x][check_pos_y] == 0:
                empty_spaces.append((check_pos_x, check_pos_y))
    
    return empty_spaces

def get_virus_rooms(graph, n, m):
    virus_list = []
    
    for i in range(n): 
        for j in range(m):
            if graph[i][j] == 2 : 
                virus_list.append((i, j))
    
    return virus_list


def get_suggested_walls(graph, n, m):       
    return [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 0]

def get_clean_spaces(graph, n, m):
    virus_list = get_virus_rooms(graph, n, m)
    q = []
    count = 0
    
    for x, y in virus_list: 
        empty_spaces = get_empty_spaces(graph, x, y, n, m)
        q = q + empty_spaces if empty_spaces else q
        
    
    while q: 
        x, y = q.pop()
        graph[x][y] = 2
        empty_spaces = get_empty_spaces(graph, x, y, n, m)
        q = q + empty_spaces if empty_spaces else q
    
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count +=1      
  
    
    return count
    

def solution(graph, n, m):
    suggested_walls = get_suggested_walls(graph, n, m)
    clean_spaces = 0
    
    if len(suggested_walls) < 3:
        walls = combinations(suggested_walls, len(suggested_walls))
    else: 
        walls = combinations(suggested_walls, 3)
        

    for wall_info in walls:
        
        new_graph = deepcopy(graph)
        for x, y in wall_info:
            new_graph[x][y] = 1
        
        clean_spaces = max(clean_spaces, get_clean_spaces(new_graph, n, m))
    
    return clean_spaces

def main():
    n, m = map(int, input().split())
    graph = []
    
    for _ in range(n):
        map_row = list(map(int, input().split()))
        graph.append(map_row)
    
    print(solution(graph, n, m))

if __name__ == '__main__':
    main()