"""
정확한 순위
"""
def solution(scores):
    for k in range(len(scores)):
        for i in range(len(scores)):
            for j in range(len(scores)):
                scores[i][j] = (scores[i][k] and scores[k][j]) or scores[i][j]
    
    return scores

def main():
    n, c = map(int, input().split())
    scores = [[0]*n for _ in range(n)]
    answer = 0
    
    for i in range(n):
        scores[i][i] = 1
        
    for _ in range(c):
        i, j = map(int, input().split())
        scores[j-1][i-1] = 1
        
    for item in solution(scores):
        print(item)
        line+=1

    

if __name__ == '__main__':
    main()