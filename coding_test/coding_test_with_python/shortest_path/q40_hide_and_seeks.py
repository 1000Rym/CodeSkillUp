"""
Quiz 숨바꼭질 Page 390
[Problem Description]
- Hider can be hide in any place around location 1~N
- Seeker try to find hider from location 1. 
- Hider hide in farthest postion from location 1.
- Find the way to farthest postionn

[Input Description]
- 1st: Location N, Direction M
- 2nd - M+1 line: The direction between two postion.

[Output Description]
- 1st num: The Hidden Position(Shortest Number when value is equal)
- 2nd num: The distance of the target hidden postion.
- 3rd num: The count of the postions which have equal distance with shortest distance.

[Input]
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2

[output]
4 2 3
"""
import heapq

INF = int(1e9)

def solution(map_info, n):
    distance_info = [0]+[INF]*(n-1)
    start_node = 0
    q=[]
    heapq.heappush(q, (0, start_node))    
    
    while q:
        rank, pos = heapq.heappop(q)
        
        for node in map_info[pos]:
            new_rank = rank + 1
            
            if new_rank < distance_info[node] :
                distance_info[node] = new_rank
                heapq.heappush(q,(new_rank, node))
                
    

    max_dist = max([node for node in distance_info if node != INF])
    target_node = distance_info.index(max_dist) + 1
    max_count = distance_info.count(max_dist)
    
    return f"{target_node} {max_dist} {max_count}" 
    

def main():
    # Assume that n is node, m is edge.
    n, m = map(int, input().split())
    
    map_info = [[] for _ in range(n)]
    
    for _ in range(m):
        start, end = map(int, input().split())
        map_info[start-1].append(end-1)
        map_info[end-1].append(start-1)
        
    print(solution(map_info, n))            

if __name__ == '__main__':
    main()