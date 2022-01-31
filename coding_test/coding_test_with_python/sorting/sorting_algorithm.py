"""
Review Sorting Algorithms
- Selection Sorts
- Quick Sorts
"""

def selection_sort(numbers):
    """ selection sort algoritm
    - complexity: always O(N²)
    """
    for i in range(len(numbers)):
        min_index = i
        for j in range(i+1, len(numbers)):
            if numbers[min_index] > numbers[j] :
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
        
    return numbers

def insertion_sort(numbers):
    """ insertion sort algorithm 
    - complexity: 
        - best: already sorted O(N)
        - worst: revserly sorted O(N²)
    """
    for i in range(1, len(numbers)):
        for j in range(i, 0, -1):
            if numbers[j] < numbers[j-1]:
                numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
            else: 
                break
    
    return numbers        


def quick_sort_simple(numbers):   
    """ 
    quick sort with list comperhension
    If some element larger than pivot in left side, else place it to pivots right side.
    """
    if len(numbers) > 1: 
        # Set the first index as pivot, comare remain elements.
        pivot = numbers[0]
        others = numbers[1:]
        
        # if the value is smaller than pivot set to left side, else set to right side.
        left_side = [x for x in others if x < pivot]
        right_side = [x for x in others if x >= pivot]   
        
        return quick_sort_simple(left_side) + [pivot] + quick_sort_simple(right_side)
    else:
        # If the lenght of numbers is smaller than 1, return the numbers
        return numbers
    
def quick_sort_origin(numbers, start, end):
    """
    quick sort with origitnal algorithm. 
    Set the pivot. 
    - divide the list as the two part(smaller than pivot, equal or bigger thant the pivot). 
    """
    def partition(numbers, start, end):
        """
        set the first index of element as pivot.
        if the number is smaller than pivot place to left side.
        """
        pivot_index = start
        pivot = numbers[pivot_index]
        
        while start < end: 
            while start < len(numbers) and numbers[start] <= pivot:
                start +=1
            while numbers[end] > pivot:
                end -=1
                
            # Start and end is crossed.
            if start>end: 
                numbers[pivot_index], numbers[end] = numbers[end], numbers[pivot_index]
            else:
                numbers[start], numbers[end] = numbers[end], numbers[start]
            
        return end
        
    if start < end: 
        p = partition(numbers, start, end)
        quick_sort_origin(numbers, start, p)
        quick_sort_origin(numbers, p+1, end)
        
def merge_sort(numbers):
    """
    Merge Sort
    - Divide the list as the left and right part(reculsively).
    - merge two left and right list.
        - find minimum from left and right list.
    """
    if len(numbers) > 1 : 
        mid = len(numbers)//2
        left = numbers[0: mid]
        right = numbers[mid:]

        merge_sort(left)
        merge_sort(right)
        
        # sort left = right
        numbers.clear()
                
        while left and right:
            if left[0] > right[0]:
                numbers.append(right[0])
                right.remove(right[0])
            else:
                numbers.append(left[0])
                left.remove(left[0])
        
        numbers.extend(left)
        numbers.extend(right)
    
    return numbers

def count_sort(numbers):
    """ 
    Count Sort : Keys between a specific range.
    1. Take a count array to store the count of each unique object.
    2. Modify the count array such that each element at each index stores the sum of previous counts.
    3. Rotate the array clockwise for one time.
    4. Output each object from the input sequence followed by increasing its count by 1.
    """
    
    # get the range of the numbers.
    min_num = int(min(numbers))
    max_num = int(max(numbers))
    range_of_nums = max_num - min_num
    
    # initialize the counter list.
    counter_list = [ 0 for _ in range(range_of_nums) ] 
    
    # add counter to each numbers.
    for number in numbers: 
        print(number-min_num)
        counter_list[number-min_num-1]+=1
        
    results = []
    
    for i in range(range_of_nums): 
        for _ in range(counter_list[min_num+i]):
            results.append(i+min_num)
            
    return results
 
                  
            
def main():
    numbers = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    print("selection sort:",selection_sort(numbers))
    numbers = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    print("insertion sort:",insertion_sort(numbers))
    numbers = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    print("quick sort simple:",quick_sort_simple(numbers))
    numbers = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    quick_sort_origin(numbers, 0, len(numbers)-1)
    print("quick sort with original algorithm:",numbers)
    numbers = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    print("merge sort algorithm:", merge_sort(numbers))
    numbers = [-5, -10, 0, -3, 8, 5, -1, 10]
    print("merge sort algorithm:", count_sort(numbers))

if __name__ == "__main__":
    main()