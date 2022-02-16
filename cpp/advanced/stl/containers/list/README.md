# List in C++ STL
List is a sequnce container that allow non-contiguous memory allocation.
- Slow travelsal, but fast insertion and deletion.

## C++ list constructor
- empty constructor
- fill constructor
- range constructor
- copy constructor 

## C++ list function
|   Functions           |   Definition                                                      |
|   :---:               |   ---                                                             |
| `front()`             | value of the first element in the list.                           |
| `back()`              | value of the last element in the list.                            |
| `begin()`,`end()`     | point the first/last element of the iterator.                     |
| `cbegin()`,`cend()`   | point the first/last element of the constantiterator.             |
| `rbegin()`,`rend()`   | point the first last element of the reversed iterator.            |
| `crbegin()`,`crend()` | point the first last element of the reversed constant iterator.   |
| `push_back(e)`        | push the `e` to the last position.                                |
| `push_front(e)`       | push the `e` to the first position.                               |
| `pop_front()`         | removes the first element and reduces size of the list.           |
| `pop_back()`          | removes the last element and reduces size of the list.            |
| `empty()`             | return 1(empty) or 0(not empty)                                   |
| `insert(n)`           | insert the elements before the specific posistion `n`.            |
| `erase()`             | erase position element or range(first, last) elements.            |

