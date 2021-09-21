## Chapter10: Sequence Hacking, Hashing, and Slicing

Features:
- Representation of instances with many items
- Basic Sequence Protocal: `__len__` and `__get_item__`
    - Slicing
    - Dynamic Attitube Access
- Hashing
- Custom formatting extension
- Formatting(ommitted)

### Representing of instances with many items
- Use `reprlib.repr()` could abbriviated with `...`
    - example code: [vector_v1.py](vector_v1.py)

### Basic Sequence Protocal
To implement sequence protocal, implement one of `__getitem__()` and `__len()__`. To support iteration only `__getitem__()` is required.
- example code: [vector_v1.py](vector_v1.py) line 37, 41.

#### Dynamic Attribute Access
- Using `@Property`: 
    - Example Code: [person_property.py](person_property.py)

- Using `__getattr__()`, `__setattr__()`
    - Example Code: [vector_v3.py](vector_v3.py)


#### Hashing and Advanced equal
- How does a `functools.reduce` work?
    - reduce(fn, lst) :
        - fn(lst[0], lst[1]) -> fn(r1, lst[2]) -> fn(r{n-1}, lst[n])
- Fast Hash method can be implemented with `functools.reduce()` by giving arguments by following.
    - first arg: function
    - second arg: iterable with `__hash__()` calculated. 
    - third arg: initilizer

- To use `len()`, `all()` and `zip()` fast compair.
- Example Code: [vector_v3.py](vector_v3.py)

### Formating
(omitted)


