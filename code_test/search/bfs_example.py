from collections import deque

def bfs_search(graph, visited, start):
    to_visit = deque([start])

    while to_visit: 
        visited_node = to_visit.popleft()
        visited[visited_node] = True
        print(visited_node, end = ' ')

        for node in graph[visited_node]:
            if not visited[node]:
                to_visit.append(node) 

    
def main():
    graph_examle = [
        [],
        [2,3,8],
        [1,7],
        [4,5],
        [3,5],
        [3,4], 
        [7],
        [2,6,8],
        [1,7]
    ]
    
    visited = [False] * 9
    bfs_search(graph_examle, visited, 1)

if __name__ == '__main__':
    main()