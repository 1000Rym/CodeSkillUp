""" 
시각(page 113)
[I/O Description]
From 00:00:00 to N:59:59
1st: input time n
result: count of the time which contain 3

[input]
5

[output]
11475
"""
def solution(n):
    counter = 0 
    for hour in range(n + 1):
        for minute in range(60):
            for second in range(60):
                if '3' in f'{hour}{minute}{second}':
                    counter +=1
    return counter

if __name__ == '__main__':
    n = int(input())
    print(solution(n))

