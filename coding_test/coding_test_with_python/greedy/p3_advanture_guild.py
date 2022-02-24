""" 모험가 길드(Page 506)

[I/O Description]
1. member count
2. list number of each member's fear degree
    - fear degree: the member can only join the group which have count of member>= fear degree.
result: maximum group count.

ex:
5
2 3 1 2 2

[output]
2
"""
def solution(member_fears):
    member_fears.sort(reverse=True)
    remain_fear = 0
    group_count = 0
    
    while member_fears: 
        remain_fear += 1
        
        if member_fears.pop() <= remain_fear: 
            remain_fear = 0
            group_count +=1
    
    return group_count
 
if __name__ == '__main__':
    _ = int(input())
    member_fears = list(map(int, input().split()))
    print('group count:', solution(member_fears))