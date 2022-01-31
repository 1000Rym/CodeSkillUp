"""
Graph check cycle algorithm

[Input]
3 3
1 2
1 3
2 3

[Output]
Cycle 이 발생했습니다.
"""

class Node:
    def __init__(self, number):
        self.parent = None
        self.number = number
    
    def set_parent(self, parent):
        self.parent = parent
    
    def get_root(self):
        return self.parent.get_root() if self.parent is not None else self
    
    def __gt__(self, other):
        return self.number > other.number
    
    def __eq__(self, other):
        return self.number == other.number
    
    def __repr__(self):
        return "{}".format(self.number)
    
     


def main():
    node_count, edge_count = map(int, input().split())
    nodes = []
    is_cycle = False
    
    for i in range(node_count+1):
        nodes.append(Node(i))
    
    for _ in range(edge_count):
        node1, node2 = map(int, input().split())
        parent1 = nodes[node1].get_root() 
        parent2 = nodes[node2].get_root()
              
        if parent1 == parent2:
            is_cycle = True
            break
        elif parent1 > parent2:
            parent1.set_parent(parent2)
        else:
            parent2.set_parent(parent1)
    
    if is_cycle: 
        print("Cycle 이 발생했습니다.")
    else:
        print([node.get_root() for node in nodes if node.number>0])

            

if __name__ == "__main__":
    main()