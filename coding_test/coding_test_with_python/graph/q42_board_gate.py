"""Quiz 42 탑승구 Page395

[Input Description]
1st. Gate Count
2nd. Plane Count
P. Dockable Gates Area for each plane(From Plane 1 to N)

{Case1}
[Input]
4
3
4
1
1
[Output]
2

{Case2}
[Input]
4
6
2
2
3
3
4
4
[Output]
3
"""

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
        return "Node{}".format(self.number)
    
    
def solution(gate_count, gate_info):
    nodes = [Node(i) for i in range(gate_count+1)]
    count = 0
   
    for plane in gate_info:
        root_node = nodes[plane].get_root()
        
        if root_node.number > 0 :
            root_node.set_parent(nodes[root_node.number-1])
            count +=1
        else:
            break
    
    return count
       
    

def main():
    gate_count = int(input())
    plane_count = int(input())
    gate_info = []
    
    for _ in range(plane_count):
        gate_info.append(int(input()))
        
    print(solution(gate_count, gate_info))
    
if __name__ == '__main__':
    main()