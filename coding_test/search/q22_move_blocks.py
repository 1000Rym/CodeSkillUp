"""
블록 이동하기 
"""

from copy import deepcopy

def get_next_move(current, board):
    directions= [(1,0),(-1,0),(0,1),(1,0)]
    moves = []
    
    for direction in directions : 
        next_move = set()
        
        for leg in current: 
            h = leg[0] + direction[0] #horizental
            v = leg[1] + direction[1] #veritical
            
            if 0 <= h < len(board) and 0<=v<len(board):
                if board[h][v] == 0 : 
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
                            rotates.append((leg, (rotate_x, leg[1])))
        else: 
            # Leg y eaqual
            rotates_y = [leg[1]+1, leg[1]-1]

            for rotate_y in rotates_y:
                if 0<=rotate_y<len(board):
                    if board[rotate_y][leg[0]] == 0 and board[rotate_y][rotate[0]]==0:
                        if (leg, (rotate_y, leg[0])) not in rotates:
                            rotates.append((leg, (leg[0], rotate_y)))
                    
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
    current = {(1,0),(0,0)}
    print_board(board, current)
    
    # next = get_next_move(current, board)
    rotates = get_rotates(current, board)
    
    for rotate in rotates :
        print("rotate:", rotate)
        print_board(board, rotate)

def main():
    board = [[0,0,0,1,1],[0,0,0,1,0],[0,1,0,1,1],[1,1,0,0,1],[0,0,0,0,0]]

    solution(board)
    
    print(board[0][3])
        
if __name__ == '__main__':
    main()