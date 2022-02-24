""" 
럭키 스트레이트
[I/O Description]
점수 자리수의 왼쪽 부분과 오른쪽 부분의 점수가 같을 경우 Lucky를 출력
아닐 경우, Ready를 출력

[input 1]
123402

[output]
LUCKY

[input 2]
7755

[output]
READY
"""

def solution(numbers):
    middle = len(numbers)//2
    
    return "LUCKY" if sum(numbers[:middle]) == sum(numbers[middle:]) else "READY"

def main():
    numbers = list(map(int, input()))
    print(solution(numbers))
    
    
if __name__ == '__main__':
    main()