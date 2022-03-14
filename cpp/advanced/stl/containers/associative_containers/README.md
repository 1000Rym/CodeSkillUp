# Associative Containers
Implement unordered or sorted data structures that can be quickly searched which have Big O's logn complexity.
- Ordered: __set__, __multi_set__, __map__, __multimap__.
- Unordered: __unordered_set__, __unordered_multiset__, __unordered_map__, __unordered_multimap__.

## C++ Associative Containers Concept
- Ordered Associative Container: 
    - __set__: Set which implemented with __BST__ have __unique__, __sorted ordered__, but __unindexed__, and  __immutable__ elements(BigO(LogN)). 
    - __multiset__: Multiset is similar with set with exception that multiple elements can have the same values.
    - __map__: Store the element in mapped fashion(_key_ and _mapped value_), It stores value with the __key sorted__.  
    - __multimap__ : Similar with the __map__ with addition that multiple elements can have the same keys.

- Unordered Associate Container:
    - __unordered_set__: _unordered_set_ is implemented with using a hash table, __unordered__ mean's that the key can be stored in any order, __Faster than the set__ (BigO(LogN)),the time complexity just cost BigO(1). 
    - __unordered_multiset__:  Much like __unordered_set__, but allowing different elemetns to have equaivalent values.
    - __unordered_map__: Store the element in mapped fashion(_key_ and _mapped value_), It stores value with __unsorted__.
    - __unordered_multimap__: Similar with __unordered_map__, but it allows different elements have equivalent keys.


## C++ Associative Constructors
- Constructor Tables
    |   Container Type                                                                                      |  Supported Constructor        |
    |       :---:                                                                                           |          :---:                |
    | set, multiset, unordered_set, unordered_multiset, unordered_map, unordered_multimap, map, multimap    |  empty , range, copy          |  
    | set, multiset, unordered_set, unordered_multiset, unordered_map, unordered_multimap                   |  initilizer, move             |

## C++ Associative Container Functions
### C++ Associative Container's Iterator Functions
|   Functions           | Supported Containers                                                                                 |   Description                                                                  |
|   :---:               |   :---:                                                                                              |   :---                                                                         |
| `begin`, `end`        |set, multiset, unordered_set, unordered_multiset, map, multimap, unordered_map, unordered_multimap    | Return an iterator pointing to the __first/last__ element.                     |
| `cbegin`, `cend`      |set, multiset, unordered_set, unordered_multiset, map, multimap, unordered_map, unordered_multimap    | Return a __constant__ iterator pointing to the __first/last__ element.         |
| `rbegin`, `rend`      |set, multiset, map, multimap                                                                          | Return an __reverse__ iterator pointing to the __last/first__ element.         |
| `crbegin`, `crend`    |set, multiset, map, multimap                                                                          | Return a __revsered constant__ iterator poing to the __last/first__ element.   |
- Example Code: [iterator_functions.cpp](../example_code/iterator_functions.cpp)

### C++ Associative Container's Capacity Functions
|   Functions   | Supported Containers                                                                                |   Description                                                 |
|   :---:       |   :---:                                                                                             |   :---                                                        |
| `empty`       | set, multiset, unordered_set, unordered_multiset, map, multimap, unordered_map, unordered_multimap  | Return 1(empty) or 0(not empty).                              |
| `size`        | set, multiset, unordered_set, unordered_multiset, map, multimap, unordered_map, unordered_multimap  | Return the number of elements in the container.               |
| `max_size`    | set, multiset, unordered_set, unordered_multiset, map, multimap, unordered_map, unordered_multimap  | Return the number of elements that the container can hold.    |
- Example Code: [capacity_functions.cpp](../example_code/capacity_functions.cpp)

### C++ Associate Container's Element Lookup(Operation) Functions.
|   Functions       | Supported Containers                                                                                  |   Description                         |
|   :---:           |   :---:                                                                                               |   :---                                |
| `find`            | set, multiset, unordered_set, unordered_multiset, map, multimap, unordered_map, unordered_multimap    | Get iterator to the target element.   |
| `count`           | set, multiset, unordered_set, unordered_multiset, map, multimap, unordered_map, unordered_multimap    | Count elements with the target value. |
| `equal_range`     | set, multiset, unordered_set, unordered_multiset, map, multimap, unordered_map, unordered_multimap    | Get range of the equal elements.      |
| `lower_bound`     | set, multiset, map, multimap                                                                          | Return iterator to lower bound.       |   
| `upper_bound`     | set, multiset, map, multimap                                                                          | Return iterator to upper bound.       |
- Example Code: [element_lookup_functions.cpp](../example_code/element_lookup_functions.cpp)

### C++ Associate Container's Observers(Allocator) Functions
|   Functions       | Supported Containers                                                                                  |   Description                         |
|   :---:           |   :---:                                                                                               |   :---                                |
| `get_allocator`   | set, multiset, unordered_set, unordered_multiset, map, multimap, unordered_map, unordered_multimap    | Get an allocator.                     |
| `hash_function`   | unordered_set, unordered_multiset , unordered_map, unordered_multimap                                 | Get hash function.                    |
| `key_eq`          | unordered_set, unordered_multiset , unordered_map, unordered_multimap                                 | Checking hash key's equality.         |
| `key_comp`        | set, multiset, map, multimap                                                                          | Return _key_ comparison object.       |
| `value_comp`      | set, multiset, map, multimap                                                                          | Return _value comparison obecjt.      | 
- Example Code: [observer_functions.cpp](../example_code/observer_functions.cpp) 

