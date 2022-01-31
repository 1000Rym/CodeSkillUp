""" 
[Descriptionß]
Starts from the node 1, find the shortest path across x to k.

Input
1. Node count, Line count. 
2~M. Map Info.
M+1. middle node, final node.

Output shortest cost. 

[Input]
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
"""

INF = int(1e9)

def floyd_wallshall(graph):
    for a in range(len(graph)): 
        for b in range(len(graph)):
            for k in range(len(graph)):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
                
    return graph

def main():
    node_count, line_count = map(int, input().split())
    graph = [[INF] * node_count for _ in range(node_count)]
    
    for node in range(node_count):
        graph[node][node] = 0
    
    for _ in range(line_count):
        start, end = map(int, input().split())
        graph[start-1][end-1] = 1
        graph[end-1][start-1] = 1
    
    end, middle = map(int, input().split())
    graph = floyd_wallshall(graph)
    
    distance = graph[0][middle-1]+graph[middle-1][end-1]
    
    for i in range(len(graph)):
        print(graph[i])
    
    if distance == INF: 
        print(-1)
    else:
        print(distance)
    
    
if __name__ == '__main__':
    main()