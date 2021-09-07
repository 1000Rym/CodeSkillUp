from random import random
from array import array

DATA_SIZE = 10**7

floats = array('d', (random() for _ in range(DATA_SIZE)))
print(floats[-1])

file = open('floats.bin', 'wb')
floats.tofile(file)
file.close()

file = open('floats.bin', 'rb')
floats2 = array('d')
floats2.fromfile(file, DATA_SIZE)
file.close()
print(floats2[-1])

print("Equal array!") if floats == floats2 else print("Not equal!")