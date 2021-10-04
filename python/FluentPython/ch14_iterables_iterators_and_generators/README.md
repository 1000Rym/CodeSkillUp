## Chapter 14: Iterables, Iterators, and Generators
In this chapter, we will learn how the Iterator pattern built into the python.

- Note: Every generator is an iterator. And be aware of Python community treats iterator and gernerator as synonyms most of the time.

- Every collection in Python is iterable, and iterators are used internally to support:
    - for loops
    - Collection types construction and extension
    - Looping over text files line by line
    - List, dict, and set comprehensions
    - Tuple unpacking
    - Unpacking actual parameters with * in function calls

### Make iterable sequence
- exmaple: [sentence.py](sentence.py)

### Why sequnce are iterable: The iter function
Interpreter checks the following items to know the objects is iterable:
- 1. Where the object implements `__iter__`
- 2. If not, It will check `__getitem__` instead of, Python creates an iterator starting from index 0
- 3. If above steps fail, Python will raise Type Error "C object is not iterable" C is meaning class of the target object.
To check the object iterable `iter(x)` is more recommended than isinstance(x, abc.Iterable). Since the abc.Iterable only checks `__iter__` method.

### Iterable Versus Iterators
Any objects that could return iterator from the `__iter__` are the iterable.

### A Classic Iterator
- exmaple: SentenceIterator in [sentence.py](sentence.py)

### Making Sentence an Iterator: Bad Idea
Making an iterable and iterator over itself is a bad idea. It's an common anti-pattern.
- Use Iterator Pattern(Alex Martelli):
    - To access an aggregate objects contentes without exposing its internal representation.
    - To support multiple traversals of aggregate objects.
        - Possible to obtain multiple independent iterators from the same iterable instance.
            - which means create a new, independant, iterator.
    - To provide a uniform interface for traversing different aggregate structures.
- Example: [sentence_gen.py](sentence_gen.py)

### Making A Lazy Implementation
Istead of using token all the text by using `re.findall`, use `re.finditer` in `__iter__()`, Which may reduce memory consumption.
- Example: [sentence_gen2.py](sentence_gen2.py)
- Exampe2: [arthmethic_progress.py](arthmethic_progress.py)
### A Generator Expression
A generator expression can be understood as a lazy verion of a list comprehensions: It does not eagely build a list, but returns a generator that will lazily produce the items on demand.

- `(expression_for_vars for vals in expression...)`

- When to use? 
    - if the generator expression spans less than couple of lines, Use generator expression, else use generator function. 
- Example: [sentence_genexp.py](sentence_genexp.py)

### Generator Functions in the Standard Library
#### Fitering Function
| Module | Function | Description |
|:---:|:---:|:---|
|itertools| compress(it, selector_it) | Consumes two iterables in parallel; yields items from it whenever the corresponding item in selector_it is truthy.|
|itertools| dropwhile(predicate, it)|Consumes it skipping items while predicate computes truthy, then yields every remaining item (no further checks are made)|
|(built-in)|filter(predicate, it)|Appliespredicateto each item ofiterable, yielding the item ifpredi cate(item)is truthy; ifpredicateisNone, only truthy items are yielded|
|itertools|filterfalse(predi cate, it)|Same asfilter, with thepredicatelogic negated: yields items whenever predicate computes falsy|
|itertools|islice(it, stop) or islice(it, start, stop, step=1)|Yields items from a slice ofit, similar tos[:stop]or s[start:stop:step] except it can be any iterable, and the operation is lazy

