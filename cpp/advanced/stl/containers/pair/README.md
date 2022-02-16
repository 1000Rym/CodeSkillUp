# Pair
Pair is used to combine together two different type values. 
- To storeheterogeneous objects as a sigle unit.
- Defined in `<utility>` header.
- First element referenced as the `first`, second element is referenced as `second`.
- Can be assigned, copied, and compared. Mostly used in `map` or `hash_map`. 
    - `first` value is `key`.
    - `second` value is `value`.

## Pairs' Constructor and declaration
- Default constructor:
    ```cpp
    pair<string, int> pair1;
    pair1 = make_pair("Bill", 18);
    ``` 
- Initialization constructor:
    ```cpp
    pair<string, int> pair2("Tommy", 20);
    ```
- Copy Constructor
    ```cpp
    pair<string, int> pair3(pair2);
    ```

- Another way to declare `pair`
    ```cpp
    pair <string, int> pair4 = {"Phonix", 23};
    ```

### Functions in Pair
- `make_pair()`: create a value pair without writing the type explicitly.
- `swap()`: swap contents of pair to the another object.
- `tie()`: creates a tuple of lvalue references to its arguments.
     - `tie(int &, int &) = pair1;` 
- example code: 


## Reference 
- About pairs' constructor: https://www.cplusplus.com/reference/utility/pair/pair/
- Pair introduced in GeeksforGeeks: [Pair in C++ Standard Template Library (STL)
](https://www.geeksforgeeks.org/pair-in-cpp-stl/)