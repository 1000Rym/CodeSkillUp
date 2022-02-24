""" Make Team (page 298)
0 means unite team.
1 means check one team or not.

[input]
1. node count, input info count
2-m input info(0 or 1 and  node1, node2)

ex: 
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

[output]
result
NO
NO
YES
"""

class Node:

    def __init__(self, number):
        self.number = number
        self.parent = self
        
    def __gt__(self, other):
        return self.number > other.number
    
    def set_parent(self, parent):
        self.parent = parent
    
    def get_root(self):
        return self if self.parent is self else self.parent.get_root()
        
    def __repr__(self):
        return '{}'.format(self.number)
    

def unite_team(nodes, num1, num2):
    root1 = nodes[num1].get_root()
    root2 = nodes[num2].get_root()
    
    if root1 > root2:
        root1.set_parent(root2)
    else:
        root2.set_parent(root1)
        

def check_team(nodes, num1, num2):
    return nodes[num1].get_root() is nodes[num2].get_root()
    
def main():
    node_count, info_count = map(int, input().split())
    nodes = []
    result = ""
    
    for i in range(node_count+1):
        nodes.append(Node(i))
    
    for _ in range(info_count):
        option, node1, node2 = map(int, input().split())
        if option == 0:
            unite_team(nodes, node1, node2)
        elif option == 1:
            result += "YES" if check_team(nodes, node1, node2) else "NO"
            result += '\n'
    
    print(result)
           

if __name__ == "__main__":
    main()


