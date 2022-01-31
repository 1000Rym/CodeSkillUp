""" 감시 피하기 Page 351
[Input]
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X

[Output]
True

[Input]
4
S S S T
X X X X
X X X X
T T T X

[Output]
False

"""
from itertools import combinations

WALL_COUNT = 3
def solution(teachers, students, spaces):
    wall_set = combinations(spaces, WALL_COUNT)
    
    for walls in wall_set: 
        blocks = []
        for s_x, s_y in students: 
            for t_x, t_y in teachers: 
                if s_x == t_x:
                    blocked = False
                    for _, w_y in walls: 
                        if  min((s_y, t_y)) < w_y < max((s_y,t_y)):
                            blocked = True
                    blocks.append(blocked)
                    
                if s_y == t_y:
                    blocked = False
                    for w_x, _ in walls: 
                        if  min((s_x, t_x)) < w_x < max((s_x,t_x)):
                            blocked = True
                    blocks.append(blocked)
                    
        if all(blocks) : return True
    
    return False
                    

def main():
    n = int(input())
    teachers = []
    students = []
    spaces = []
    
    
    for i in range(1, n+1):
        info = list(input().split())
        teachers += [(i,j) for j in range(len(info)) if info[j] == 'T']
        students += [(i,j) for j in range(len(info)) if info[j] == 'S']
        spaces += [(i,j) for j in range(len(info)) if info[j] == 'X']
    
    print(solution(teachers, students, spaces))
    
    

if __name__ == '__main__':
    main()