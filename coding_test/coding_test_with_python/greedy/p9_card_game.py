"""
카드게임
[I/O Description]
1st: row line
2nd-end: card numbers
result: The number is minimum in each row but maximum comparative to other rows. 

[input]
3 3
3 1 2
4 1 4
2 2 2

[output]
2
"""
if __name__ == '__main__':
    row, line = map(int, input().split())
    largest_minimum = 0    
    
    for _ in range(row):
        min_in_row = min(map(int, input().split()))
        largest_minimum = min_in_row if largest_minimum < min_in_row else largest_minimum
    
    print(largest_minimum)
