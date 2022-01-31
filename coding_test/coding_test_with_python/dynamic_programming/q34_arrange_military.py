""" 군사배치하기 Page380
"""
        

def solution(members):
    """
    f[i] = max(f[i], f[j]+1) if member[i]<member[j]
    """
    f = [1]*len(members)
    
    for i in range(1,len(members)):
        for j in range(0, len(members)):
            if members[j]>members[i]:
                f[i] = max(f[i], f[j]+1) 
    
    return len(members)-max(f)

def main():
    n = int(input())
    
    members = list(map(int, input().split()))
        
    print(solution(members))

if __name__ == '__main__':
    main()