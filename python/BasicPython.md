# Abstract
This page is containing basic knowledge of python. 

## Introduction
Python is an interpreted high-level general-purpose programming language, Developed by Guido van Rossum.
- Beatiful is better than ugly. 
- Explicit is better than implicit. 
- Simple is better than complex. 
- Readability counts. 

> "Life is short, You need python."

## Data Type
### Number
- Integer
- Floating-point
- Octal: Add `0o` or `0O` infront of the value.
    ``` python
    value = 0o1771
    value = 0O1771
    ```
- Hexademical: Add `Ox` in front of the value. 
    ```python
    value =  0x8ff
    ```

## Arithmatic Operator
Python supports the following arithmetic operators. 
They are `+`, `-`, `*`, `/`, `%`, `//`, `**`
- `//`:  Integer Division
```python
>>> 7//4
1
```
- `**`: Exponentiation
```python
>>> 2**4
16
```

## String 
A charactre string: Sequence of the Unicode code points(immutable). 
-  Excape code: Predefined character set when programming. 

| Code | Description|
| :---:|    :---:   |
|   \n    | New Line        |
|   \t    | Tab             |
|   \\\	  | Char `\`        |
|   \\'	  | Char `'`        |
|   \\"	  | Char `"`        |
|   \\r	  | Carrage Return  |
|   \\f   | Form Feed       |
|   \\a   | Bell Sound      |
|   \\b   | Back Space      |
|   \\000 | Null            |

- Carrage Return: Move cursor to the head of line. 
- Form Feed: Move cursor to next line. 

### String Operation
#### Concatenation, Multiple String
Python supports concatnation, and multiple by using `+` and `*`.
``` python
a = 'I have a pen.\t'
b = 'I have a pencel.'
c = a+b
d = a*2
```

### String Index and Slicing.
- vaue[`from_index`:`to_indx`] -> value[`from_index`x:`to_index`)
- value[`from_index` : ] ->  value[`from_index` : end)
- value[`: toindex` ] -> [`frist_index `:` to_index`)


###  String Format 
-  With format code: 
     ```python
        >>> progress = 98
        >>> value = "The progress is up to %d %%." %progress
        >>> print(value)
        The progress is up to 98%.
      ```
    | Code | Description|
    | :---:|    :---:   |
    |   %s  |Str        |
    |   %c  |Char       |
    |   %d  |Integer    |
    |   %f  |Floating   |
    |   %o  |Oct        |
    |   %h  |Hex        |
    |   %%  |Literal %  |

    - With Number Align:
        ```python
        >>> print("%10s, lin" %value)
                hi, lin

        >>> print("%-10s,lin" %value)
        hi        ,lin


        >>> pi = 3.14159265359
        >>> print("Pi is %5.4f" %pi)
        Pi is 3.1416
        ```

- With Format function. 
    - With ordered number: {0},{1}
    - With variable:{greeting}
    ```python
    >>> name = "Tim"
    >>> "Hello {1}, I am {0}, {greeting}".format(name, "Lam", greeting="Nice to meet you!")
    'Hello Lam, I am Tim, Nice to meet you!'
    ```
    - With number align
        - `:<` : Left
        - `:>` : Right
        - `:^` : Align Center
        ```python
        >>> str = "hi"
        >>> "{0:<10}, jane".format(str)
        'hi        , jane'
        >>> "{0:>10}, jane".format(str)
        '        hi, jane'
        >>> "{0:^10}, jane".format(str)
        '    hi    , jane'
        ```
    - Fill with char : Add char in the middle of `:<` or `:>`, `:^ `
        ```python
        >>> "{0:=^10}".format(str) ## will print 8 =
        '====hi===='
        ```

- With \``f` formating(from python 3.6)
    - Can do exact same thing with format, If the arguments declared previously. 
    ```python
    >>> name = "Lin"
    >>> f"Hello, my name is {name:=^10}"
    'Hello, my name is ===Lin===='
    ```

#### String function
- stc.count(`value`): Return count of the value among the string.
- str.find(`value`): Return first index of found value, return -1 when not found.
- str.index(`value`): Return the first index of found value. return error when not found.
- `str2add`.join(`str2change`)
- str.upper(), str.lower()
- str.strip(), str.lstrip(), str.rstrip(): Remove space(Left, Right, or two sides) of the value.
- str.replace(`from`,`to`)
- str.split(`str2split`,`standard_of_split_value`)

### List 
The ordered elements. Element can be an empty list, integer, string, or list it self. 
- List value can be modified by using index(Mutable).  
    ```python
    >>> a = ["Hello","My name"]
    >>> a[0] = 'hi'
    >>> a
    ['hi', 'My name']
    ```
- List value can ve added or removed. 
     ``` python
    >>> a = [1,2,3]
    >>> del a[1:-1]
    >>> a
    [1, 3]
    ```
- List Function
    - `append()`, `extend()`: 
        ``` python
        >>> a = [1,2,3]
        >>> a.append("hello word")
        # Add Object.
        [1, 2, 3, 'hello word']

        >>> a = [1,2,3]
        >>> a.extend("hello word") # or a+= "Hello word"
        # Add items in Object.
        [1, 2, 3, 'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'd']
        ```
    - index(x), find(x): Find the x from the list. `index()` return ValueError Exception, `find()` return -1 when not find target item in list.
    ```python

    ```
    - `sort([Option]reverse= True or False)`, reverse(): These function also change the order.
        ```python
        >>> a = [1, 22, 33, 112, 11, 63,32]
        >>> a.sort()
        >>> a
        [1, 11, 22, 32, 33, 63, 112]
        
        # Reverse sort
        >>> a.sort(reverse=True)
        >>> a
        [112, 63, 33, 32, 22, 11, 1]
        >>> a.reverse()
        >>> a
        [1, 11, 22, 32, 33, 63, 112] 

        # Sort with key
        >>> list_1 = "You are my every thing".split()
        >>> list_1.sort(key=len)
        >>> list_1
        ['my', 'You', 'are', 'every', 'thing']

        # Sort assign without change origninal.
        >>> b = [123,34,23,12,32,55,534]
        >>> c = sorted(b)
        >>> c,b # c is changed without b
        ([12, 23, 32, 34, 55, 123, 534], [123, 34, 23, 12, 32, 55, 534])
        ``` 

    - `reverse()` the list.
        ```python
        >>> a = [112, 63, 33, 32, 22, 11, 1]
        >>> a.reverse()
        >>> a
        [1, 11, 22, 32, 33, 63, 112]

        #reverse without change original list.
        >>> a = [112, 63, 33, 32, 22, 11, 1]
        >>> b = [x for x in reversed(a)]
        >>> b
        [1, 11, 22, 32, 33, 63, 112]
        ``` 

    - `insert(position, object)`: insert object into the position.
        ```python
        >>> a.insert(2, "hello word!")
        >>> a
        [1, 2, 'hello word!', 3]
        ```
    - `remove(x)`: Remove the first x from the list.
        ```python
        >>> a
        [1, 2, 'hello word!', 3, 'hello word!']
        >>> a.remove('hello word!')
        >>> a
        [1, 2, 3, 'hello word!']
        ```
    - `pop(), pop(position)`: Pop the last item(without position) or pop position's item(The poped item would be removed from the list) and return the item.
        ```python
        >>> a= [1, 2, 3, 'hello word!']
        >>> value = a.pop(3)
        >>> print(value)
        'hello word!'
        # a
        [1, 2, 3]
        ```
    - `count(x)`: count the x in the list. 
        ```python
        >>> a = [11,22,23,11,[11,22],13]
        >>> a.count(11)
        2
        ```
- List Copy
    - Shallow Copy (`[:]`): Copy the items in the from the list, But the items are still same object. 
        ```python
        >>> a = [[12,23],[25,32]]
        >>> b = a[:]
        >>> a is b
        False
        >>> a[0] is b[0]
        True
        >>> a[0].append(12)
        >>> b 
        [[12, 23, 12], [25, 32]] # b[0] is also changed.

        # Also same as copy function from copy module.
        import copy
        b = copy.copy(a)
        >>> import copy
        >>> c = copy.copy(a)
        >>> c
        [[12, 23, 12], [25, 32]]
        ```
    - Deep Copy(`copy.deepcopy()`): Copy the item's value from the list.
        ```python
        import copy
        >>> d = copy.deepcopy(a)
        >>> d[0] is a[0]
        False   
        ```

### Tuple
Tuple is the immutable object that it could not modify the value once it declared.
- Declare with `()`, and the symbol can be ignored.
- Use index to access, or slicing, Use (`+`) to concatenate, (`*`) to multi tuple's item.
- When declare one element, use `,` `a(1,)`.
    ```python
    >>> (1,2,3)+(4,)*2
    (1, 2, 3, 4, 4)
    ```
- use built in method `len` to gen tuple's length.
- use `count(x)` to get x's count.
- use tuple to return multiple value.
- use tuple to exchange value. 
    ```python
    >>> a =1
    >>> b =2
    >>> a,b = b,a
    >>> a,b
    (2, 1)
    ```
### Dictionary 
Dictionary is an associated array constructed with the items pair of `key` and `value`.
- Key is immutable type object, Value can be mutable or immutable. 
- If the key value is overlapped, adopt the last value.
- Functions: `keys()` to get keys, `values()` to value. `items()` to get items with key and value. `clear()` to delete all items. `get('key')` to get the item's value with key.
- To update the value, use `object[key]` and change single value, or use `update({items})` to change multiple values.
- To shallow copy dictionary, use `=` or `copy.copy()`. To deep copy the dictionary use `copy.deepcopy()`
- Use `dict()` to dictionary type change. When the items(tuple, list) in the tuple or list construct with key and value. We can use dict() to change the type to the dictionary.
- use built in method `del(key)` to delte the item with key.
- use pprint to pretty print the key:value type.


```python
>>> dict_a = {'a':1, 'b':2, 'c':3} 
>>> dict_a = dict(a=1, b=2, c=3)
# Get Keys
>>> dict_a.keys()
dict_keys(['a', 'b', 'c'])

# Get Values
>>> dict_a.values()
dict_values([1, 2, 3])

# Get Items
>>> dict_a.items()
dict_items([('a', 1), ('b', 2), ('c', 3)])

# Get Item with the key
>>> dict_a.get('a') # or dict_a['a']
1

#Get Not exist item.
>>> dict_a.get(1) 
None #print noting
>>> dict_a[1] 
keyError

#Get value with key from dictionary by using default value. 
>>> dict_a.get('d', 0)
0 # default return 0
>>> dict_a
{'a': 1, 'b': 2, 'c': 3} # But the value is not added to the dictionary
a

# Update value
>>> dict_a['a']  = 2 # Single Update
>>> dict_a.update({'b':3, 'c':4}) # Multiple Update
>>> dict_a
{'a': 2, 'b': 3, 'c': 4}

# Dicionary type change
>>> a = [[1, 2], [2, 3], [4, 5]]
>>> dict(a), 
{1: 2, 2: 3, 4: 5}

>>> b =(((1, 2), (3, 4)), (5, 6), (7, 8))
>>> dict(b)
{(1, 2): (3, 4), 5: 6, 7: 8}

# Use pprint(Pretty print)
>>> from pprint import pprint as pp
>>> pp(dict_a)
dict_a ={'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30, 'dodo': [1, 3, 5, 7], 'mario': 'pitch'}
>>> pp(a)
{'alice': [1, 2, 3],
 'bob': 20,
 'dodo': [1, 3, 5, 7],
 'mario': 'pitch',
 'suzy': 30,
 'tony': 15}
```

### Set
Set is the object with unordered, non-overlapping item(s).
- Set can only have immutable and iterable object.
- Similar with dictionary but not have key.
- When declaring a set, use the built-in function `set` is suggested(The empty `{}` is known as dictionary).
```python
# Declaring a set
>>> s1 = {1,2,3}
>>> s2 = set((4,5,6))
>>> s1
{1, 2, 3}
>>> s3 = {}
>>> type(s3)
<class 'dict'> # The empty {} is known as dictionary
```

- Set Function (The op function can be used with `=` to assign op)
    - intersection : `&`
    - union : `|`
    - difference : `-`
    - symmetric difference: `^` (Union - difference)
    ```python 
    >>> a = {1,2,3,4,5}
    >>> b = {3,4,5,6,7}
    
    # union
    >>> a.union(b)
    >>> a | b
    {1, 2, 3, 4, 5, 6, 7}

    # difference
    >>> a.difference(b)
    >>> a-b
    {1, 2}

    # Symmetric differnce
    >>> a.symmetric_difference(b)
    >>> a^b
    {1, 2, 6, 7}

    >>> a |= b
    >>> a
    {1, 2, 3, 4, 5, 6, 7}
    ```

    - Use `add(x)` to add one x, use `update(values)` to add multiple value.
    ```python
    # add one value.
    >>> a = {1,2,3,4,5}
    >>> a.add(6)
    {1, 2, 3, 4, 5, 6}

    # update multiple values
    >>> a.update((7,8))
    {1, 2, 3, 4, 5, 6, 7, 8}
    ```

    - use `remove()` or `discard()` to delete value.
    ```python
    >>> a = {1, 2, 3, 4, 5, 6, 7, 8}
    >>> a.remove(7)
    >>> a.discard(5)
    {1, 2, 3, 4, 6, 8}
    ```

### Condition 
- Instead of using `&&`, `||`,`!`, in python use `and`, `or`. and  `not`.
- Conditional expression: expression `if` condition `else` expression
    ``` python
    >>> score = 100
    >>> print("You are passed") if score>=60 else print("Failed")
    You are passed
    ``` 






### Scoping Rule
Currently there are 4 scopes in python. They are __Local Scope__, __Non-local(Enclousing) Scope__, __Global Scope__, and __Built-in Scope__. 

- Scope:
    - Local Scope: The name(s) in the local scope are only available to the scope where it is declared(lambda expression or function).
    - Enclosing Non-local Scope: If the local scope is the inner(nested) function, the non-local scope is the scope between the inner function and the outer(enclosing) function.
        - Introduced in python 3.0.  
    - Global Scope: The names defined in global scopes are available to all scope.
        - The scope under the `__main__`
    - Built-in Scope: The scope in the module is named `builtins`. The `builtin` module is automatically loaded when running the python interpreter.

- Accessing Rules: 
    - Find the variable from local-> non-local(enclosing), global, to builtins. 
    - The variable in the lower scope can not be accessed by higher scope.
    - The variables typed immutable(string, number,tuples) defined in higer scope could not be modified in lower scope. 
        - However, we can use the keyword `global`, `nonlocal`, to modify the value. 
            - Using the keyword `global` to access a global name will declare a name from the global namespace if the global name does not exist. 
            - On the other hand, when using `nonlocal` when the name does not exist in the nonlocal namespace, it will show a syntax error.   


### function
- About Return Value: In Python we can return multiple values constructed with one object typed tuple.
- About arguments: In python we can use two kinds of arguments.
    - positinal arguments: Provide the arguments in the same order as defined.
        - Use a single *(asterisk) operator(Also known as iterable unpacking) extends functionality. 
    - keyword arguments: An argument could be passed with keyword arguments. 
        - Use double ** operator(Also known as dictionary unpacking operator) to unpack arguments have been passed.
    - default arguments: Default argument is an argument to a funtion that a programmer not need to specify(Default arguments should not located in previously).

- Lambda Expression: `lambda` param1, param2, ... : expression(use the params) 


### Input and Output
- Prompt:
    input : use `input()` to input value. 
    output : `print()` to print the value.  
    - `print("a" "b" "c" "d")` is equal to `print("a"+"b"+"c"+"d")`
    -  comma(`,`) in `print` mean's space `print("a", "b")` -> `a b`
    - use keyword `end` to finish sentence.
        ```python
        >>> for x in range(25) : print(x, end=" ")
        ...
        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
        ```
- File IO:
    - write: open with `w` mode, use function `write()`
    ```python
    >>> try:
    ...     file = open("test.txt", 'w')
    ...     for i in range(1, 11):
    ...             file.write("This is the {0} lines\n".format(i))
    ... finally:
    ...     file.close()
    ```
    - read: open with `r` mode.
        - use function `readline()`: Read line by line
        - `readlines()` 
        - `read()`

    ```python
    >>> try:
    ...     file  = open("test.txt", "r")
    ...     number = 1
    ...     
    ...     # using read lines: 
    ...     lines = file.readlines() 
    ...     for no, line in enumerate(lines, start=1):
    ...             print(f"{number}:{line}")
    ...     
    ...     # using readline:
    ...     while(True):
    ...     line = file.readline()
    ...     if line :
    ...             print(f"{number}:{line}")
    ...             number +=1
    ...     else:
    ...             break
    ...
    ...     # using read: 
    ...     print(file.read())
    ...
    ... finally:
    ...     file.close()
    ``` 
    - append : open with `a` mode. use `write, writelines` function. 
    ``` python
    >>> try :
    ...     file = open("test.txt", "a")
    ...     for i in range(11,21):
    ...             file.write("This is the {0} lines.\n".format(i))
    ... finally:
    ...     file.close()
    ```
    - use `with` and `as` to automatically `close` the file.
    ```python
    >>> with open("test.txt", 'r') as file: print(file.read())
    ``` 


### Class
- Class Variable: The class variables can be shared via classes. (Like Singleton)

### Regular Expression
Regular Expression is a sequence of characters that specifies a search pattern
(Use for the string search algorithms.).

- Meta Charecters
    - `^` :  Start position of the string token in a line.
    - `.` :  Any characters.(new line is excluded in python).
    - `[]`:  Bracket expression matches any character beteween `[` and `]`
    - `[^ ]` Matches a single character not in bracket expression.
    - `$`:  End position of the string token in a line
    - `()`: Sub Expression(Grouping).
    - `\n`: Matches nth marked subexpression.
    - `*`: More than zero occurences of the proceeding element.  
    - `+`: More than one occurences of the proceeding element.
    - `?`: Zero or one occurences of the proceeding element.
    - `|` : Option A or B
    - `\A` : Match the first string when using re.MULTILINE option.
    - `\Z` : Match the last string when using re.MULTILINE option.
    - `\b`: Word boudary(Seperate words between white space.).
    - `\B`: opposite option to `\b`. 




- Method supported for the pattern compiled object.
    - `match()` : First matched object from the first string.
    - `search()`: First matched object from the total context.
        ```python
        # Init the pattern, pattern is the any string costruct with alphabetic charecters. 
        >>> import re
        >>> p = re.compile('[a-z]+')

        #  Use search to find matched object from the first string. 
        >>> m = p.match("is python good?")
        >>> m
        <re.Match object; span=(0, 2), match='is'>

        # Use match method to find the first matched object from the context.
        >>> m = p.search('3 python is good!')
        >>> <re.Match object; span=(2, 8), match='python'>

        # Use findall method to get a list constructed with string tokens match the pattern.
        >>> m = p.findall('3 python is good!')
        >>> m
        ['python', 'is', 'good']

        # Use finditer method to get a iterator that include tokens match the pattern.
        >>> m = p.finditer('3 python is the good')
        >>> m
        <callable_iterator object at 0x10e086190>

        
        # Use Word Boundary \b and \B
        >>> p1 = re.compiler('\bclass\b')
        >>> print(p1.search("I like my class"))
        <re.Match object; span=(10, 15), match='class'>

        >>> p = re.compile(r'\Bclass\b')
        >>> print(p.search('one subclass is'))
        <re.Match object; span=(7, 12), match='class'>
        ```

    - Method supported for matched patterns.
        - group() : return the matched string. 
        - start(): return the matched string's start position. 
        - end():  return the matches string's end position
        - span(): return a tuple object which have (start_position, end_position) of matched string.
        - sub(): Change the string matches the pattern.

        ``` python
        >>> import re
        >>> p = re.compile('[a-z]+')
        >>> m = p.search('3 python is good!')
        
        # group function
        >>> m.group()
        'python'

        # start fucntion 
        >>> m.start()
        2
        
        # end function
        >>> m.end()
        8
        
        # span function
        >>> m.span()
        (2, 8)
        ```

    - Compile Option:
        - DOTALL, S : Include the newline. 
        - IGNORECASE, I : Ignore upper or lower cases.
        - MULTILINE, M : Handling multi-lines. 
        - VERBOSE, X : Add commentary in the regular expression.

    - Grouping: `()` to group multiple used string as a group 
        - Refereing Group: `\number` -> `\1`, `\2`
        - Grouping name:`(?P<name>)` -> to define name.
    - Search
        - Front : `(?=...)`
        - Negative Front: `(?!...)`  
    - Greedy to NonGreedy add `?` to the back, to avoid greedy search from `*`, `+`, `{m,n}`(Search Once). 
    - Note: 
        - Directly use the search, match method from the regular expression module.
        ```python
        >>> import re
        >>> p = re.compile('[a-z]+')
        >>> m = p.search('[a-z]+', '3 python is good!')
        >>> m = re.search('[a-z]+', "3 python is good")
        ```
        - When using back slack(`\`), add `r`(rough string) in front of the target string.
            - To avoid regular expression compiler ignore the backslach from python regular engine when compile.
 



### Exception
Use with the keyword `try`, `except`, `else`, and `finally`
- `try`: try to run some code.
- `except`: except handling when there are any exception.
- `else`: if there is no exception run the code. 
- `finally`: no matter success or not run the code.
- When implement in the class.
    - inherit from `Exception` 
    - add and special method `__str__(self)` 

```python
def changelist():
...     list = [10,20,30]
...     index = input("Please input the index:")
...     value = input("Please input the value:")
...     try:
...             list[index] = value
...     except IndexError as e:
...             print("Index Wrong {0}".format(e))
...     else:
...             print(list)
...     finally:
...             print("The changelist function has finished")
...
>>> changelist
<function changelist at 0x10f37c488>
>>> changelist()
Please input the index:1
Please input the value:15
[10, 15, 30]
The changelist function has finished
>>> changelist()
Please input the index:6
Please input the value:20
Index Wrong list assignment index out of range
The changelist function has finished
```

### Builtin Method
- `abs`: return absolute value.
- `all(iterable)`: Check the iterable items, if all of the item is True return True.  
- `any(iterable)` : Check the iterable items, if any item is false, return false. 
- `chr`, `ord` : Change the ASCII to char, Change char to ASCII
- `dir` : Show the object function and varibles. 
- `divmod`: Return division(`//`) and remain.
- `enumerate` : return `index` and `iterable` value together.
- `eval` : evalueate teh expression.
- `filter(f, iterable)` : Filter the items in iterable are returning the true, return filter(iterable object).
- `hex`, `oct`, `int` : change value to hex, oct, integer. 
    - `int(string, base)`: change base type string value to integer.
- `id`: Show the object reference id. 
- `input` : input prompt
- `isinstance` : Show is instance of somethign or not. 
- `len` : Show the lenght of iterable object.
- `list`, `str`, `tuple` : change iterable object to list , str, tuple type.
- `map(f, iterable)`: run the function with iterable object, return iterable result. 
- `zip`: zip the iterable objects item(nXm -> mxn). 
- `max`, `min`: return largest number in iterable object.
-  `sum`, `pow`, `round(number, [ndigits])` : return the sum, pow, round of the results in items(items type should be numeric) 
- `open`: Open the file with read, write, binary mode.
- `sorted`, `reversed`: Return sorted, or reversed result. This function dosen't change original object.


### Library
- `sys`: To control python interpreter's function and variable.
    - `sys.path`: python modules path, the modoule in path are callable in any where.
    - `sys.exit()`: Terminate the interpreter.
- `pickle`: Use the `pickle.dump()` to store python data on the file(only support write to byte -> `wb`), `pickle.load(data, f)` to get data. 
- `os` : To control modules os environment, directory, Run the system command.
    - `os.chdir(path2change)`: change directory. 
    - `os.mkdir(directory))` : create the directory. 
    - `os.rmdir(directory)` : delete directory when the directory is empty.
    - `os.unlink(file_name)` : delete the file.
    - `os.rename(src, dst)` : change the file name. 
    - `os.getcwd()`: get current path. 
    - `os.system(command)` : Run the system command
    - `result = os.popen(command)` : Run the system command and return the result. 
        - `result.read()` : check returned result.
- `shututil`: copy the src file to dst. 
- `glob`:  Using for the find the file. Can use `*`, and `?` meta char to filter the files.
- `tempfile` : Create a tempororay file. `temfile.mkstemp()` gen file. or `tempfile.TempororaryFile(option, wb, wt)` to create an temporary file, delete when close.
- `time`: Time module. 
    - `time.time()`: Return UTC(Universal Time Coordinated 1970.1.1),return time
    - `time.localtime()`: reuturn structured local time. 
    - `time.asctime(time.localtime()))` : return stirnig type time.
    - `time.ctime()`: same as above command
    - `time.strtime(format, time.localtime())`: print format typed time
    - `time.sleep(time)`: sleep n seconds time.
- `calendar`: print calandar.
    - `calendar.prcal(year)`
    - `calendar.prmonth(year, month)`
    - `calendar.weekday(year, month, day)`
    - `calendar.monthrange(year month)`
- `random`
    - `random.randint(start,end)` :  generate an random number between start to `end-1`
    - `random.random()`: generate a float number between 0 to 1
    - `random.shuffle()` : shuffle the iterable object.
    - `random.choice()`: random choice one element from the list
- `threading` : Use thread.
    - `t= threading.Thread(target = Function2Run)`: start a t thread. 
    - `t.join()`: Wait until the thread ends.

