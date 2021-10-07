#Start 18:40 Finished in 19:00

pos_x = 1
pos_y = 1

max_bound =  int(input())
directions = input().split()

for direction in directions: 
    if direction == 'D':
        if pos_y < max_bound : pos_y += 1 
    elif direction == 'U':
        if pos_y > 1: pos_y -= 1 
    elif direction == 'R':
        if pos_x < max_bound: pos_x +=1 
    elif direction ==  'L':
        if pos_x > 1: pos_x -=1 
    else :
        print("Input error")

print(pos_y, pos_x)