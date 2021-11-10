
M, N = map(int, input().split())

result = 0

for count in range(M): 
    new_row_min = min(map(int, input().split()))
    if result < new_row_min : result = new_row_min

print(result)
