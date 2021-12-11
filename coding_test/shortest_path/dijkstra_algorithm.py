"""
Dijkstra Algorithm

[Description]
- input:
    - node counts, line counts
    - start node
    - graph info

- output: 
    each distance to node.
    
[input]
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

[output]
0, 2, 3, 1, 2, 4
"""
import heapq

INF = int(1e9)
        
def dijkstra_origin(graph, start_node, distance_info, visited_info):
    
    def find_shortest_node():
        min_node = 0
        
        for i in range(1, len(distance_info)):
            if visited_info[i] == False and distance_info[i] < distance_info[min_node]: 
                min_node = i
        
        return min_node
       
               
    visited_info[start_node] = True
    distance_info[start_node] = 0
    
    # Update start node info
    for node, distance in graph[start_node]:
        distance_info[node] = distance
    
    while (new_node:=find_shortest_node()):
        visited_info[new_node] = True
        for node, distance in graph[new_node]: 
            if distance + distance_info[new_node] < distance_info[node]: 
                distance_info[node] = distance + distance_info[new_node]
    
    return distance_info[1:]

def advanced_dijkstra(graph, start_node, distance_info):
    # Advanced dijecstra will use heapq instead of find_shortest_node
    q = []
    heapq.heappush(q, (start_node, 0))
    
    while q: 
        distance, now = heapq.heappop(q)
        
        if distance > graph[now] :
            continue
        
        for node, dis in graph[now]:
            cost = dis + distance
            
            if cost < distance_info[node]:
                distance_info[node] = cost
                heapq.heappush(q, (cost, node))
                
        return distance_info[1:]
                
            
def main():
    node_num, line_num = map(int, input().split())
    start_node = int(input())
    graph = [[] for _ in range(node_num+1)]
    distance_info = [INF] * (node_num+1)
    visited_info = [False] * (node_num+1)
    
    # input the map
    for _ in range(line_num):
        start, end, distance = map(int, input().split())
        graph[start].append((end, distance))
        
    #print(graph)
    print(dijkstra_origin(graph, start_node, distance_info, visited_info))
    print(advanced_dijkstra(graph, start_node, distance_info))
    

if __name__ == '__main__':
    main()