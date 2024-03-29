"""
문자열 뒤집기
Get Minimum Flip Count, Make the string same number. page(313)
- Flip Number 0, 1
[Input]
0001100

"""
def my_solution(numbers):
    # Flip number if the current number is not same as the front number
    flip_start = False
    count = 0
    for i in range(1, len(numbers)):
        if numbers[i-1] != numbers[i] : 
            flip_start = not flip_start
            # If current flip is new flip add count
            if flip_start : count +=1 
    
    return count

def main():
    numbers = list(map(int, input()))
    print(my_solution(numbers))
   

if __name__ == '__main__':
    main()