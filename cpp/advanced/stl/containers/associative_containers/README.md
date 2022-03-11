# Associative Containers.
Implement unordered or sorted data structures that can be quickly searched which have Big O's logn complexity.
- Ordered: __set__, __multi_set__, __map__, __multimap__.
- Unordered: __unordered_set__, __unordered_multiset__, __unordered_map__, __unordered_multimap__.

## C++ Associative Containers Concept
- Ordered Associative Container: 
    - __set__: Set which implemented with __BST__ have __unique__, __sorted ordered__, but __uunindexed__, and  __immutable__ elements. 
    - __multiset__: Multiset is similar with set with exception that multiple elements can have the same values.


## C++ Associative Constructors
- Constructor Tables
    |   Container Type                      |  Supported Constructor                        |
    |       :---:                           |          :---:                                |
    | set, multiset                         |  empty , range, copy, initilizer, move        |

## C++ Associative Container Functions

### C++ Container's Iterator Functions
|   Functions           | Supported Containers          |   Description                                                                 |
|   :---:               |   :---:                       |   :---                                                                        |
| `begin()`, `end()`    |set, multiset | Return an iterator pointing to the __first/last__ element.                    |
| `cbegin()`, `cend()`  |set, multiset | Return a __constant__ iterator pointing to the __first/last__ element.        |
| `rbegin()`, `rend()`  |set, multiset | Return an __reverse__ iterator pointing to the __last/first__ element.        |
| `crbegin()`, `crend()`|set, multiset | Return a __revsered constant__ iterator poing to the __last/first__ element.  |
- Example Code: [iterator_functions.cpp](examples/iterator_functions.cpp)




## Reference
- About __set__:
    - [GeeksForGeeks: Set in C++ Standard Template Library (STL)](https://www.geeksforgeeks.org/set-in-cpp-stl/)
    - [cplusplus.com: set](https://www.cplusplus.com/reference/set/set/)
    
- About __multiset__:
    - [GeeksForGeeks: Multiset in C++ Standard Template Library (STL)](https://www.geeksforgeeks.org/multiset-in-cpp-stl)
    - [cplusplus.com: multiset](https://www.cplusplus.com/reference/set/multiset/)