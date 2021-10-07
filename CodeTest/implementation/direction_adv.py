n = int(input())
directions_input = input().split()
directions = ['U', 'D', 'L', 'R']

# W, D, L, R
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

pos_x, pos_y = 1,1

for direction in directions_input:
    move = directions.index(direction)
    new_pos_x= pos_x+dx[move]
    new_pos_y= pos_y+dy[move]
    
    if new_pos_x < 1 or new_pos_x > n or new_pos_y <1 or new_pos_y > n :
        continue
    else: 
        pos_x, pos_y = new_pos_x, new_pos_y

print(pos_y, pos_x)
