"""
ex1: Sort Top to bottom. 
- Input number N.
- Input numbers.
- Sort the numbers.

[input]
3
15
27
12

[output]
27 15 12
"""

def input_values():
    N = int(input())
    numbers = []
    for _ in range(N):
        numbers.append(int(input()))
    
    return N, numbers

def solution(numbers):
    array = sorted(numbers, reverse = True)
    results = ""
    for number in array:
        results += str(number) + ' '
    return results
    
def main():
    N, numbers = input_values()
    print(solution(numbers))

if __name__ == '__main__':
    main()