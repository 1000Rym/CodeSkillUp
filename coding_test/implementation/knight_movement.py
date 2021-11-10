position = input()
# x = 'abcdefgh'.index(position[0]) + 1
x = int(ord(position[0])-int(ord('a'))+1)
y = int(position[1])

movement=[(1,2),(1,-2),(-1, 2),(-1, -2),(2,1),(2,-1),(-2,1),(-2,-1)]

counter=0
for move_x, move_y in movement: 
    if(move_x + x >8 or move_x+x <1 or move_y +y >8 or move_y+y < 1):
        continue
    else:
        counter +=1  

print(counter)