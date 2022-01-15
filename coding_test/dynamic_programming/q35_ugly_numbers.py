"""
못생긴 수 
Page 380
"""
from collections import deque

def solution(n):
    "약수가 2, 3, 5 인 n 번째 숫자"
    
    numbers = [1]

    checking_numbers = deque()
    checking_numbers.extend(numbers)
    
    while len(numbers)<=n:
        
        check_number = checking_numbers.popleft()
        
        for number in range(2,6):
            new_number = number * check_number
            
            if new_number not in numbers and new_number not in checking_numbers:
                numbers.append(new_number)
                checking_numbers.append(new_number)
                    
            
    return numbers[n-1]


def main():
    n = int(input())
    print(solution(n))

if __name__ == '__main__':
    main()