- example code: 
    ```python
    import itertools

    #iter.compress
    >>> list(itertools.compress('hello', [1,1,1,0,0,]))
    ['h', 'e', 'l']

    #iter.dropwhile
    >>> li = [2,4,5,7,8] #Skip first 2,4
    >>> list(itertools.dropwhile(lambda x : x %2 == 0, li))
    [5, 7, 8]

    #filter
    >>> li = list(range(10))
    >>> list(filter(lambda x : x%2 ==0, li))
    [0, 2, 4, 6, 8]
    #itertools.filterfalse
    >>> list(itertools.filterfalse(lambda x : x%2 ==0, li))
    [1, 3, 5, 7, 9]

    #itertools.isslice
    >>> list(itertools.islice(range(10), 4)) #end
    [0, 1, 2, 3]
    >>> list(itertools.islice(range(10), 4,7)) #start end
    [4, 5, 6]
    >>> list(itertools.islice(range(10), 4,7,2)) #start end step
    [4, 6]
    ```
#### Mapping generator functions
| Module | Function | Description |
|:---:|:---:|:---|
|itertools|accumulate(it, [func])| Yields accumulated __sums__; if func is provided, yields the result of applying it to the first pair of items, then to the first result and next item, etc|
|built-in|enumerate(iterable, start=0)|Yields 2-tuples of the form (index, item), where index is counted from start, and item is taken from the iterable|
|itertools|starmap(func, it)|Applies func to each item of it, yielding the result; the input iterable should yield iterable items iit, and func is applied as func(*iit)|

- example: 
    ```python
    # mul
    >>> list(itertools.accumulate(range(1, 11)))
    [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    # maximum
    >>> list(itertools.accumulate(range(1, 11), max))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # factorial
    >>> list(itertools.accumulate(range(1, 11), operator.mul))
    [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    
    #enumerate
    >>> list(enumerate(('apple','bear','banana','orange','cherry'),1))
    [(1, 'apple'), (2, 'bear'), (3, 'banana'), (4, 'orange'), (5, 'cherry')]

    #map
    >>> list(map(lambda a, b: (a,b), range(3),('stone','paper','scissors')))
    [(0, 'stone'), (1, 'paper'), (2, 'scissors')]
    
    #starmap
    >>> list(itertools.starmap(lambda x,y : x+y, map(lambda x,y : (x,y), range(1,11), range(11,21))))
    [12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    ```

#### multiple input iterables
| Module | Function | Description |
|:---:|:---:|:---|
|itertools|chain(it1, ..., itN)|Yield all items from it1, then from it2 etc., seamlessly|
|itertools|chain.from_iterable(it)|Yield all items from each iterable produced by it, one after the other,seamlessly|
|itertools|product(it1, ..., itN, re peat=1)| yields N-tuples made by combining items from each input iterable like nestedforloops could produce; repeat allows the input iterables to be consumed more than once|
|(built-in)| zip(it1, ..., itN) | Yields N-tuples built from items taken from the iterables in parallel, silently stopping when the first iterable is exhausted |
|itertools|zip_longest(it1, ..., itN, fillvalue=None)|Yields N-tuples built from items taken from the iterables in parallel, stopping only when the last iterable is exhausted, filling the blanks with the fill value|


```python
#itertools.chain
>>> list(itertools.chain('ABC',[123,345],range(3)))
['A', 'B', 'C', 123, 345, 0, 1, 2]

#itertools.chain.from_iterable
list(itertools.chain.from_iterable(enumerate('ABC')))
[0, 'A', 1, 'B', 2, 'C']

#itertools.product , with repeat
>>> for x, y in itertools.product(range(1,10),range(1,10)):
...     print(f"{x}x{y} = {x*y}") #99단
1x1 = 1
1x2 = 2
1x3 = 3
...(omitted)
9x7 = 63
9x8 = 72
9x9 = 81

>>> list(itertools.product('ABC', repeat = 2))
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

#zip, itertools.ziplongest
>>> list(zip('ABC',range(5)))
[('A', 0), ('B', 1), ('C', 2)]
>>> list(itertools.zip_longest('ABC',range(5)))
[('A', 0), ('B', 1), ('C', 2), (None, 3), (None, 4)]
>>> list(itertools.zip_longest('ABC',range(5), fillvalue="Unset"))
[('A', 0), ('B', 1), ('C', 2), ('Unset', 3), ('Unset', 4)]
```
#### Expend input values 

