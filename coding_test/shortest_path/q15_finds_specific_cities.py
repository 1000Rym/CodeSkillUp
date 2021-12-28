""" 특정 도시 찾기 page 339
최단 도시가 K 인 노드를 오름차순으로 출력
case 1: 
[input]
4 4 2 1
1 2
1 3
2 3
2 4

[output] 
4

case 2: 
[input]
4 3 2 1
1 2
1 3
1 4
[output] 
-1

case 3: 
[input]
4 4 1 1
1 2
1 3
2 3
2 4
[output] 
2
3

"""
import heapq

INF = int(1e9)

def solution(graph, x, k):
    start = x-1
    dists = [INF] * len(graph)
    dists[start] = 0
    
    q = []
    heapq.heappush(q,(0, start))
    count = 1
    
    while q:
        rank, start = heapq.heappop(q)
        
        if rank >=  graph[node]: 
            continue 
        
        for end in graph[start]: 
            if dists[end] > rank + 1: 
                dists[end] = rank + 1
                heapq.heappush(q, (dists[end], end))
            
    return [node+1 for node in range(len(dists)) if dists[node] == k]
    

def main():
    n, m, k, x = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        start, end = map(int, input().split())
        graph[start-1].append(end-1)
    
        
    
    result = solution(graph, x, k)
    
    if result: 
        for item in result:
            print(item)
    else:
        print(-1)
    

if __name__ == '__main__':
    main()

