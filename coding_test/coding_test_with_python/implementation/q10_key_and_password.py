""" 
자물쇠와 열쇠 Page 325
"""
def rotate_key(key):
    rotated_key = [[0]*len(key) for _ in range(len(key))]
    
    for i in range(len(key)):
        for j in range(len(key)):
            rotated_key[i][j] = key[len(key)-1-j][i]
            
    return rotated_key

def is_key_fit(key, graph):
    for i in range(len(key),len(graph)-len(key)):
        for j in range (len(key),len(graph)-len(key)):
            if graph[i][j] != 1: 
                return False
    
    return True

            

def print_array(array):
    print()
    for value in array:
        print(value)
    

def solution(key, lock):    
    graph_len = 2*len(key) + len(lock)
    graph = [[0]*graph_len for _ in range(graph_len)]
    
    # init key
    for i in range(len(lock)):
        for j in range(len(lock)):
            graph[len(key)+i][len(key)+j] = lock[i][j]
            
    for _ in range(4):
        # check key
        for i in range(len(key)+len(lock)):
            for j in range(len(key)+len(lock)):
                for x in range(len(key)):
                    for y in range(len(key)):
                        graph[i+x][j+y] += key[x][y]
                        
                if is_key_fit(key, graph) :
                    return True
                else :
                    for x in range(len(key)):
                            for y in range(len(key)):
                                graph[i+x][j+y] -= key[x][y]
        key = rotate_key(key)
                
    return False
            
                 

def main():
    key = [[0,0,0],[1, 0, 0],[0,1,1]]
    lock = [[1,1,1],[1,1,0],[1,0,1]]
    
    print(solution(key, lock))

if __name__ == '__main__':
    main()