"""
곱하기 혹은 더하기
Get Maximum Value by using adding or multiply op(page 312)

[Input]
02984
[Output]
576

[Input]
567
[Output]
210
"""
def my_solution(numbers):
    result = numbers[0]
    for number in numbers[1:]: 
        result = result + number if result + number > result * number else result * number
    
    return result
        
def main():
    numbers = list(map(int, input()))
    print(my_solution(numbers))

if __name__ == '__main__':
    main()