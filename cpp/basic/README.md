# CPP Basic
## What is the CPP?
C++ is a middle-level language rendering it the advantage of programming low-level(drivers, kernels) to higher-level applications(games, GUI, desktop, etc).
- Features:
    - Mid-level Language
    - Speed of execution
    - Compiled Language
    - Machine Independent but platform dependent
        - Compiled programs on Linux won't run on Windows.
    - Rich Library support(standard, 3rd-party)
    - Pointer and direct Memory-Access
    - Object-Oriented 
- Applications:
    - OS & System Programming
    - Browsers, Graphics & Game engines
    - Database Engines
    - Cloud/Distributed System

## How to compile in CPP?
- Make binary files. 
    ```shell
    g++ -o output_name hello_world.cpp
    ```
- Execute the binary executable file.
    ```shell
    ./output_name
    ```
- Example Code: [hello_world.cpp](hello_world.cpp)

## Basic Input/Output in CPP.
- Input Stream:The direction of flow bytes is from device(Keyboard) to the main memory.
- Output Stream: The direction of flow of bytes is from main memory to the device(display screen).

### Header files for Input/Output Operations.
- iostream: Standard IO stream(`cin`, `cout`, `cerr`, `clog`).
    - `cin`: standard input stream, Often using with extraction operator(`>>`)
    - `cout`: standard output stream, Using with insertion operator(`<<`)
    - `cerr`: Un-buffered standard error stream, Not stored in buffer.
        - Immediatly show the error messmage.
    - `clog`: Buffered standard error stream, The error message, first stored in to the buffer.
    - example_code: [ex01_iostream.cpp](ex01_iostream.cpp)
- iomainip: IO manipulators(`setw`, `setprecision`). 
- fstream: File stream, Do read and write operatrion(`ifstream`, `ofstream`)

### Comments in C++
Comments are statements that are not executed by the compiler and interpreter, but to give explation or anotion.
```cpp
// Single Line Comment

/*
Multi-Line Comment.
 First Line.
 Second Line.
*/
```

### Data Types
Data types in C++ is mainly divided into 3 types. Those are primitive, derived,  user defined.

### Primitive Data Types
Built-in or predefiend data types and can be used directly byt the user to declare variables.
- Integer(`int`, or `unsigned int`) : 4 bytes.
    - `short [int]` or `unsigned short [int]`: 2 bytes.
    - `long [int]` or `unsigned long [int]`: 4 bytes or 8 bytes(Based on OS).
    - `long long [int]` or `unsinged long long[int]` : 8 bytes.
- Character(`char`) : 1 byte.
    - `signed char` or `unsigned char`
- Boolean(`bool`): `true` or `false`.
- Floating Point(`float`): 4 bytes.
- Double Floating Point(`double`): 8 bytes.
    - `long double` 12 bytes.
- Valueless or Void(`void`): valueless entity. 
- Wide-Character: (`wchar_t`)2-4 bytes.

#### Uninitialized primitive data types in C/C++
Note that C++ will not initilize the default value to the declared value.
- The overhead of initilizing a stac variable is costly as it hampers the speed of execution,therefore these variables can contain indeterminate values.
- It is considered as a best pracitce to initialize a primitve data type variable before using it in code.


### Derived Data Types
The data-types that are derived from the primitive or biult-in datatypes.
- Function
- Array
- Pointer
- Reference

### Abstractor or User-Defined Data Types
The datatypes that are defined by users.
- Class
- Structure
- Union
- Enumeration
- Typedef defined DataType

## Variables in C++
A variable is a name given to a memory location. 
- The values stored in a variable can be changed during the program execution. 
- In C++, all the variables must be declared before use.

### Difference between variable declaration and definition.
- __variable declaration__: A variable is first declared or introduced before its first use.
- __variable definition__: variable is assinged a memory location and value.
- Most of times variable declaration and variable definition are done together.

### Types of the variables
- __Local Variables__: A variable defined within a block or method or constructor. 
    - Created when the block in entered or the function is called, destroyed after existing from the block or when the call returns form the fucntions.
    - Mandatory to instantiation the variable.
- __Instance Variables__: Instance variables are non-static variables and are declared in a class outside any method, constructor or block. 
    - Declared in a class, created when an object of the class created and destroyed when the object is destroyed.
    - If we do not specify any acess specifier then the default acess specifier will be used.
    - Not mandatory to instantiation the variable.
    - The instance variable can only be accessed by creating objects.
- __Static Variables__: Class variable.
    - Delcalared using the `static` keyworld within a class outside any method constructor or block.
    - Can only have one copy of the static variable per class.
    - Not mandatory to instantiation the variable.

### Scope of the variable in C++
- __Local Variables__: Variables defined within a function or block.
- __Global Variables__: Global Variables can be accessed from any part of the program.
    - They are available through out the life time of a program.
    - Declared at the __top of the program outside all of the functions or blocks__.
