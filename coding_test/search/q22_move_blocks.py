"""
블록 이동하기 
[Input]
    board = [[0,0,0,1,1],[0,0,0,1,0],[0,1,0,1,1],[1,1,0,0,1],[0,0,0,0,0]]
[Output]
    7

"""

def get_next_move(current, board):
    directions= [(1,0),(-1,0),(0,1),(0,-1)]
    moves = []
    
    for direction in directions : 
        next_move = set()
        
        for leg in current: 
            h = leg[0] + direction[0] #horizental
            v = leg[1] + direction[1] #veritical
            
            if 0 <= h < len(board) and 0<=v<len(board):
                if board[v][h] == 0 : 
                    next_move.add((h,v))
        
        if len(next_move) == 2: 
            if next_move not in moves: 
                moves.append(next_move)
        
    return moves
    
def get_rotates (current, board):
    # Check the current coordinates (X, Y)
    rotates= []
    current = list(current)
    
    for leg in current:
        rotate = current[len(current)-current.index(leg)-1]

        if leg[0] == rotate[0]:  # if x the same
            rotates_x = [leg[0] +1,  leg[0]-1]
            
            for rotate_x in rotates_x: 
                if 0 <rotate_x <=len(board): 
                    if board[leg[1]][rotate_x] ==0 and board[rotate[1]][rotate_x] == 0: 
                        if (leg, (rotate_x, leg[1])) not in rotates:
                            rotates.append({leg, (rotate_x, leg[1])})
        else: 
            # Leg y eaqual
            rotates_y = [leg[1]+1, leg[1]-1]

            for rotate_y in rotates_y:
                if 0<=rotate_y<len(board):
                    if board[rotate_y][leg[0]] == 0 and board[rotate_y][rotate[0]]==0:
                        if (leg, (rotate_y, leg[0])) not in rotates:
                            rotates.append({leg, (leg[0], rotate_y)})
                    
    return rotates
                           
def print_board(board, current):
    show_board = [[] for _ in range(len(board))]

    for r in range(len(board)):
        for c in range(len(board)):
            if (c, r) in current: 
                show_board[r].append('X')
            else:
                show_board[r].append(str(board[r][c]))

    for info in show_board:
        print(info)
            

def solution(board):
    start = {(0,0),(1,0)}
    visited = []
    count = 0
    
    visited.append(start)
    
    while True:
        next_moves=[]
        for position in visited: 
            new_moves = get_next_move(position, board)
            new_rotates = get_rotates(position, board)
            
            for move in new_moves + new_rotates:
                if move not in visited:
                    next_moves.append(move)
                    
        if next_moves: 
            visited.extend(next_moves)
            count +=1
 
            if {(len(board)-2, len(board)-1),(len(board)-1, len(board)-1)} in next_moves:
                return count
        else:
            return -1
        
def test(board):
    current = {(2,4),(3,4)}
    print_board(board, current)
    
    
    for move in get_next_move(current, board):
        print(move)
        print_board(board, move)
    
    
      
def main():
    board = [[0,0,0,1,1],[0,0,0,1,0],[0,1,0,1,1],[1,1,0,0,1],[0,0,0,0,0]]
    print(solution(board))
    #test(board)
    
        
if __name__ == '__main__':
    main()