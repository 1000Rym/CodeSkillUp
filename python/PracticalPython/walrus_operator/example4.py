import time

def wait(count):
    time.sleep(count)
    print(count)
    return count

numbers = [1,2,3,4]

# Original List Comprehension Code
# the wait function run in two times. 
#print("Original:")
#[wait(number) for number in numbers if wait(number) > 0]

print("After Modify:")
[wait_result:=wait(number) for number in numbers if (wait_result:=wait(number)) > 0]