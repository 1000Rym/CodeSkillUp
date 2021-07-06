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
        >>> "{0:=^10}".format(str)
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
- List value can be modified by using index.  
    ```python
    >>> a = ["Hello","My name"]
    >>> a[0] = 'hi'
    >>> a
    ['hi', 'My name']
    ```
- List value can ve added or removed. 

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

