"""
블록 이동하기 
"""
def solution(board):
    pos = (0,0)
    length = len(board)
    while pos == (length-1, length-1):
        break
    
    pass

def main():
    board = [[0,0,0,1,1],[0,0,0,1,0],[0,1,0,1,1],[1,1,0,0,1],[0,0,0,0,0]]
    solution(board)
        
if __name__ == '__main__':
    main()