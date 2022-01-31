"""
Balling Ball

example 1:
[Input]
5 3
1 3 2 3 2
[output]
8
"""

def my_solution(balls):
    result = set()
    balls.sort()
    
    for i in range(len(balls)):
        for j in range(i+1, len(balls)):
            if balls[i] != balls[j]:
                result.add((i, j))

    return len(result)
    
    

def main():
    count, kinds = map(int, input().split())
    balls = list(map(int, input().split()))
    
    print(my_solution(balls))
    

if __name__ == '__main__':
    main()