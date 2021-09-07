from collections import OrderedDict, defaultdict
from typing import DefaultDict

fruits = (('Apple',1),('Pear',2),('Grape',4),('Water melon',5),('Orange',3))
dict_fruits = dict(fruits)

# 1. Ordered fruits can keeps order.
ordered_fruits = OrderedDict(fruits)
# 2. Ordered fruits can be made with sorted value.
sorted_fruits = OrderedDict(sorted(fruits, key= lambda x : x[1]))


# Default dicts can assign default factory method. 
defaults_fruits = DefaultDict(int)
for key, value in fruits:
    defaults_fruits [key] = value

defaults_string = DefaultDict(int)
str1 = "Hello world!"

# Count of the char will be increased.
for key in str1 : 
    defaults_string[key] +=1


# Q1: Why there is no diff?
# A1: From the python 3.6 "dict keeps the insertion order."
print(f'Normal Dict: {dict_fruits.items()}')
print(f'Ordered Dict: {ordered_fruits.items()}')
print(f'Sorted Dict: {sorted_fruits.items()}')

print(f'Default Dict: {defaults_fruits.items()}')
print(f'Unknown item in default dict Mango:{defaults_fruits["Mango"]}')
print(f'Default Dict made by sting(Count Char):{defaults_string.items()}')
