""" 자물쇠와 열쇠 Page 325
"""
def rotate_key(key):
    rotated_key = [[0]*len(key) for in range(len(key))]
    for i in range(key_len):
        for j in range(key_len):
            rerotated_key[j][i] = key[i][j]
            
    return rotated_key

def is_key_fit():
    pass

def solution(key, lock):    
    graph_len = 2*len(key) + len(lock)
    graph = [[0]*graph_len for _ in range(graph_len)]
    
    for i in range(len(lock)):
        for j in range(len(lock)):
            graph[len(key)+i][len(key)+j] = lock[i][j]
            
  
    
                 
                
            
    


def main():
    key = [[0,0,0],[1, 0, 0],[0,1,1]]
    lock = [[1,1,1],[1,1,0],[1,0,1]]
    
    solution(key, lock)

if __name__ == '__main__':
    main()