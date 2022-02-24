"""
q08 문자열 재정열 page 322
문자는 오름차순 정열, 문자열 뒤에 숫자들의 합

예제 1: 
[input]
k1ka5cb7
[output]
ABCKK13

예제 2:
[Input]
AJSDLSI412K4JSJ9D
[output]
ADDIJJJKLSSS20
"""
def solution(array):
    array.sort()
    sum = 0
    result = ''
    for char in array:
        if '0' <= char <= '9':
            sum+=int(char)
        else:
            result+= char
    
    return result if sum == 0 else result+str(sum)

def main():
    array = list(input().upper())
    print(solution(array))

if __name__ == '__main__':
    main()