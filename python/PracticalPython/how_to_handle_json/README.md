# How to handle JSON in Python?
### About JSON
__JSON__ stands for JavaScript Object Notation.
- lightweight data-interchange format that used to store and exchange data. 
- language-independent format.
- consisting of key-value mapping enclosed between curly brackets`{}`.
- we can use `json` built-in package in python.

### JSON Method
- `json.loads(s)`: Returns a dictionary type converted python object, `s` can be a string, bytes, or byte array instance.
- `json.load(file)`: Returns a dictionary type converted python object from json file.
- `json.dumps()` : Converts python object into a json string, the function have the folllowing parameters.
    - `obj`: python object to serialized to convert.
    - `skipkeys`: dict keys that are not of a basic type (str, int, float, bool, None) will be skipped instead of rising error(default=`False`).
    - `ensure_ascii`: all incomming non-ASCII characters escaped(default=`True`).
    - `check_circular` the circular reference check for container types will be skipped, and a circular reference will result in OverflowError(deafault=`False`)
    - `indent`:  used for pretty printing.
    - `allow_nan`: if `allow_nan` is false  then it will be a ValueError to serialize out of range float values `(nan, inf, -inf)`(default = `True`)
    - `separators`: define separators with `(item_separator, key_separator)` tuple(default is `(',' , ':' )`).
    - `default`: function that gets called for serialize the object.
    - `sort_keys` : the output of dictionaries will be sorted by key(default=`False`).

- Example Code: [how_to_handle_json.py](how_to_handle_json.py)

## Reference
- [GeeksforGeeks: json.load() in Python
](https://www.geeksforgeeks.org/json-load-in-python/)
- [GeeksforGeeks: json.loads() in Python
](https://www.geeksforgeeks.org/json-loads-in-python/)
- [GeeksforGeeks: json.dumps() in Python
](https://www.geeksforgeeks.org/json-dumps-in-python/)