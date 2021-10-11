# map size m_y, m_x
ms_y, ms_x = map(int, input().split())
# player position p_y, p_x, player direction p_d
p_y, p_x, p_d = map(int, input().split())

# map dict {(pos_y, pos_x):(map_info, history)}
map_dict = {}
history_dict = {}

# up, left, down, right
dx = [0,-1,0,1]
dy = [-1,0,1,0]

# receive map info
for y in range(ms_y): 
    map_info= list(map(int, input().split()))
    for x in range(len(map_info)):
        map_dict[(y,x)] = map_info[x] 
        history_dict[(y,x)] = map_info[x]


def check_stop_condition():
    global ms_x, ms_y
    global map_dict, history_dict
    for y in range(ms_y): 
        for x in range(ms_x):
            if history_dict[y,x] == 0: 
                return True
    return False

def turn_left():
    global p_d
    if p_d<3: p_d +=1
    else: p_d = 0


def check_forwardable(): 
    # direction = up, down, left right
    global map_dict, history_dict
    global ms_y, ms_x
    global p_y, p_x, p_d
    global dy, dx

    # if player is out of boundary
    if p_y + dy[p_d] <0 or p_y + dy[p_d] == ms_y or \
        p_x + dx[p_d] <0 or p_x + dx[p_d] == ms_x:
        return False
    
    if map_dict[(p_y+dy[p_d], p_x+dx[p_d])] == 1 or \
        history_dict[(p_y+dy[p_d], p_x+dx[p_d])] == 1: 
        return False
    else:
        return True

    

history_dict[(p_y,p_x)] = 1
forward_count = 1
try_count = 0

#2. while going condition is truth
while check_stop_condition():

    #2.1 if the forward is sea and history is visited go forward
    if check_forwardable():
        # move postion
        p_y = p_y+dy[p_d]
        p_x = p_x+dx[p_d]
        # record history
        history_dict[(p_y,p_x)] = 1
        forward_count +=1
        print("forward:",(p_y, p_x),p_d)
        try_count = 0
    #2.2. turn left max 4 times
    elif try_count < 3:
        try_count +=1
        turn_left()
        print("turn left", try_count)
    #2.3 go back
    else:
        try_count = 0
        p_y= p_y-dy[p_d]
        p_x =p_x-dx[p_d]
        print("go back")



print("map info:",ms_y, ms_x)
print("player info", p_y, p_x, p_d)
print(map_dict)
print("forward count:",forward_count)