- Example Code for global variable and local variable.
    ```cpp
    #include <iostream>
    using namespace std; 

    int var = 10;

    int main(){
        // unlike python global variable can be accessed without declare a global keyword.
        var = 12;

    ¸   // we declare a local variable which have same name with glboal variable.
        int var = 20; 

        // the variable is pointing local variable.
        cout << var <<  endl;

        // To point global variable we need to add "::"
        cout << ::var<< endl;

        return 0; 
    }
    ```
## Constants and Literals in C++
- __Literals__: The `value` assinged to each constant variables are reffered to as the literals. 

- example code: 
    ```cpp
    // identifierName: name of givent to the constant
    #define identifierName value

    // var is name of constant, 5 is literal.
    const int var = 5 
    ```
## Type of Literals in C/C++
- Integer Literals
    - Prefix: 
        - Decimal-Literal(base 10): A __non-zero decimal digit__ followed by zero or more dicmal digts.
        - Octal-literal(base 8): A __0__ followd by zero or more octal digits(045, 076, 06120).
       - Hex-literal(base 16): __0x__ or __OX__ followed by one or more hexadicimal digits(0x123, 0XFEA).
        - Binary-literal(base 2): __0b__ or __0B__ followed by one or more binary digits(Ob101, 0B11).
    - Suffix: 
        - __int__ : No suffix
        - __unsigned int__: character `u` or `U` at the end of the constant.
        - __long int__ : chracter `l` or `L` at the end of the constant.   
        - __unsigned long int__: character `ul` or `UL` at the end of the constant.
        - __long long int__: character `ll` or `LL` at the end of the constant.
        - __unsigned long long int__: character `ull` or `ULL` at the end of the constant.
 
 ## Access Modifiers in C++
There are follwing 3 types of acces modifiers in c++: 
- `public`: All the class members declared under the public specifier will be availible to every one.
    - The class member can be accessed anywhere in the program using the direct member access operator `.`.
- `private`: The class members can accessed only by the member of functions inside the class.
- `protected`:  The class members can acccessed only by the member of the functions and the subclass who inherit the class.

## Storage Classes in C++
Describe features of a variable/function. basically include scope, visibility and life-time.
- `auto`: Provides type inference capabilitie, Using `auto` might increase compiler phase, however it does not affect the run time of the program.
- `extern`: A global variable initilized with a leagal value where it is declared in order to be used elsewhere.
    - Can be accessed within any function/block. 
    - The main purpose of using extern variables is that they can be accessed between two different files, which are part of a large program.
    - A normal global variable can be changed as a extern as well by placing the keyword `extern`.
- `static`: Preserve the value of their last use in their scope. The value can only be initilized once and exsit until the termination of the program([ex03_static_var.cpp](ex03_static_var.cpp)).
- `register`: Have the same functionality as that of the `auto` variables. The only difference is that the compiler tries to store these varibles in the __register__ if a free register is available. 
    - Improves the running time of the program.
    - We can not obtain the address of a register varible using pointers.
- `mutable`:  Adding a `mutable` to a variable allows a const pointer to change members.
## Operators in C/C++
The operators supported in the C/C++.
|   Type                |   Operator                        |
|   :---:               |   :---:                           |
| Unary Operator        | `++`,`--`                         |
| Arthimetic Operator   | `+`,`-`,`*`,`/`,`%`               | 
| Relational Operator   | `<`,`<=`,`>`,`>=`, `==`, `!=`     | 
| Logical Operator      | `&&`, `||`, `!`                   | 
| Bitwide Operator      | `&`, `|`, `<<`, `>>`, `~`, `^`    | 
| Assignment Operator   | `=`, `+=`, `-=`, `*=`, `/=`, `%=` | 
| Tenary(Conditional) OP| `?:`                              |
| Other Operators       | `sizeof()` , Comma OP: `,` ([ex05_comma_op.cpp](ex05_comma_op.cpp))|

## Loops in C/C++
There are two types of loops in C++. They are __Entry Controlled Loops__ and __Exit Controlled Loops__.
- Entry Contolled Loops
    - `for` 
        ```cpp
        for (initilization expr; condition expr; update expr)
        // body of the loop.
        ``` 
    - `while` 
        ```cpp
        initilization expr;
        while (condition expr)
        {
            statements
        } 
        ```
- Exit Controlled Loops
    - `do-while` 
        ```cpp
        initilization expr;
        do
        {

        } while(condition expr);
        ```
## Decision Making in C/C++
Following keywords `if`, `else if`, `else`, `switch` are used in C/C++.
```cpp
if (condition){
    expr1
}else if(condition){
    expr2
}
    //...
else{
    expr3
}

switch(arg){
    case condition:
        expr; 
        break;
        //...
    default: 
        expr;
}
```
## Forward Declaration
__Forward Declaration__ referes to the beforehand declaration of the syntax or signature of an identifer, variable, function, class, etc. Prior to its usage to avoid compile error(done later in the program).
- example code:
    ```cpp
    // Forward declaration.
    void sum();
    
    // Definition of sum() delcared previously. 
    void sum{
        //Body
    }    
    ```
