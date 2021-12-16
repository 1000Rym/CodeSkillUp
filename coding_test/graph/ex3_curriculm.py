"""
Curriculum (Topology Sort)
Page 303
[input]
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

[output]
10, 20, 14, 14, 17
"""
from collections import deque

INF = int(1e9)

def topology_sort(costs, graph, indegree):
    q = deque()
    
    results = [INF]*len(indegree)
    
    for i in range(1, len(indegree)):
        if indegree[i] == 0 :
            q.append(i)
            results[i] = costs[i]
            
    while q: 
        node = q.popleft()
        print(node)
        
        for i in graph[node]: 
            indegree[i]-=1
            results[i] = min(results[i], results[node]+costs[i])
            
            if indegree[i] == 0:
                q.append(i)
    
    print(results[1:])
    
    
def main():
    node_count = int(input())
    indegree = [0]* (node_count +1)
    costs = [0]* (node_count+1)
    graph = [[] for _ in range(node_count+1)]
    
    for i in range(1, node_count+1):
        values = list(map(int, input().split()))
        costs[i] = values[0]
        for node in values[1:-1]:
            indegree[i] += 1
            graph[node].append(i)
            
    topology_sort(costs, graph, indegree)
               
            
if __name__ == '__main__':
    main()