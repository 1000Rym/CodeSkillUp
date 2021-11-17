"""Escape the maze
Escape from the maze map N*M
- If the block is accessable 1, 
- Else inaccessable 0.
- Start from (1,1) Escape to (N, M)
"""

from collections import deque

def input_value():
    """ Input value. 
    - First input value is map size: N M
    - From second row input the map_info.
    """
    N,M = map(int, input().split())
    map_info = list()
    
    for _ in range(N):
        map_info.append(list(map(int, input())))
    
    return N, M, map_info

def is_visitable_new_node(pos_x, pos_y, N, M,map_info):
    """If visitable return True(1), else return False(0)."""
    if pos_x == 0 and pos_y == 0:
        return False
    elif  0<= pos_x < N and 0 <= pos_y < M: 
        return True if map_info[pos_x][pos_y] == 1 else False
    else: 
        return False
    
    
def escape_maze(N,M,map_info):
    """Using BFS Algorithm"""
    to_visit_nodes = deque([(0, 0)]) 
    depth_count = 0
    
    # up, down, left, right
    dx = [ 0, 0, -1, 1 ]
    dy = [ -1, 1, 0, 0 ]
    
    while to_visit_nodes :
        pos_x, pos_y = to_visit_nodes.popleft()
        depth_count +=1
        for index in range(4):
            to_x, to_y = pos_x+dx[index], pos_y+dy[index]
            if is_visitable_new_node(to_x, to_y, N, M, map_info): 
                to_visit_nodes.append((to_x,to_y))
                map_info[to_x][to_y] = map_info[pos_x][pos_y] +1
    
    return map_info[N-1][M-1]
    


def main():
    N, M, map_info = input_value()
    escape_maze(N, M, map_info)
    

if __name__ == '__main__':
    main()
