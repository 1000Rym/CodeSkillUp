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

