"""
플로이드 Page 574
[Input]
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4

[Output]
[0, 2, 3, 1, 4]
[12, 0, 15, 2, 5]
[8, 5, 0, 1, 1]
[10, 7, 13, 0, 3]
[7, 4, 10, 6, 0]

"""
INF = int(1e9)

def solution(graph):
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
    
    return graph
    

def main():
    n = int(input())
    graph = [[INF] * n for _ in range(n)]
    
    for i in range(n):
        graph[i][i] = 0
        
    edge = int(input())

    for _ in range(edge):
        i, j, c = map(int, input().split())
        graph[i-1][j-1] = min(c, graph[i-1][j-1])
        
        
    
    result = solution(graph)
    
    for item in result:
        print(item)
    

if __name__ == '__main__':
    main()