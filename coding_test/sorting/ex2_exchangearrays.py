"""
Exchange Arrays
- Input the exchange count K.
- Input two arrays array1 array2. 
- Exchange the elements of two arrays, make elements in array1's total value maximum.
- Print sum of each elements in array1.

[Input]
5 3
1 2 5 4 3
5 5 6 6 5

[Result]
26
"""

def input_values():
    n, k = map(int, input().split())
    array1 = list(map(int, input().split()))
    array2 = list(map(int, input().split()))
    
    return n, k, array1, array2
        
def solution(k, array1, array2):
    array1.sort()
    array2.sort(reverse = True)
    for i in range(k):
        array1[i], array2[i] = array2[i], array1[i]
    return sum(array1)

def main():
    n, k, array1, array2 = input_values()
    print(solution(k, array1, array2))
    
if __name__ == '__main__':
    main()