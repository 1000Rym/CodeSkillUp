numbers = [2,12,23,2,12,2,3,12,31]
description = {
    "length": (num_length:=len(numbers)),
    "sum": (num_sum:=sum(numbers)),
    "mean": num_sum/num_length
}

print(description)
