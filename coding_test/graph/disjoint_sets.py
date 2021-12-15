"""
공통 원소가 없는 두 집합

input 
1. node , edge
2-M union numbers

output
each element of  
1. root node
2. parent node

[Input]
6 4
1 4
2 3
2 4
5 6

[Output]
[1, 1, 1, 1, 5, 5]

"""

class Node:
    def __init__(self, number):
        self.number = number
        self.parent = self
        
    def set_parent(self, parent):
        self.parent = parent
        
    def get_parent(self):
        return self.parent
    
    def get_root(self):
        return self if self.parent is self else self.parent.get_root()
    
    def get_number(self):
        return self.number
        
    def __repr__(self): 
        return "{}".format(self.number)
    
    def __gt__(self, other):
        return self. number > other.number
    

def main(): 
    node_count, edge_count = map(int, input().split())
    nodes = []
    
    for i in range(node_count+1):
        node = Node(i)
        nodes.append(node)
        
    for _ in range(edge_count):
        node1 ,node2 = map(int, input().split())
        
        root1 = nodes[node1].get_root()
        root2 = nodes[node2].get_root()
        
        if root1>root2:
            root1.set_parent(root2)
        else: 
            root2.set_parent(root1)

    
    print([node.get_parent() for node in nodes if node.get_number()>0])
    print([node.get_root() for node in nodes if node.get_number()>0])
        
            
if __name__ == '__main__':
    main()