# The SOLID principles of Object-Oriented Programming.
## Single Responsibility Principle

> A class should have only one reason to change." - Robert C. Martin(Uncle Bob)

Definition: Every module, class or function in computer program should have responsibility over a single part of that program's functionality, and it shoud encapsulate that part. 

- Example Code:
    - Journal:  Move journal's save function to writer.( [journal.h](journal.h), [journal.cpp](journal.cpp))