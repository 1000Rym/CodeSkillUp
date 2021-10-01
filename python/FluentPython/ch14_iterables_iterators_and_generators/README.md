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

    ````
