""" Floyd Wallshall algorithm

D[ab] = min(D[ab], D[ak]+D[kb]

input data:
- node count, line count
    - loop line count 
        node1 node2 distance

output 
- loop nodes
    - loop nodes
        - print nodes to nodes distance

[input]
4 7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
"""
INF = int(1e9)

def floyd_wallshall_algorithm(graph):
    """
    Floyd Wallshall Algorithm: 
    D[ab] = min(D[ab], D[ak]+D[kb]
    """
    count = len(graph)
    for a in range(count):
        for b in range(count):
            for k in range(count):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b]) 
    
    return graph

def main():
    # Input User Data
    node_count, line_count = map(int, input().split())
    graph = [[INF]*node_count for _ in range(node_count)]
    
     # Same node distance should be 0 
    for node1 in range(node_count):
        for node2 in range(node_count):
            if node1 == node2 : 
                graph[node1][node2] = 0
                
    # input user data.
    for _ in range(line_count):
        node1, node2, distance = map(int, input().split())
        graph[node1-1][node2-1] = distance 
    
    for item in floyd_wallshall_algorithm(graph):
        print(item)
    

if __name__ == '__main__':
    main()