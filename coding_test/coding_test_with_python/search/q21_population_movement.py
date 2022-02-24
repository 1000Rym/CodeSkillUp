"""
21 인구 이동 Page 353
[input]
2 20 50
50 30
20 40

[output]
1

[input]
2 40 50
50 30
20 40

[output]
0

[input]
3 5 10
10 15 20
20 30 25
40 22 10

[output]
2

[input]
4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10

[output]
3
"""
def get_movable_neigbours(graph, x, y,minimum, maximum,q):
    directions = [(-1,0),(1,0),(0,1),(0,-1)]
    
    for dx, dy in directions:
        nx = dx+x
        ny = dy+y
        
        if 0 <= nx < len(graph) and 0 <= ny <len(graph):
            if minimum <= abs(graph[x][y] - graph[nx][ny]) <= maximum :
                if (nx, ny) not in q: 
                    q.add((nx,ny))
                    get_movable_neigbours(graph, nx, ny, minimum, maximum, q)

def is_added_node(i, j, q):
    for item in q: 
        for x, y in item: 
            if (x,y) == (i,j):
                return True 
    
    return False
        
    


def solution(graph, minimum, maximum):
    count = 0
    
    while True: 
        q=[]
        for i in range(len(graph)):
            for j in range(len(graph)):
                if not is_added_node(i,j,q):            
                    neibour = set()
                    neibour.add((i, j))
                    get_movable_neigbours(graph, i, j, minimum, maximum, neibour)
                    if len(neibour) >1 : 
                        q.append(neibour)
         
        if q:
            for neibours in q:
                sum = 0
                for x, y in neibours:
                    sum += graph[x][y]
                
                avg = int(sum/len(neibours))
                
                for x, y in neibours:
                    graph[x][y] = avg
            
            count +=1
               
        else: 
            break
           
    return count         

def main():
    n, minimum, maximum = map(int, input().split())
    graph = []
    
    for _ in range(n):
       info = list(map(int, input().split()))
       graph.append(info)
    
    print(solution(graph, minimum, maximum))
    

if __name__ == '__main__':
    main()
