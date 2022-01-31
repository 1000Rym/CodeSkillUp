# Contents
- Identify The Walrus Operator
- Understand Use Cases
- Avoid Repetition
- Convert Between Assignment Methods
- Understand Backwards Compatiblitity
- Style

## Fundementals
- Python >= 3.8 
- Naming Conventions For `:=` 
    - Assignment Expression Operator
    - Walrus Operator
    - Colon Equals Operator
    - Named Expressions
- Usage
    - Used in Assignment Expressions
    - Returns Assigned Value

- Why use Walrus
    - Repeated Function calls
    - Repeated Statements
    - Repeated Iterators

- Use Cases
    - Simplify Syntax: [example1.py](example1.py)
    - Used List and Dictionaries:
        - Simplify Number List [example2.py](example2.py)
        - Simplify File Reader: [example3.py](example3.py)
        - List Comprehensions:
            - [example4.py](example4.py)
        - While Loops: (example5.py)[example5.py]
        - Witness:(example6.py)[example6.py]

    - Rules:
        - Discourage to replace `=` with walrus operator any reason.
        -  Can not be used in Attribute and Item Assignment
        - Can not be used in Iterable Unpackting
        - Can not be used in augmented assignment operator(+=, -= etc,)
        - Follow LEGB Rule.
        - Walrus operator binds more tightly than `,`
        - Only Use it when it is helpful.
    
    - Piftfalls:
        - Python >= 3.8
        - Only Implement When usefor
        - Improving, Readibility, Effectioncy.
    
## Summary
In this page, we described how to use and read walrus operator. Walrus operator is used for reduce repeatable code, and Improve code quality, however, overuse it not recommended.


    