n = int(input())
counter = 0 
for hour in range(n + 1):
    for minute in range(60):
        for second in range(60):
            if '3' in f'{hour}{minute}{second}':
                 counter +=1
print(counter)

