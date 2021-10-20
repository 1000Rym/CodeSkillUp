## How to use PDB to Debbuging python.
### Introduction.
- PDB: `P`ython`D`e`B`ugger
- module for interactive source code debugging.
- Built in to the Python Standard Library.
- CLI Debugging solution.

### How to use?

- Insert a single line of code into your code to set a breakpoint.

    ```python
    import pdb; 
    pdb.set_trace() # execution stops before the next line of code is executed.
    ```
    - If the environment is python>=3.7 we can also use the follwing code instead.

    ```python
    breakpoint()
    ```
- Post-mortem debugging will drop us into debugger automatically when an exception is hit.

    ```shell
    python3 -m pdb my_code.py
    ```

- Use breakpoint
    - Use `l` to move next breakpoint
    - Use `l .` to move back to first breakpoint
    - Use `ll` (long list) to see the function we are currtly in. 
    - Use `p` and variable to check the value: `p getattr(get_path, '__doc__')`

- Stepping through code:
    - Use `n` to move to next.  
    - Use `s` to move a step into the module.

- Working with breakpoint
    - Use `b module_name break_point_2_insert` to create a breakpoint: `b util:5`
    - Use `c` to continue execution. 
    - Use `b` to list up listed breakpoint. (listed breakpoint and hit time)
        - We can also add conditinal break point: `b util.get_path, not filename.startswith('/')`
    - Use `a` to list up the argument used.

- Continuing execution.
    - `UNT` is short for until.
        - __if supplied with a line number:__ `c`ontinue until that line number is reached. 
        - __if no line number is supplied:__ `n`ext(move forward) one line, not logically executed.
            - Difference between `n` is that, `UNT` will move one line until the logic is fully is finished, 
            - unlike `n` will go back to the previous line, when the current loop is not finished.

- Displaying Expression
    - use `display` to show variable.

- Stack Frames and Stack Traces
    - Print Stack state 
        - `w`(where) 
        - `u`(up stack)
        - `d`(down stack)

- Advance Tools: __pdb++__ 
    - PDB++(pdbpp) is an open source drop-in replacement for pdb that adds support for colorful output, sticky mode and other convenences. 
