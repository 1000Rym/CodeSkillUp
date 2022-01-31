""" 외벽 점검 page 336
case 1: 
weak_walls = [1, 3, 4, 9, 10]
friends_dist = [3, 5, 7]

result : 1
---
case 2: 
weak_walls = [1, 5, 6, 10]
friends_dist = [1, 2, 3, 4]

"""
from itertools import permutations

def solution(n, weak_walls, friends_dist):
    weak_double = weak_walls + [ n + wall for wall in weak_walls ]
    result = len(friends_dist) + 1
    
    for start in range(len(weak_walls)): 
        for friends in permutations(friends_dist, len(friends_dist)):
            pos_index = start
            friend_index = 0
            friend_start = start
            
            while pos_index < start + len(weak_walls) -1 : 
                next_pos = pos_index + 1
                
                if weak_double[friend_start] + friends[friend_index] < weak_double[next_pos]:                    
                    friend_start = next_pos
                    friend_index += 1
                    
                    if friend_index >= len(friends_dist):
                        friend_index = -1
                
                pos_index = next_pos
                
            print((friend_index + 1), friends, start)
            result = min(result, (friend_index + 1)) if friend_index != -1 else result
                    
        
    return result if len(friends_dist) + 1 else -1
                   
   

def main():
    n = 12
    weak_walls = [1, 3, 4, 9, 10]
    friends_dist = [3, 5, 7]
    print(solution(n, weak_walls, friends_dist))

if __name__ == '__main__':
    main()


