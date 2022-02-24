"""
Ice Cream Maker.
Problem from chapter 05 DFS/BFS(음료수 얼려먹기)

Description: 
How many ice cream (0 parts) are exsit in the tables?
- When the 0 is conencted(direction of up down left right)
  consider they are fully connected.

input
>>> 00110
>>> 00011
>>> 11111
>>> 00000

result 
>>> 5
"""

def input_value():
    """Input following values 
    1. row column
    2. values condier with 0 and 1
        - 0 means non ice
        - 1 means ice 
    """
    rows, columns = map(int, input().split())
    graph = list()
    for _ in range(rows):
        graph.append(list(map(int, input())))
    
    return rows, columns, graph


def is_visitable_blocks(row, max_row, column, max_column,graph):
    """Check the target block visitable

    Args:
        row (int) : current row 
        max_row (int): max row in graph
        column (int): max column in graph
        max_column (int): max column in graph

    Returns:
       Boolean: is a visitable block?
    """
    if row < 0 or row >= max_row or column  < 0\
        or column >= max_column :
        return False
    else:
        return not graph[row][column]
                


def visit_visitable_blocks(row, max_row, column, max_column, graph):
    """ Visit the visitable blocks
    1. Set the block as iced(visited)
    2. Vist the block up, down, left, right recursively
       If the block is in the graph range and not iced. 

    Args:
        row (int) : current row 
        max_row (int): max row in graph
        column (int): max column in graph
        max_column (int): max column in graph
        graph (list)
    """
    # set current block as visited. 
    if(is_visitable_blocks(row, max_row, column, max_column, graph)):
        graph[row][column] = 1  # set the current block    
        # Check each directio of the block
        visit_visitable_blocks(row, max_row, column-1,max_column, graph) # Right
        visit_visitable_blocks(row, max_row, column+1,max_column, graph) # Left
        visit_visitable_blocks(row-1, max_row, column,max_column, graph) # Upper
        visit_visitable_blocks(row+1, max_row, column,max_column, graph) # Down
        return True
    else:
        return False
        
def find_icecream_blocks(rows, columns, graph):
    """
    The main logic of find ice cream.
    """
    # Check sequencely if visited pass the block.
    count = 0
    for row in range(rows):
        for column in range(columns):
                count+=visit_visitable_blocks(row, rows, column, columns, graph)
    return count
            
     
def main():
    """main function"""
    rows, columns, graph = input_value()
    count = find_icecream_blocks(rows, columns, graph)
    print("Result", count)


if __name__ == '__main__':
    main()


