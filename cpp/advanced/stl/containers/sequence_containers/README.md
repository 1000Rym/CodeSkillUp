# Sequence Container in C++ STL
Sequence containers are the containers taht access data in a sequential manner.
In C++, we consider __vector__, __list__, __deque__, __array__, __forward_list__ as the the sequential containers. In this page, we are going to summerize these containers.

## Concept
- __Array__: Array class which was introduced in C++11, knows its own size(no need to pass size of array as a separate parameter), it's more efficient, light-weight and reliable.
- __Vector__: Same as the dynamic arrays, vector has the ability to resize itself automatically when an elment is inserted or deleted.
    - Resize itself automatically.
    - Elements are placed in __contiguous storage__, 
    - Can be accessed and traversed using iterators.
    - New data is inserted at the end.
        - Remove last element takes only constant time.
        - Inserting and erasing at the beginng or middle cost linear time.
- __List__: Allow __non-contiguous__ memory allocation, Slow travelsal, but fas insertion and deletion.
- __Deque__: Double ended queue which allows insertion and deleteion in both ends. Unlike vector it might have non-contiguous memory.
- __forward_list__: Forward lists are implemented as singly-linked list(only point next element). Thus the lists are more efficient in forward iterables.

## C++ Sequential Container Constructors
- Constructor Tables
    |   Container Type                      |  Supported Constructor                        |
    |       :---:                           |          :---:                                |
    | list, vector,deque, forward_list      |  empty fill, range, copy, initilizer, move    |

- Constructor Explanation
    1. Empty Container Constructor
        ```cpp
        deque<int> my_deque;        
        ```
    1. Fill Constructor : Constructs a container with n elements(Each element is copy of val).
        ```cpp
        // Fill 10 5
        vector<int> vector_fill(5,10);
        ```
    1. Range Construcor: Constructs a container with as many elements as the range [first, last).
        ```cpp
        // Range Constructor
        vector<int> vector_range(vector_fill.begin(), vector_fill.end());
        ```
    1. Copy Constructor: Constructs a container with a copy of each of the elements in x, in the same order.
        ```cpp
        vector<int> vector_cp(vector_fill);
        ```
    1. Initilizer Constructor: Constructs a container with each of the elements in other container in the same order.
        ```cpp
        forward_list<int> first = {1,2,3,4,5};
        ```
    1. Move Constructor: `move()` other container's elements to construct the constructor.
        ```cpp
        // first: empty, second: 1 2 3 4 5 
        forward_list<int> first = {1,2,3,4,5};
        forward_list<int> second (move(first));
        ```


## C++ Sequenctial Container Functions

### C++ Container's Iterator Functions
|   Functions           | Supported Containers          |   Description                                                                 |
|   :---:               |   :---:                       |   :---                                                                        |
| `begin()`, `end()`    | array, vector, list, deque    | Return an iterator pointing to the __first/last__ element.                    |
| `cbegin()`, `cend()`  | array, vector, list, deque    | Return a __constant__ iterator pointing to the __first/last__ element.        |
| `rbegin()`, `rend()`  | array, vector, list, deque    | Return an __reverse__ iterator pointing to the __last/first__ element.        |
| `crbegin()`, `crend()`| array, vector, list, deque    | Return a __revsered constant__ iterator poing to the __last/first__ element.  |
| `before_begin()`      | forward_list                  | Return the iterator to before beginning.                                      |
| `cbefore_begin()`     | forward_list                  | Return the constant iterator to before beginning.                             |  
- Example Code: [iterator_functions.cpp](examples/iterator_functions.cpp)

### C++ Container's Capacity Functions
|   Functions           | Supported Containers                      |   Description                                                                                          |
|   :---:               |   :---:                                   |   :---                                                                                                 |
| `empty()`             | array, vector, list, deque, forward_list  | Return 1(empty) or 0(not empty)                                                                        |
| `max_size()`          | array, vector, list, deque, forward_list  | Return the number of elements that the container can hold.                                             |    
| `size()`              | array, vector, list, deque                | Return the number of elements in the container.                                                        |
| `resize()`            | vector, deque, forward_list               | Resize the containers to hold(n) elements, But not destroy other elements.                             |
| `capacity()`          | vector, deque                             | Return the size of the storage space currently allocated to the container.                             |
| `reserve()`           | vector, deque                             | Request that the container capacity be at least enough to contain n elements.                          |
| `shrink_to_fit()`     | vector, deque                             | Reduce the capacity of the container to fit its size, and destroy all elements beyond the __capacity__.|
- Example Code: [capacity_functions.cpp](examples/capacity_functions.cpp)

### C++ Container's Elements Access Functions
|   Functions                       | Supported Containers          |   Definition                                                                                              |
|   :---:                           |   :---:                       |   :---                                                                                                    |
| `front()` and `back()`            | array, vector, list, deque    | Return a reference to the __first/last__ element in the container.                                        |
| Reference Operator: `[n]`,`at(n)` | array, vector, deque          | Return a reference to the element at position n.                                                          |
| `data()`                          | array, vector                 | Return a direct pointer to the memory array used internally by the container to store its owned elements. |
| `front()`                         | forward_list                  | Access the first elements.                                                                                |
- Example Code: [element_access_functions.cpp](examples/element_access_functions.cpp)

