"""
큰 수의 법칙
Find Biggest number

[I/O Description]
1st: N M K: 
- N: The usable numbers count.
- M: Total numbers count.
- K: Maximum count of the number that can be sequentially used. 
2nd: numbers
result : sum of the result.

[input]
5 8 3
2 4 5 4 6

[output]
46
"""

def solution(m, k, data):
    data.sort(reverse=True)
    result = 0
    
    for count in range(m):
        result += data[1] if count % k == k-1 else data[0]
    
    return result

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))
    
    print(solution(m, k, data))