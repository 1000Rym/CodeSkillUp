""" 정렬된 배열에서 특정 수의 개수 구하기
Time Require: O(logN)
[input]
7 2
1 1 2 2 2 2 3
[output]
4

[input]
7 4
1 1 2 2 2 2 3
[output]
-1
"""

def first_number_index(numbers, number, start, end):
   
    if start > end: 
        return None
    
    mid = (start + end)//2
    
    if (mid == 0 or numbers[mid-1] < number) and numbers[mid] == number: 
        return mid
    elif numbers[mid] >= number:
        return first_number_index(numbers, number, 0, mid-1)
    else:
        return first_number_index(numbers, number, mid+1, end)
    
    
def last_number_index(numbers, number, start, end):
    
    if start > end : 
        return None
    
    mid = (start + end) // 2
    
    if (mid == end -1 or numbers[mid+1] > number) and numbers[mid] == number:
        return mid
    elif numbers[mid] > number:
        return last_number_index(numbers, number, start, mid-1)
    else :
        return last_number_index(numbers, number, mid+1, end)

def solution(numbers, number, count):
    
    first = first_number_index(numbers, number, 0, count-1)
    
    if first == None:
        return 0
    else:
        last = last_number_index(numbers, number, 0, count-1)
        
        return last-first +1
    

def main():
    count, number = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(solution(numbers, number, count))

if __name__ == '__main__' :
    main()