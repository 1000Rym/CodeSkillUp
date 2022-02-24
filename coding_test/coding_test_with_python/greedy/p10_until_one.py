"""
1이 될때까지 
[I/O description]
repeat minus one, or divide process until result is 1.
1st: number devided number
result: count
"""
def solution(N, K):
    count = 0
    count  += N%K 
    while N > 1: 
        N//=K
        count +=1
    
    return count

if __name__ == '__main__':
    N, K =  map(int, input().split())
    print(solution(N, K))