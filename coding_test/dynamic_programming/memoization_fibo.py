def memoization_fibo(n): 
    # allocate n size array
    a = [0]*n 
    
    def fibo(n):
        if n < 1: 
            return -1
        
        if n == 1 or n == 2:
            return 1
        
        # allocate value when the value is not assigned.
        if a[n-1] == 0 :
             a[n-1] = fibo(n-1) + fibo(n-2) 
             
        return a[n-1]
        
    return fibo(n)

def bottom_up_fibo(n):
    if n < 1:
        return -1
    
    a = [0] * n
    a[0] = a[1] = 1
    
    for x in range(2,n):
        a[x] = a[x-1] + a[x-2]
        
    return a[n-1]
    
    
if __name__ == "__main__":
    print("top-down fibo:", memoization_fibo(10))
    print("memoization fibo:", bottom_up_fibo(10))