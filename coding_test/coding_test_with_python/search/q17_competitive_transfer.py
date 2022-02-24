"""
경쟁적 전염 Page 344
n: map size
k: virus kinds

[input]
3 3
1 0 2
0 0 0
3 0 0
2 3 2
[output]
3

[input]
3 3
1 0 2
0 0 0
3 0 0
1 2 2

[output]
0

"""

def is_empty_space_exist(graph):
    for i in range(len(graph)):
        for j in range(len(graph)): 
            if graph[i][j] == 0 :
                return True
    
    return False


def get_spread_block(graph, x, y, vk):
    directions = ((1,0),(-1,0),(0,1),(0,-1))
    blocks = []
    
    for dx, dy in directions:
        new_x = dx+x
        new_y = dy+y
        
        if  0<= new_x < len(graph) and 0<= new_y < len(graph):
            if graph[new_x][new_y] == 0 :
                blocks.append((new_x, new_y, vk))
        
    return blocks

            
def solution(graph, k, x, y, remain_count):
    while is_empty_space_exist(graph) and remain_count:
        spread = []
        for vk in range(1, k+1): 
            for i in range(len(graph)):
                for j in range(len(graph)):
                    if graph[i][j] == vk:
                        spread.extend(get_spread_block(graph, i, j, vk))
        
        for i, j, vk in spread:
            graph[i][j] = vk if graph[i][j] == 0 else graph[i][j]
                            
        remain_count-=1
    
    for i in range(len(graph)):
        print(graph[i])
                  
    
    return graph[x][y]
            


def main():
    n, k = map(int, input().split())
    graph = []
    
    for _ in range(n):
        line = list(map(int, input().split()))
        graph.append(line)
        
    s, x, y = map(int, input().split())
    
    print(solution(graph, k, x-1, y-1, s))
    

if __name__ == '__main__':
    main()