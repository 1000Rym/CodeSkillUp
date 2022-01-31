""" 
고정점 찾기 Page 368

[case 1 input]
5
-15 -6 1 3 7

[output]
3

[case 2 input]
7
-15 -4 2 8 9 13 15
[output]
2

[case 3 input]
7
-15 -4 -3 8 9 13 15
[output]
-1


"""
def solution(numbers, start, end):
    if start > end: 
        return -1
    
    mid = (start + end)//2
    
    if numbers[mid] == mid:
        return mid
    elif numbers[mid] > mid: 
        return solution(numbers, 0 , mid-1)
    else:
        return solution(numbers, mid+1, end)

def main():
    count = int(input())
    numbers = list(map(int, input().split()))
    
    
    print(solution(numbers,0,count))

if __name__ == '__main__':
    main()