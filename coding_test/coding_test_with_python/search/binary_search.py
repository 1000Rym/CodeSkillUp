"""
Binary Search Algorithm
    
[input]
7
1 2 7 16 33 64 84

[output]
Found target  7
"""
def binary_search(target, array):
    """ 
    Binary search
    return target when found the value, otherwise return None.
    """
    start = 0
    end = len(array)
    
    while start <= end:
        mid = (start+end)//2
        
        if array[mid] == target: 
            return array[mid]
        elif array[mid] > target: 
            end = mid-1
        else:
            start = mid+1  
    return
    
if __name__ == '__main__':
    # Input target data
    target = int(input())
    array = list(map(int, input().split()))
    
    if binary_search(target, array):
        print('Found target ', target)
    else: 
        print('Target not found.')