### C++ Container's Modifier Functions
|   Functions       | Supported Containers                      |   Description                                                                                     |
|   :---:           |   :---:                                   |   :---                                                                                            |
| `fill()`          | array                                     | Fill the values.                                                                                  |
| `swap()`          | array, vector, list, deque, forward_list  | Swap to another container of same type .                                                          |
| `assign()`        | vector, list, deque, forward_list         | Assign the container content.                                                                     |
| `push_back()`     | vector, list, deque                       | Add the element into a container from back.                                                       |
| `pop_back()`      | vector, list, deque                       | Pop the last element from the container.                                                          |
| `emplace_back()`  | vector, list, deque                       | Insert a new element into the back of the container(Not create temporary object implicitly).      |
| `emplace()`       | vector, list, deque                       | Insert a new element at specific position(Not create temporary object implicitly).                |
| `insert()`        | vector, list, deque                       | Insert new elements before the element at the specified position.                                 |
| `erase()`         | vector, list, deque                       | Remove elements from a container from specified poistion or range.                                |
| `clear()`         | vector, list, deque                       | Remove all elements from the container container.                                                 |
| `push_front()`    | list, deque, forward_list                 | Push the new element to the first position.                                                       |
| `pop_front()`     | list, deque, forward_list                 | Remove the first element and reduces size of the container.                                       |
| `emplace_front()` | list, deque, forward_list                 | Insert a new element into the front of the container(Not create temporary object implicitly).     |
| `emplace_after()` | forward_list                              | Insert a new element into the after the current container(Not create temporary object implicitly).|
| `insert_after()`  | forward_list                              | Insert new elements before the element at the specified position.                                 |
| `erase_after()`   | forward_list                              | Remove elements from a container from specified poistion or range.                                |

- Example Code: [modifier_functions.cpp](examples/modifier_functions.cpp)

### C++ Container's Operations Functions
|   Functions       | Supported Containers  |   Description                                 |
|   :---:           |   :---:               |   :---                                        |
| `splice()`        | list                  | Transfer elements from one list to another.   |
| `splice_after()`  | forward_list          | Transfer elements from one list to another.   |
| `remove()`        | list, forward_list    | Remove target element(s) if exist.            |
| `remove_if()`     | list, forward_list    | Remove elements that fit the condition.       |
| `unique()`        | list, forward_list    | Remove duplicate values.                      |
| `merge()`         | list, forward_list    | Merge two _sorted_ lists into one.            |
| `sort()`          | list, forward_list    | Sort the list(default _incresing order_).     |
| `reverse()`       | list, forward_list    | Reverse the container.                        |
- Example Code: [operation_functions.cpp](examples/operation_functions.cpp)

### C++ Container's Allocator(Observer) Function
|   Functions       | Supported Containers              |   Description     |
|   :---:           |   :---:                           |   :---            |
| `get_allocator()` | vector, list, deque, forward_list | Get an allocator. |
- Example Code: [allocation_function.cpp](examples/allocator_function.cpp)

### C++ Container's Non-member function overloads
|   Functions               | Supported Containers                      |   Description                             |
|   :---:                   |   :---:                                   |   :---                                    |
| `get<index>(container)`   | array                                     | Get an element from the container.        |
| __relational operators__  | array, vector, list, deque, forward_list  | Relational Operations for the container.  |  
| `swap(container)`         | vector, list, deque, forward_list         | Relational Operations for the container.  |
- Example Code: [non_member_function_overloads.cpp](examples/non_member_function_overloads.cpp)

### C++ Container's Non-member class specializations
|   Functions               | Supported Containers          |   Description                             |
|   :---:                   |   :---:                       |   :---                                    |
| `tuple_element<container>`| array                         | Tuple element type for the container.     |
| `tuple_size<container>`   | array                         | Tuple size traits for the container.      |


## Reference:
- Array
    - [Array class in C++](https://www.geeksforgeeks.org/array-class-c/)
    - [cplusplus.com: array](https://www.cplusplus.com/reference/array/array/)
- List 
    - [List in C++ Standard Template Library (STL)](https://www.geeksforgeeks.org/list-cpp-stl/)
    - [cplusplus.com: list](https://www.cplusplus.com/reference/list/list/)
- Vector
    - [Vector in C++ Standard Template Library (STL)](https://www.geeksforgeeks.org/vector-in-cpp-stl/)
    - [cplusplus.com: vector](https://www.cplusplus.com/reference/vector/vector/)
- Deque
    - [Deque in C++ Standard Template Library (STL)](https://www.geeksforgeeks.org/deque-cpp-stl/)
    - [cplusplus.com: deque](https://www.cplusplus.com/reference/deque/deque/)
- Forward List 
    - [Forward List in C++ Standard Template Library (STL)](https://www.geeksforgeeks.org/forward-list-c-set-1-introduction-important-functions/)
    - [cplusplus.com: forward_list](https://www.cplusplus.com/reference/forward_list/forward_list/)

