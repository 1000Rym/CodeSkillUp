""" 
Prints Students Name From Lowest Score.
- Input students count : n
- From second row input Students Info(name and score): name score
- Print students name from lowest score.

[input]
2
홍길동 95
이순신 77

[output]
이순신 홍길동
"""
def input_values():
    n = int(input())
    students = dict()
    for _ in range(n): 
        name, score = input().split()
        students[name] = int(score)
    
    return students
        
    
def solution(students):
    results = ""
    for key, _ in sorted(students.items()):
        results += key + ' '
    
    return results
    

def main():
    students = input_values()
    print(solution(students))

if __name__ == '__main__':
    main()