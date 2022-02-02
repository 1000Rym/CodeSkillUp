""" 여행 계획
Get the possibility that traveller can travel the target positions.
[Input Description]
1st:  Number of the cities, Count of the connections between the city.
2-n:  N by N info that indicates cities connection
last: travling plans.

[Output Description]
Results of the traveller can travel target cites.

[Input]
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0 
1 0 0 0 0
2 3 4 3

[Output]
YES
"""

def solution(n, map_info, targets):
    graph_info = [[False]*n for _ in range(n)]
    
    for i in range(n):
        graph_info[i][i] = True
    
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph_info[i][j] = (map_info[i][k] and map_info[k][j]) or map_info[i][j]
                

    source = targets[0]
    destinations = targets[1:]
    
    result = True
    for target in destinations:
        result &= graph_info[source-1][target-1]
        
        
    print(graph_info[source-1])
    
    return result      
    

def main():
    n, _ = map(int, input().split())
    map_info = []
    
    for _ in range(n):
        line_info = list(map(int,input().split()))
        map_info.append(line_info)
    
    targets = list(map(int, input().split()))
    
    result =  "YES" if solution(n, map_info, targets) else "NO"
    print(result)
    

if __name__ == '__main__':
    main()