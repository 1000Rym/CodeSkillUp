# Python Modules and Packages
## Advantages of modularizing
modular programming
- Simplicity
- Maintainability
- Reussability
- Scoping: sperate __namespace__

- The interpreter searches for the file.
    - current directory
    - `PYTHONPATH`
    - installation-depenent list of directories.

- Append new path.
    - Append 
        - Append new path can be easiliy done with `sys.path.append(r'path')`
        - However, this path can be removed once session is finished.
    - Search imported module
        - module2search`.__file__` to see path of the module.

### import statement
- `import module`
    - `import module as module_name`
- `from module import object`
    - `from moudle import object as object_name`
    - `from module import *`
- module can be imported in funtion 
    - Only available in fuction. 
    - Can not use `*`(can only be used in top module)
- module `import` with `try`...`except`... 
    - avoid the exception

### reload modulle
- `importlib.reload()`

### Package Initilization
- The `__init__.py` file.
    - If a file named `__init__.py` is pressent in a package directory, it is invoked when the package or a module in the package is imported.
    - `__init__py` can also be used to automatically import the modules from a pacakge.
    - `__all__` list controls what is imported when `import *` is specified
        - For the package `__all__` is not defined, `import *` does not import anything.
        - For a module, when `__all__` is not defined, `import *` imports everything(except names starting with an underscore)

## Subpacakge 
Use `..` to go relatively parent path of current module's directory.
Use `.` to access current dir path.

### Example Code.
- pkg
    - [`__init__.py`](pkg/__init__.py)
    - sub_pkg1
        - [`__init__.py`](pkg/sub_pkg1/__init__.py)
        - [mod1.py](pkg/sub_pkg1/mod1.py)
        - [mod2.py](pkg/sub_pkg1/mod2.py)
     - sub_pkg2
        - [`__init__.py`](pkg/sub_pkg2/__init__.py)
        - [mod3.py](pkg/sub_pkg2/mod3.py)
        - [mod4.py](pkg/sub_pkg2/mod4.py)