"""
City Division (Page300)

Divide city to shortest path.
- Using Kruscal Algorithm
- Remove Longest edge from the total

[input]
1: node count, edge count
2-M: node1, node2 distance

7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4


[output]
shortest distance


"""
import heapq

class Node:
    def __init__(self, number):
        self.number = number
        self.parent = self
        
    def __gt__(self, other):
        return self.number > other.number
    
    def set_parent(self, other):
        self.parent = other
        
    def get_root(self):
        return self if self.parent is self else self.parent.get_root()
    
    def __repr__(self):
        return '{}'.format(self.number)
    

def check_cycle(node1, node2):
    return node1.get_root() is node2.get_root()

def unite_nodes(node1, node2):
    root1 = node1.get_root()
    root2 = node2.get_root()
    
    if root1 > root2: 
        root1.set_parent(root2)
    else:
        root2.set_parent(root1)
        


def main(): 
    node_count, edge_count = map(int, input().split())
    nodes = []
    q = []
    dists = []
    
    for i in range(node_count+1):
        nodes.append(Node(i))
    
    for _ in range(edge_count):
        node1, node2, dist = map(int, input().split())
        heapq.heappush(q,(dist, (node1, node2)))
    
    while q:
        dist, (node1, node2) = heapq.heappop(q)
        
        if check_cycle(nodes[node1], nodes[node2]) :
            continue
        else:
            unite_nodes(nodes[node1], nodes[node2])
            dists.append(dist)
            
    
    dists.remove(max(dists))
    print(sum(dists))
            
            
if __name__ == '__main__':
    main()