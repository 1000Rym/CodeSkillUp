"""
Balling Ball

[I/O description]
- The possibility that user can choose.

[Input]
5 3
1 3 2 3 2
[output]
8
"""

from itertools import combinations

def solution(balls):
    result = [(x,y) for x, y in list(combinations(balls, 2)) if x!=y]
    return len(result)  

def main():
    _, _ = map(int, input().split())
    balls = list(map(int, input().split()))
    print(solution(balls))
    

if __name__ == '__main__':
    main()