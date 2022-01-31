"""
Kruscal Algorithm
"""
import heapq

class Node:   
    def __init__(self, number):
        self.parent = None
        self.number = number
        
    def __eq__(self, other):
        return self.number == other.number

    def __gt__(self, other):
        return self. number > other.number
    
    def set_parent(self, parent):
        self.parent = parent
        
    def get_root(self):
        return self if self.parent is None else self.parent.get_root()


def main():
    node_count, edge_count = map(int, input().split())
    nodes = []
    q = []
    total_cost = 0
    
    
    for i in range(node_count + 1):
        nodes.append(Node(i))
    
    for _ in range(edge_count):
        node1, node2, cost = map(int, input().split())
        heapq.heappush(q, (cost, (node1, node2)))
        
    
    while q: 
        cost, (node1, node2) = heapq.heappop(q)
        
        parent1 = nodes[node1].get_root()
        parent2 = nodes[node2].get_root()
        
        if parent1 == parent2:
            continue
        elif parent1 > parent2:
            parent1.set_parent(parent2)
        else:
            parent2.set_parent(parent1)
        
        total_cost += cost
    
    print(total_cost)

if __name__ == '__main__':
    main()