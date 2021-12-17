""" Advanture Guild
Page 506

[Input]
1. member count
2. fear degree

ex:
5
2 3 1 2 2

[output]
2
"""

def solution(array):
    array.sort(reverse=True)
    remain = 0
    result = 0
    
    while array: 
        remain += 1
        
        if remain >= array.pop(): 
            remain = 0
            result +=1
    
    return result
        


def my_solution(array):
    result = 0
    remain = 0
    
    while array:
        min_value = min(array)
        min_count = array.count(min_value)
        fightable = min_count + remain
        
        result += fightable // min_value
        remain += fightable % min_value
        
        array[:] = (value for value in array if value != min_value)
            
    return result
        
    
def main():
    member_count = int(input())
    array = list(map(int, input().split()))
    array2 = []
    array2 [:] = array
    print(my_solution(array))
    print(solution(array2))
    

if __name__ == '__main__':
    main()