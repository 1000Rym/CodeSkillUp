# Seperate Input data(int) 
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
output = 0
print("n, m, k is ", n, m, k)
print("data is ", data)

data.sort()
first_data = data[len(data)-1]
second_data = data[len(data)-2]

output = second_data*(m%k) + first_data*(m-m%k)
print(output)