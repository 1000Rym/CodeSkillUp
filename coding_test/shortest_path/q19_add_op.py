"""
연산자 끼워 넣기 page 538
"""
from itertools import permutations

def solution(op_num_list, op_list):
    op_sets = permutations(op_list, len(op_list))
    results = []
    
    for op_set in op_sets: 
        result = op_num_list[0]
        for i in range(len(op_set)): 
            if op_set[i] == 0 : 
                result += op_num_list[i+1]
            elif op_set[i] == 1:
                result -= op_num_list[i+1]
            elif op_set[i] == 2:
                result *= op_num_list[i+1]
            else:
                result = int(result/op_num_list[i+1])
        results.append(result)
        
    return max(results), min(results)
                
    

def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    op_num_list = list(map(int, input().split()))
    op_list = []
    
    for i in range(4):
        op_list+= op_num_list[i] * [i]
    
    print(solution(numbers, op_list))
    
        
        

if __name__ == '__main__':
    main()