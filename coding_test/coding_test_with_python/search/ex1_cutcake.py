"""
Cut Cake
- Find maximum Cut Weight
- OriginalCakes - CutWeight = CakesToOffer

[input]
4 6
19 15 10 17

[output]
15 
"""

def input_values():
    _ , m = map(int, input().split())
    array = list(map(int, input().split()))
    
    return m, sorted(array)

def solution(m, array):
    def cutted(h):
        c = lambda x, y : x-y if x>y else 0
        result = [ c(i, h) for i in array]
        
        return sum(result)
    
        
    start = 0
    end = max(array)
    
    while start <= end: 
       mid = (start + end)//2
       
       if cutted(mid) == m: 
           return mid
       elif cutted(mid) > m:
           start = mid +1
       else:
           end = mid-1
           
    return -1
    
def main():
    m, array = input_values()
    print(solution(m, array))

if __name__ == '__main__':
    main()    