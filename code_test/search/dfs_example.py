def dfs_search(graph, visited, current):
    visited[current] = True
    print(current, end=' ')

    for node in graph[current]:
        if not visited[node]: 
            dfs_search(graph, visited, node)
    
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
    dfs_search(graph_examle, visited, 1)

if __name__ == '__main__':
    main()