|Module|Function|Description|
|:---:|:---:|:---|
|itertools|combination(it, out_len)|Yield combinations of out_len items from the items yielded by it|
|itertools|combinations_with_replacement(it, out_len)|Yield combinations of out_len items from the items yielded by it,including combinations with repeated items|
|itertools|count(start=0, step=1)|Yields numbers starting at start, incremented by step, indefinitely|
|itertools|cycle(it)|Yields items from it storing a copy of each, then yields the entire sequence repeatedly, indefinitely|
|itertools|permulations(it, out_len=None)|
|itertools|repeat(item, [times])|Yield the given item repeadedly, indefinetly unless a number of times is given|


```python
# itertools.combinations, itertools.combinations_with_replacement
>>> list(itertools.combinations('ABC', 2))
[('A', 'B'), ('A', 'C'), ('B', 'C')]
>>> list(itertools.combinations_with_replacement('ABC', 2))
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
>>> a =itertools.count(10, 2)
>>> next(a), next(a), next(a)
(10, 12, 14)

# itertools.cycle(unlimited)
>>> list(itertools.islice(itertools.cycle('ABCDE'), 10))
['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E']

# itertools.permulations(sequence)
>>> list(itertools.permutations('ABC',2))
[('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# itertools repeat
>>> list(itertools.repeat('abc',4))
['abc', 'abc', 'abc', 'abc']
```

#### Rearrageing generator functions
|Module| Function | Description |
|:---:|:---:|:---|
|itertools|groupby(it, key=None)|Yields 2-tuples of the form (key, group), where key is the grouping criterion andgroupis a generator yielding the items in the group|
|(built-in)|reversed(seq)|Yields items from seq in reverse order, from last to first; seq must be a sequence or implement the__reversed__special method.|
|itertools| tee(it, n=2) |Yields a tuple of n generators, each yielding the items of the input iterable independently |


```python
#itertools.groupby(it, key=len), built-in reversed
>>> fruits = ['apple', 'bear', 'banana', 'grape', 'orange', 'strawberry', 'blueberry','lemon','kiwi']
>>> fruits.sort(key=len)
>>> for length, group in itertools.groupby(reversed(fruits), len):
...     print(f"Lenght:{length} -> {list(group)}")
...
Lenght:10 -> ['strawberry']
Lenght:9 -> ['blueberry']
Lenght:6 -> ['orange', 'banana']
Lenght:5 -> ['lemon', 'grape', 'apple']
Lenght:4 -> ['kiwi', 'bear']

#itertools.tee
>>> x, y = itertools.tee(range(3),2) #generate n iters independently.
>>> next(x),next(x)
(0, 1)
>>> next(y)
0
>>> list(x),list(y)
([2], [1, 2])
```

#### Iterable Reducing Functions
|Module|Function|Description|
|:---:|:---:|:---|
|(built-in)| all(it) | Returns True if all items in it are truthy, otherwise False; all([]) returns True |
|(built-in)| any(it) | Returns True if any item in it is truthy, otherwise False; any([]) returns False |
|(built-in)| max(it, [key=,] [default=]) | Returns True if any item in it is truthy, otherwise False; any([]) returns False |
|functools|reduce(func, it, [initial]) | Returns the result of applying func to the first pair of items, then to that result and the third item and so on; if given, initial forms the initial pair with the first item |
|(built-in)|sum(it, start = 0) | The sum of all items in it, with the optional start value added (use math.fsum for better precision when adding floats)|

### A Closer Look at the iter Function
`iter` has another trick:

- `iter(func, stop_condition)`
    - The function pass to paramenter should not contain arguments.
    - Second argument is the stop conditi9on.

```python
number = 10

>>> def number_reducer():
...     global number
...     number -=1
...     return number
...
>>> reducer_iter = iter(number_reducer, 1)
>>> for roll in reducer_iter:
...     print(roll)
...
9
8
7
6
5
4
3
2
```

