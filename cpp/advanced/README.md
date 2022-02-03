# Advanced C++
In this page, we are going to add some advanced C++ skills. 
- Obejct Oriented Programming in C++
- Generic Programming
- Generic Algorithm
- Associative Containers
- Non-STL Datastructures
- STL Datastructures
- Exception Handling

## Obejct Oriented Programming in C++
The main aim of OOP is to bind together the data and the functions that operate on them so that no other part of the code can access this data except that function.

- __Class__: Conceptually, we can say it is a blueprint representing a group of objects which shares some common behavior; technically, we may define it as the user-defined data type that holds its member data and functions.
- __Object__: An instance of a class has some characteristics and behavior of a class.

### Features in OOP
- __Encapsulation__: Binidng together the data and the functions that manipulate them. This also leads to data abstraction or hiding([about_encapsulation.cpp](about_encapsulation.cpp)).
- __Abstraction__: Displaying only essential information to the outside world and hiding background details and implemetation([about_abstraction.cpp](about_abstraction.cpp)). 
    - Abstraction using Classes. 
    - Abstraction using Header Files.  
- __Polymorphism__: Operation my exhibit different behaviours in different instances.The behaviour depends upon the types of data used in the operation.
    - How to overload: 
        - __Oprator Overloading__: The process of making an operator to exhibit different behaviours in different instances.
        - __Function Overloading__: Using a single function to perform different types of tasks.
    - Example: Employees and Manager
        - UML : ![polymorphism_case1](polymorphism/emp_manager.png) 
        - Example Code: [gross_employee.cpp](polymorphism/about_polymorphism.cpp)


- __Inheritance__: The capability of a class to derive properties and characteristics. 
    - __Sub Class(Derived Class)__: The class that inherits properties from another class.
    - __Super Class(Base Class)__: The class whose properties are inherited by sub class.
    - In C++, One sub classes might inheritaed from multiple superclasses.
    - Example: Manager who like sports.
        - UML: ![inheritance](inheritance/inheritance.png)
        - Example Code: [about_inheritance.cpp](inheritance/about_inheritance.cpp)
    
