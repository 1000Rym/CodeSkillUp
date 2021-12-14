"""dijkstra example
- input
1. node count, line count, start node. 
2-M: line info (start, end, cost)
- output
acceable node, maximum distance

[input]
3 2 1
1 2 4
1 3 2

[output]
2, 4

"""

import heapq

INF = int(1e9)

def dijkstra(start, graph):
    dists = [INF] * len(graph)
    q = []
    
    heapq.heappush(q, (0, start))
    dists[start] = 0
    
    while q: 
       dist, node = heapq.heappop(q)
       
       if dists[node] < dist:
           continue
       
       for end, distance  in graph[node]:
           new_dist = dists[node] + distance
   
           if new_dist < dists[end] :
               dists[end] = new_dist
               heapq.heappush(q, (new_dist, end))
        
    return dists
            
        


def main():
    node_count, line_count, start_node = map(int, input().split())
    graph = [[] for _ in range(node_count)]
    
    for i in range(line_count):
        start, end, cost = map(int, input().split())
        graph[start-1].append([end-1, cost])
            
    dists = dijkstra(start-1, graph)
    
    condition = lambda x: True if 0 < x < INF else False
    
    results = list(filter(condition, dists))
    print(len(results,max(results))
    
    
if __name__ == '__main__':
    main()