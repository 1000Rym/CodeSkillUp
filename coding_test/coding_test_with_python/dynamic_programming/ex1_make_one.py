""" Make One
Input numbers can be operated by following if conditions fit: 
1. divide by 5
2. divide by 3
3. divide by 2
4. minus 1

Get minimum count
"""
def my_solution(n):
    numbers = {1,}
    
    for count in range(1, n+1):
        new_numbers = set()
        for element in numbers:
            new_numbers.add(element+1)
            new_numbers.add(element*2)
            new_numbers.add(element*3)
            new_numbers.add(element*5)
        
        if n in new_numbers:
            return count
        else:
            numbers.update(new_numbers)
    
    return count

def use_dynamic_programming_solution(n):
    a = [0] * (n +1)
    
    for i in range(2, n + 1):
        
        # case add one
        a[i] = a[i-1] + 1
        
        # case divide one
        if i%2 == 0 :
            a[i] = min(a[i], a[i//2] + 1)
        
        if i%3 == 0 :
           a[i] = min(a[i], a[i//3] + 1)
            
        if i%5 == 0 :
            a[i] = min(a[i], a[i//5] + 1)
            
    return a[n]
      
        
def main():
    n = int(input("input the count numbers:"))
    print(my_solution(n))
    print(use_dynamic_programming_solution(n))
    

    
if __name__ == '__main__':
    main()