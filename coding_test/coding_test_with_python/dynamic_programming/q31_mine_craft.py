"""
금광 Page 375

[input]
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""
def solution(mines):
    row = len(mines)
    column = 0 if row <= 0 else len(mines[0])    
    craft = [[0]*column for _ in range(row)]

    for j in range(column):
        for i in range(row):    
            if j-1 < 0: 
                up_left = 0
                down_left = 0
                left = 0
            else:
                left = craft[i][j-1]
                
                if i-1 < 0:
                    up_left = 0
                else:
                    up_left = craft[i-1][j-1]
                
                if i+1 >= row:
                    down_left = 0
                else:
                    down_left = craft[i+1][j-1]
                          
                
            craft[i][j] = max(up_left, down_left, left) + mines[i][j]
    
    return max([craft[i][j] for i in range(row) for j in range(column)])    
          

def main():
    cases = int(input())
    results = []
    for _ in range(cases):
        n, m = map(int, input().split())
        numbers = list(map(int, input().split()))
        mines = [[0]*m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                mines[i][j] = numbers[m*i +j]
       
        results.append(solution(mines))
        
    for result in results:
        print(result)
    
if __name__ == '__main__':
    main()