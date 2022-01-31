"""
Steal Food from the ants food garage. 
Foods stores in each index. 
{1,3,5,6,9}
1. Can be detacted by ants warrior if steal from the neighbor of stealed index. 
2. Get maximum, some of the food amounts. 

[Input]
4
1 3 1 5

[output]
8

"""
def solution(n, array):
    """
    Use recurrence relation
    a[i] = max(a[i-1], a[i-2]+k)
    """
    # preallocation memory size. 
    a = [0] * n
    a[0] = array[0]
    a[1] = max(array[0], array[1])
    
    for i in range(2, n) :
        a[i] = max(a[i-2]+array[i], a[i-1])
        
    
    return a[i]
    

def main():
    n = int(input())
    array = list(map(int, input().split())) 
    solution(n, array)

if __name__ == '__main__':
    main()