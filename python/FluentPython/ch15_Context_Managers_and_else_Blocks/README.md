## Chapter15 Context Managers and else Blocks
In this chapter we are going to master `with` and `else` clauses:
- The `with` statement and context managers.
    - Prevent errors and reduces boilerplate code.
- The `else` clause in `for`, `while` and `try` statements.

### Do This, then That: else Blocks Beyond if
The `else` can be used in other sementics such as: 
- `for/else` : The else block will run only if and when the for __loop runs to completion__(not when for is aborted with a break).
    ```python
    item_list = ["banana", "apple", "bear", "strawberry", "blueberry"]
    item_to_find = "melon"
    for item in item_list:
        if item_to_find == item : break
        else: raise ValueError('We could not find the', item_to_find)

    # Result
    Traceback (most recent call last):
    File "<stdin>", line 4, in <module>
    ValueError: ('We could not find the', 'melon')
    
  
- `while/else` : The else block will run only if and when the while __loop exist because condition became false.__(not when for is aborted with a break)
    ```python
    item_list = ["banana", "apple", "bear", "strawberry", "blueberry"]
    while item_list:
        if item_list.pop() == item_to_find : break
    else : 
        raise ValueError('We could not found the', item_to_find)
    
    #Result 
    Traceback (most recent call last):
    File "<stdin>", line 4, in <module>
    ValueError: ('We could not found the', 'melon')
    ```
  
- `try/except/else`: Else block is called when there is no exception. Commonly used for control flow, and not just for error handling.
    ```python
    try: 
        dangerous_call() # open file
    except OSError:
        log('OSError...') # file not found
    else: 
        after_call() # close file
    ```


