# Vector
Same as the dynamic arrays, vector has the ability to resize itself automatically when an elment is inserted or deleted. 
- Resize itself automatically.
- Vector elements are placed in contiguous storage, which can be accessed and traversed using iterators.
- New data is inserted at the end.
- Remove last element takes only constant time.
- Inserting and erasing at the beginng or middle cost linear time.

## Constructor
Vector constructor([about_vector_constructor.cpp](about_vector_constructor.cpp))
1. Empty Container Constructor
1. Fill Constructor : Constructs a container with n elements(Each element is copy of val).
    ```cpp
    // Fill 10 5
    vector<int> vector_fill(5,10);
    ```
1. Range Constructor: Constructs a container with as many elements as the range [first, last).
    ```cpp
    // Range Constructor
    vector<int> vector_range(vector_fill.begin(), vector_fill.end());
    ```

1. Copy Constructor: Constructs a container with a copy of each of the elements in x, in the same order.
    ```cpp
    vector<int> vector_cp(vector_fill);
    ```

### Functions - Iterators
- `begin()`, `end()`: Returns an iterator pointing to the __first/last__ element. 
- `rbegin()`, `rend()`: Returns an __reverse__ iterator pointing to the __last/first__ element.
- `cbegin()`, `cend()`: Returns a __constant__ iterator pointing to the __first/last__ element.
- `crbegin()`, `crend()`: Returns a __revsered constant__ iterator poing to the __last/first__ element.

### Functions - Capacity
- `size()`: Returns the number of elements in the vector.
- `max_size()`: Returns the number of elements that the vector can hold.
- `capacity()`: Returns the size of the storage space currently allocated to the vector.
- `resize(n)`: Resize the containers to hold(n) elements, But not destroy other elements.
- `shrink_to_fit()`: Reduce the capacity of the container to fit its size, and destroy all elements beyond the capacity.
- `reserve()`: Requests that the vector capacity be at least enough to contain n elements.

### Elements access
- `[n]`(Reference Operator),`at(n)`: Returns a reference to a element at position n.
- `front()`, `back()`: Returns a reference to the __first/last__ element in the vector.
- `data()`: Returns a direct pointer to the memory array used internally by the vector to store its owned elements.

### Modifiers
- `assign()`: Assign a new value elements by replacing.
- `push_back()`: Push elements into a vector from back.
- `pop_back()`: Pop last elements from the vector.
- `insert()`: Inserts new elements before the element at the specified position.
- `erase()`: Remove elements from a container from specified poistion or range.
- `swap()`: Swap the contents of the vector with another vector of same type.
- `clear()`: Remove all the elements of the vector container.
- `emplace()`: Extends the container by inserting new elements at specific position.
- `emplace_back()`: Insert a new element into the vector container. Unlike `push_back()`, It will not create a temporary object implicitly.




