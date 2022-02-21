# List in C++ STL
List is a sequnce container that allow non-contiguous memory allocation.
- Slow travelsal, but fas insertion and deletion.

## C++ list constructor
- empty constructor
- fill constructor
- range constructor
- copy constructor 

## C++ list function            
|   Functions                       |   Definition                                                                      |
|   :---:                           |   ---                                                                             |
| `front()`                         | value of the first element in the list.                                           |
| `back()`                          | value of the last element in the list.                                            |
| `begin()`,`end()`                 | point the first/last element of the iterator.                                     |
| `cbegin()`,`cend()`               | point the first/last element of the constantiterator.                             |
| `rbegin()`,`rend()`               | point the first last element of the reversed iterator.                            |
| `crbegin()`,`crend()`             | point the first last element of the reversed constant iterator.                   |
| `push_back(e)`                    | push the `e` to the last position.                                                |
| `push_front(e)`                   | push the `e` to the first position.                                               |
| `pop_front()`                     | removes the first element and reduces size of the list.                           |
| `pop_back()`                      | removes the last element and reduces size of the list.                            |
| `empty()`                         | return 1(empty) or 0(not empty)                                                   |
| `insert(n)`                       | insert the elements before the specific posistion `n`.                            |
| `erase()`                         | erase position element or range(first, last) elements.                            |
| `assign()`                        | assign new elements to list by replacing current elements and resizes the list.   |
| `remove()`                        | remove target element if exist.                                                   |
| `remove_if()`                     | remove elements that fit the condition.                                           |
| `clear()`                         | remove all the elements in the list, and make the container size to 0.            |
| `reverse()`                       | reverse the list.                                                                 |
| `size()`                          | returns the number of elements in the list                                        |
| `resize()`                        | resize the container.                                                             |
| `sort()`                          | sorts the list in _incresing order_.                                              |
| `emplace_front() emplace_back()`  | insert the new element from front or back.                                        |
| operator `=`                      | assign and replacing new contents.                                                |
| `swap()`                          | swap to another list of same type and size. [Q1]                                  |
| `splice()`                        | used to transfer elements from one list to another.                               |
| `merge()`                         | merge two _sorted_ lists into one.                                                |
| `emplace()`                       | extends list by inserting new element at a given positin.                         |

## example code
[list_functions.cpp](list_functions.cpp)
## reference:
[List in C++ Standard Template Library (STL)](https://www.geeksforgeeks.org/list-cpp-stl/)