### C++ Associate Container's Bucket Functions
|   Functions           | Supported Containers                                                  |   Description                                             |
|   :---:               |   :---:                                                               |   :---                                                    |
| `bucket_count`        | unordered_set, unordered_multiset, unordered_map, unordered_multimap  | Return number of the buckets.                             |
| `max_bucket_count`    | unordered_set, unordered_multiset, unordered_map, unordered_multimap  | Return maximum number of the buckets.                     |
| `bucket_size`         | unordered_set, unordered_multiset, unordered_map, unordered_multimap  | Return the number of the elements in the bucket(n).       |
| `bucket`              | unordered_set, unordered_multiset, unordered_map, unordered_multimap  | Return the bucket number where the element is located.    |
- Example Code: [bucket_functions.cpp](../example_code/bucket_functions.cpp) 

### C++ Associate Container's Hash Policy Functions
|   Functions           | Supported Containers                                                  |   Description                                                                     |
|   :---:               |   :---:                                                               |   :---                                                                            | 
| `load_factor`         | unordered_set, unordered_multiset, unordered_map, unordered_multimap  | Return the load factor.                                                           |
| `max_load_factor`     | unordered_set, unordered_multiset, unordered_map, unordered_multimap  | Get/Set the maximum load factor.                                                  |
| `rehash`              | unordered_set, unordered_multiset, unordered_map, unordered_multimap  | Set the number of the buckets.                                                    |
| `reserve`             | unordered_set, unordered_multiset, unordered_map, unordered_multimap  | Set the number of buckets to the most appropriate to contain at lease n elements. |
- Example Code: [hash_policy_functions.cpp](../example_code/hash_policy_functions.cpp)

### C++ Associate Container's Element Access Functions
|   Functions               | Supported Containers  |   Description                     |
|   :---:                   |   :---:               |   :---                            |
| operator`[key]`, `at(key)`| map, unordered_map    | Access the element at target key. |             
- Example Code: [element_access_functions](../example_code/element_access_functions.cpp)


### C++ Associate Container's Modifier Functions
|   Functions                       | Supported Containers                                                                                 |   Description                                 |
|   :---:                           |   :---:                                                                                              |   :---                                        |
| `insert`                          | set, multi_set, unordered_set, unordered_multiset, map, multimap, unordered_map, unordered_multimap  | Insert the elements.                          |
| `erase`                           | set, multi_set, unordered_set, unordered_multiset, map, multimap, unordered_map, unordered_multimap  | Erase the elements.                           |          
| `swap`                            | set, multi_set, unordered_set, unordered_multiset, map, multimap, unordered_map, unordered_multimap  | Swap the content of the container.            |
| `clear`                           | set, multi_set, unordered_set, unordered_multiset, map, multimap, unordered_map, unordered_multimap  | Clear the content of the container.           |
| `emplace`                         | set, multi_set, unordered_set, unordered_multiset, map, multimap, unordered_map, unordered_multimap  | Construct and insert the element.             |
| `emplace_hint(position_it, args)` | set, multi_set, unordered_set, unordered_multiset, map, multimap, unordered_map, unordered_multimap  | Construct and insert the element with hint.   |
- Example Code: [associate_container_modifier_functions.cpp](../example_code/associate_container_modifier_functions.cpp)


## Reference
- Ordered Associate Container: 
    - About __set__:
        - [GeeksForGeeks: Set in C++ Standard Template Library (STL)](https://www.geeksforgeeks.org/set-in-cpp-stl/)
        - [cplusplus.com: set](https://www.cplusplus.com/reference/set/set/)    
    - About __multiset__:
        - [GeeksForGeeks: Multiset in C++ Standard Template Library (STL)](https://www.geeksforgeeks.org/multiset-in-cpp-stl)
        - [cplusplus.com: multiset](https://www.cplusplus.com/reference/set/multiset/)
    - About __map__:
        - [GeeksForGeeks: Map in C++ Standard Template Library (STL)](https://www.geeksforgeeks.org/map-associative-containers-the-c-standard-template-library-stl/)
        - [cplusplus.com: map](https://www.cplusplus.com/reference/map/map/)    
    - About __multimap__:
        - [GeeksForGeeks: Multimap in C++ Standard Template Library (STL)](https://www.geeksforgeeks.org/multimap-associative-containers-the-c-standard-template-library-stl/)
        - [cplusplus.com: multimap](https://www.cplusplus.com/reference/map/multimap/)


    
- Unordered Assocciate Container:
    - About __unordered_set__:
        - [GeeksForGeeks: Unordered Set in C++ Standard Template Library (STL)](https://www.geeksforgeeks.org/unordered_set-in-cpp-stl/)
        - [cplusplus.com: unordered_set](https://www.cplusplus.com/reference/unordered_set/unordered_set/)
    - About __unordered_multi_set__: 
        - [cplusplus.com: unordered_multi_set](https://www.cplusplus.com/reference/unordered_set/unordered_multiset/)
    - About __unordered_map__:
        - [GeeksForGeeks: Unordered Map in C++ Standard Template Library (STL)](https://www.geeksforgeeks.org/unordered_map-in-cpp-stl/)
        - [cplusplus.com: unordered_map](https://www.cplusplus.com/reference/unordered_map/unordered_map/)
    - About __unordered_multi_set__: 
        - [cplusplus.com: unordered_multimap](https://www.cplusplus.com/reference/unordered_map/)

