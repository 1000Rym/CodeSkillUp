"""
상하좌우
[I/O description]
1st: Map size(NxN)
2nd: Direction Info
result: Final destination

[input]
5
R R R U D D
[output]
3 4 
"""
def solution(directions, map_size):
    direct_info = ['U', 'D', 'L', 'R']
    direct_vals = [(-1,0), (1,0),(0,-1),(0,1)]
    pos = (0,0)
    
    for direction in directions:
        index = direct_info.index(direction)
        new_x = pos[0] + direct_vals[index][0]
        new_y = pos[1] + direct_vals[index][1]
        pos = (new_x, new_y) if 0<= new_x < map_size and 0<=new_y< map_size else pos

    return f'{pos[0]+1} {pos[1]+1}'

if __name__ == '__main__':
    map_size = int(input())
    directions = input().split()
    print(solution(directions,map_size))
    