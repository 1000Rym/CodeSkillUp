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


def quick_sort(numbers):   
    """ quick sort
<<<<<<< HEAD
    If some element larger than pivot in left side, else place it to pivots right side.
=======
    If some element larger than pivot in left side
    exchange the element with right side element which larger than the left side. 
>>>>>>> ee06a0483a376a207bd3317cc1768fef50887fce
    """
    if len(numbers) > 1: 
        # Set the first index as pivot, comare remain elements.
        pivot = numbers[0]
        compare_set = numbers[1:]
        
        # if the value is smaller than pivot set to left side, else set to right side.
        left_side = [x for x in compare_set if x < pivot]
        right_side = [x for x in compare_set if x >= pivot]   
        
        return quick_sort(left_side) + [pivot] + quick_sort(right_side)
    else:
        # If the lenght of numbers is smaller than 1, return the numbers
        return numbers
    
            
def main():
    numbers = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    print("selection sort:",selection_sort(numbers))
    numbers = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    print("insertion sort:",insertion_sort(numbers))
    numbers = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    print("quick sort:",quick_sort(numbers))

if __name__ == "__main__":
    main()