- example case: [ex06_forward_declaration.cpp](ex06_forward_declaration.cpp)

## Preprocessors in C++
Preprocessor programs provide preprocessors directives which tell the compiler to preprocessors the source code __before compiling__.
- begin with a `#` symbol(include, define, ifndef).
There are 4 types preprocessor. 
- Macros : Piece of code in a program which is given some name(`#define`).
    - No semi-colon is required after the macro definition.
    - Macros with arguments: We can also define a macro with arguments([ex07_macro_usage.cpp](ex07_macro_usage.cpp))
- File Inclusion: Using with the statement `#include`
    - When the included file are __Headerfile or Standard Files__, we use `<>`.
    - Otherwise, the included files are __User Defined Files__, we use `""`. 
- Conditional Complation: To help compiler compile some specific part of the program baased on some conditions, we can use `ifdef`, `endif` and `ifndef`.
- Other Directives.
    - `#undefine` Directive: To undefine an exsiting macro.
    - `#progma` Directive: Used to turn on or off some features.
        - `#progma startup`: Run before the control passes to `main()`. 
        - `#progma exit` : Run just before the program exit(just before the control returns from main()).
        - `#progma warn -rvl`: Hides those warning raised when a function which is supposed to return __a value does not returns a value__.
        - `#progma warn -par`:Hides those warning raised when a function __does not uses the parameters passed to it__.
        - `#progma warn -rch`: Hides those warning raised when a code is unreachable(Unreachable code writtern after then `return` statement in a function.). 
    
## Errors in C++
We may find several error types in the C++ as follows:
- __Syntax Error__ : Violatees the rules of writing C/C++ syntax known as C/C++.
- __Run-time Error__: Errors which occur during program execution(run-time) after successful complitions(Division Error).
- __Linker Error__: Link different object files with the main compiled object.
- __Logical Error__: On complition and execution of a program, desired output is not obtained when certain input values are given. 
- __Semantic Error__: The statements written in the progrram are not meaning to the compiler.

## Functions in C/C++
- Why we need functions?
    - Reducing code reduancy
    - Make code modular
    - Provide abstraction(Use library functions wihtou worring about their internal working process).

### Paramter passing to functions
- __Actual Parameter__: The arguments passed to function.
- __Formal Paramter__: The parameter received by function.
- __Pass by Value__: Value of the actual parameter are copied to the formal parameter.  They are store in different memory locations.
- __Pass by Reference__: Both actual and formal parameters refer to the same locations([ex08_params_pass_by_reference.cpp](ex08_params_pass_by_reference.cpp)).

### Main Function
Every C++ program contain a function named `main`, which is serve as the entry point of the program.
- Main function without parameters
    ```cpp
    int main(){
        //...
        return 0;
    }
    ```
- Main function with paramters
    ```cpp
    // Argument count, and arguments variable.
    int main(int arc, char * const argv[]){
        //...
        return 0;
    }
    ```

## Arrays in C/C++
Array in programming language is a collection of similar data items stored at contiguous memory locations, and randomly accessed by using indices of the array.
- Declaration of the Array
    ```cpp
    // Array delcaration by specifying its size.
    int arr[10]; 

    // Array declaration by initilizing elements.
    int arr[] = {10, 20, 30, 40}

    // Array declaration by specifiying its size and initilizing elements.
    // The rest value will be initilized as 0.
    int arr[10] = {10, 20, 30, 40}

    // Way to access Second elements the array
    // Way 1: 
    arr[1]
    // way 2: 
    1[arr] 
    ```
- Pros and Cons
    - Pros
        - Easy access to all the elemets.
    - Cons
        - Fixed number of the elements to be entered.
        - Insertion and deletion of elements can be constly.

### Container Library Array
To overcome the following fundamental problems in built-in C arrays, container `array` or `vector` are supported.
- C array dosen't know its own size.
    - Built-in Array
        ```cpp
            void function(int a[], int size){
                for (int i =0; i<s ; i++){
                    a[i] = i;
                }
            }
            //...
            // To call function we have to pass the size of the array.
            function(arr, 20);
        ``` 
    - The container `vector`.
        ```cpp
        #include <vector> 
        void function(vector<int>& v){
            for (int i=0; i< v.size(); i++){
                v[i] = i;
            }
        }
        
        // Do int type casting and making an size 20 array.
        array<int, 20> arr; 
        function(arr)
        ```
- The name of a C array converts to a pointer to its first element at the sligtest provocation. On the contrary, we may use `front()` and `back()` to access both of the first and last elements.
- We can also use some strong features which does container supports such as `memcpy()`
- Note: Unlike the built-in or container `array` by using __`vector`__ we can change the container size dynamically.
