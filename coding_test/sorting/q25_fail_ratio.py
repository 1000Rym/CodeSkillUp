""" 실패율 Page 361
"""
def solution(n, stages):
    ratios = []
    person_count = len(stages)
    result = []
    index = 0
    total_failed = 0
    for stage in range(1, n+1): 
        challenger = person_count - total_failed
        failed = stages.count(stage)
        ratio = failed/challenger if challenger >0 else 0
        total_failed += failed
        ratios.append((ratio, stage))
        
       
    while ratios:
        ratio, index = max(ratios, key=lambda x: x[0])
        ratios.remove((ratio, index))
        result.append(index)
        
    return result
        
        
def main():
    n1 = 5
    stages1 = [2,1,2,6,2,4,3,3]
    n2 = 4
    stages2= [4,4,4,4,4]
    
    print(solution(n1, stages1))
    print(solution(n2, stages2))


if __name__ == '__main__':
    main()