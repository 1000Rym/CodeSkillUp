# Container Adaptors in C++ STL
Container adapters are made for providing a different interface for sequential containers. And they are `queue`, `priority_queue`, and `stack`.

## Concept
- __stack__: Designed to operate a LIFO context, where elements are inserted and extracted only from _end_ of the container.
- __queue__: Designed to operate a FIFO context. Elements are pushed into the _back_ and popped from the _front_.
- __priority_queue__: Designed that the first element of the queue is the greatest of all elements in the queue and elements are in descending order.

### C++ Container Adapter Constrcutor
- Constructor Tables
    |   Container Type                      |  Supported Constructor                                                            |
    |       :---:                           |          :---:                                                                    |
    | stack, queue, priority_queue          | initialization, range, move-intialization, move-range initialization, allocator   |
    | stack, queue                          | initilization with allocator, move-initialization with allocator                  |


### C++ Container Adapter - Member Functions
|   Functions   | Container Type                |  Description                                                                                  | 
|   :---:       |   :---                        |  :---                                                                                         |
| `empty()`     | stack, queue, priority_queue  | Return whether the container is empty.                                                        |
| `size()`      | stack, queue, priority_queue  | Return the size of the container.                                                             |
| `swap()`      | stack, queue, priority_queue  | Exchange the contentes of the queue(same type).                                               |
| `push()`      | stack, queue, priority_queue  | Adds the element at the the container(stack: last, queue: first, priority: decending order).  |
| `emplace()`   | stack, queue, priority_queue  | Adds the element at the the container(stack: last, queue: first, priority: decending order).  |      
| `pop()`       | stack, queue, priority_queue  | Delete the front(queue) or top(stack) most element of the container.                          |
| `top()`       | stack, priority_queue         | Access the top(last) element.                                                                 |
| `front()`     | queue                         | Access the front most element.                                                                |
| `back()`      | queue                         | Access the last most element.                                                                 |
- Example Code: [container_adapter_method_functions.cpp](../example_code/container_adapter_method_functions.cpp)

### C++ Container Adapter - Non-member function overloads
|   Functions               | Container Type                |  Description                              | 
|   :---:                   |   :---                        |  :---                                     |
| `swap()`                  | stack, queue, priority_queue  | Exchange the same type container.         |
| __relational operators__  | stack, queue                  | Relational operators for the container.  | 
- Example Code: [non_member_function_overloads.cpp](../example_code/non_member_function_overloads.cpp)

## Reference
- Stack
    - [cplusplus.com: std::stack](https://www.cplusplus.com/reference/stack/stack/stack/)
    - [GeeksForGeeks: Stack in C++ Standard Template Library (STL)](https://www.geeksforgeeks.org/stack-in-cpp-stl/)
- Queue
    - [cplusplus.com: std::queue](https://www.cplusplus.com/reference/queue/queue/)
    - [GeeksForGeeks: Queue in C++ Standard Template Library (STL)](https://www.geeksforgeeks.org/queue-cpp-stl/)
- Priority Queue
    - [GeeksForGeeks: Priority Queue in C++ Standard Template Library (STL)](https://www.geeksforgeeks.org/priority-queue-in-cpp-stl/?ref=rp)
    - [cplusplus.com: std::priority_queue](https://www.cplusplus.com/reference/queue/priority_queue/)