N, K =  map(int, input().split())
count = 0
count  += N%K 
while N > 1: 
    N//=K
    count +=1
print(count)