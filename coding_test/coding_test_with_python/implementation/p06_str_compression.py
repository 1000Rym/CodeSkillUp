""" 문자열 압축 페이지 323
[input-1]
aabbaccc
[output]
7
"""
def solution(array):
    max_count = len(array)//2 + 1
    results = []
    
    for step in range(1, max_count):
        count = 1
        prev = array[0: step]
        result = ""
        
        for index in range(step, len(array), step):
            if prev == array[index : index + step]: 
                count += 1
            else : 
                result += str(count) + prev if count > 1 else prev
                count = 1
            
            prev = array[index : index + step]
        
        result += str(count) + prev if count > 1 else prev
        results.append(result)
        
    return len(min(results, key=len))
                    

def main():
    array = input()
    print(solution(array))
    

if __name__ == '__main__':
    main()
