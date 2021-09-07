#This Example code is made for implement simple list comprehension example. 

if __name__ == "__main__":
    print("9X9 multiplication table.")
    
    # List comprehension example.
    list_comp = [(f"{i} X {j}", i*j) for i in range (1, 10)
                                    for j in range (1, 10)]

    for description, value in list_comp: 
        print(f'{description}={value}')

    print("="*10)

    # Generator Example. 
    generator = ('{0} x {1} = {2}'.format(i, j, i*j) for i in range(1,10)
                                            for j in range(1, 10))

    for description in generator:
        print(description)
    