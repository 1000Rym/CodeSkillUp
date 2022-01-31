"""
Find minimum money count. 

[input]
- type count, amount
- array 

[output]
- minimum money count

example: 
[input]
2 15
2
3

[output]
3
"""
MAX_VALUE = 10000

def my_solution(types, amount):
    possible_amount = {0,}
    count = 0 

    while min(possible_amount)<amount:
        new_amount = set()
        count += 1

        for money in possible_amount: 
            for mount in types: 
                new_amount.add(money + mount)

        if amount in new_amount :
            return count
        else: 
            possible_amount = new_amount

    return -1

def dynamic_solution(types, amount):
    end_count = MAX_VALUE + 1
    array = [end_count] * (amount + 1)
    array[0] = 0
    
    for mount in types: 
        for i in range(mount, amount+1): 
            if array[i-mount] != end_count:
                array [i] = min(array[i], array[i-mount] + 1)
        
    if array[amount] == end_count:
        return -1
    else:
        return array[amount]
    


def main():
    type_count, amount = list(map(int, input().split()))
    types = []
    
    for _ in range(type_count):
        types.append(int(input()))
    
    print(my_solution(types, amount))
    print(dynamic_solution(types, amount))

if __name__ == '__main__':
    main()