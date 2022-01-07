""" 퇴사 Page 377
"""

def solution(info):
    benifits = [0]*len(info)
    
    for i in range(len(info)):
        for j in range(i):
            day = info[j][0]
            pay = info[j][1]
 
            if i-j-day>=0: 
                benifits[i] = max(pay + benifits[j], benifits[i])
    
    return benifits
    
def main():
   n = int(input())
   info = []
   
   for _ in range(n):
        day, pay = map(int, input().split())
        info.append((day, pay))
    
   print(solution(info))
          

if __name__ == '__main__':
    main()
