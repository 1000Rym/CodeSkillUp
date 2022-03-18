
# Modern Effective CPP
## Introduction
In this section, we will summarize the contents discussed in Effective Modern CPP written by Scott Meyers.

###  Terminology and Conventions
#### Version 
| Terms         | Target Version    | Description                                       |   
|:---           | :---              |:---                                               |   
| C++           | All Version       | Effectioncy                                       |
| C++98         | C++98 and C++03   | Lacks support for concurrency.                    |
| C++ 11        | C++11 and C++14   | Supports for lambda expressions, move semantics   |  
| C++ 14        | C++ 14            | Generalized function return type deduction.       |

- About Move sementics
    - Distinguishing expressions that are __rvalues__ from those that are __lvalues__(refered objects).
        - __rvalues__: Temporary objects that can have address.
        - __lvalues__: Refererd objects that generally don't have address.