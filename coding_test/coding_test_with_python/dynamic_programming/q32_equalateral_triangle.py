"""
정삼각형 Page 566
[input]
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""

def solution(numbers):
    """
    result[i][j] = max(f[i-1][j-1], f[i][j-1]) + numbers[i][j]
    """
    
    result = [[0] * i for i in range(1, len(numbers)+1)]
    result[0][0] = numbers[0][0]
    
    for i in range(1, len(numbers)):
        for j in range(i+1):
            if j == 0 :
                result[i][j] = result[i-1][j] + numbers[i][j]
            elif j==i:
                result[i][j] = result[i-1][j-1] + numbers[i][j]
            else:
                result[i][j] = max(result[i-1][j-1], result[i-1][j]) + numbers[i][j]
    

    return max(result[len(numbers)-1])


def main():
    n = int(input())
    numbers = []

    for _ in range(n):
        values = list(map(int, input().split()))
        numbers.append(values)

    print(solution(numbers))
    


if __name__ == '__main__':
    main()