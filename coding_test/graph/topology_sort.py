"""
Topology Sort

[input]
- 1. node count, edge count
- 2~M. connected info node1, node2
-ex: 
7 8 
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4

[output]
1 2 5 3 6 4 7
"""
from collections import deque

def topology_sort(graph, indegree):
    result = []
    q = deque()
    
    for i in range(1, len(indegree)):
        if indegree[i] == 0: 
            q.append(i)
    
    while q: 
        node = q.popleft()
        result.append(node)
        
        for new_node in graph[node]:
            indegree[new_node]-=1
            if indegree[new_node] == 0: 
                q.append(new_node)
    
    result_str = ""
    
    for node in result:
        result_str += str(node) + " "
    
    return result_str 
        

    

def main():
    node_count, edge_count = map(int, input().split())
    indegree = [0] * (node_count + 1)
    graph = [[] for _ in range(node_count+1)]
        
    for _ in range(edge_count):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        indegree[node2] +=1
        
    
    print(topology_sort(graph, indegree))
    

if __name__ == '__main__': 
    main()