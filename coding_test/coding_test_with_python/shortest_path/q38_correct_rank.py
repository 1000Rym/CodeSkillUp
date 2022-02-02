"""
정확한 순위 Page 387
[Input Data Description]
1st: Number of students, times of comparison.
2-n: comparison result.
[Output Data Description]
Number of students whose rank can be estimated.

[Input Data]
6 6
1 5
3 4
4 2
4 6
5 2
5 4

[Output Data]
1

"""
def solution(scores):
    for k in range(len(scores)):
        for i in range(len(scores)):
            for j in range(len(scores)):
                scores[i][j] = (scores[i][k] and scores[k][j]) or scores[i][j]
    
    return scores

def main():
    n, c = map(int, input().split())
    scores = [[False]*n for _ in range(n)]
    
    for i in range(n):
        scores[i][i] = True
        
    for _ in range(c):
        i, j = map(int, input().split())
        scores[i-1][j-1] = True
        
    for line in solution(scores):
        print(line)

if __name__ == '__main__':
    main()