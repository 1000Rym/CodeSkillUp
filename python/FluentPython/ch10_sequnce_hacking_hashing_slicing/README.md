## Chapter10: Sequence Hacking, Hashing, and Slicing

Features:
- Representation of instances with many items
- Basic Sequence Protocal: `__len__` and `__get_item__`
- Slicing
- Hashing
- Custom formatting extension

### Representing of instances with many items
- Use `reprlib.repr()` could abbriviated with `...`
    - example code: [vector_v1.py](vector_v1.py)

### Basic Sequence Protocal
To implement sequence protocal, implement one of `__getitem__()` and `__len()__`. To support iteration only `__getitem__()` is required.
