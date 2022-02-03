""" 어두운 길 Page 397
[Problem Description]
Light up dark road with minimum street lamp.

[Input Description]
1st: City Count, Edge Conut
2nd-P: City No1, City No2, Cost(lamp count) 

[Output Description]
minimum count of the lamp to light up all connection via cities.

{Case}
[Input]
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
[Output]
51
"""
import heapq

class Node:
    
    def __init__(self, number):
        self.number =  number
        self.parent = self
    
    def set_parent(self, parent):
        self.parent = parent
    
    def get_root(self):
        return self if self.parent is self else self.parent.get_root()
    
    def __repr__(self):
        return "{} <---> {} ".format(self.number, self.parent)
    
    def __gt__(self, other):
        return self.number > other.number
    

def main():
    node_count, edge_count = map(int, input().split())
    nodes = [Node(i) for i in range(node_count)]
    q = []
    total_cost = 0
    total = 0
    
    for _ in range(edge_count):
        node1, node2, cost = map(int, input().split())
        heapq.heappush(q, (cost, (node1, node2)))
        total += cost
    
    while q:
        cost, (node1, node2) = heapq.heappop(q)
        
        root1 = nodes[node1].get_root()
        root2 = nodes[node2].get_root()
        
        
        if root1 == root2:
            # There is a cycle between two nodes.
            continue
        elif root1 > root2 :
            root2.set_parent(root1)
        else:
            root1.set_parent(root2)
        
        total_cost += cost

    print("Total Cost:",  (total - total_cost))        

if __name__ == '__main__':
    main()