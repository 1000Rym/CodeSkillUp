# Chapter9 A Pythonic Object
## Abstract 
Knowledge to learn : 
- Buit-in function(More Advanced)
- ClassMethod
- format()
- read-only access to attributes
- saving space with the `__slots__`
- overidding class attributes
 

## Built-in function
- repr(): Representing string object for the __developer__.
- str(): Representing string object for the __user__.
    - example code: [vector2d.py](vector2d.py)

## classmethod Versus staticMethod
- Static method decorator is not widly used. 
- On the contrary, `classmethod` is widly used, since we can access the class variable with `cls` parameter.
```python
#... Code under the class 
var = 10 
@classmethod
def class_method(cls, param):
    return recls.var + param
#...
```
- Exmample: [Classmethod Versus Static Method](class_vs_static_method.py)

## format
Built-in function `format()` or `str.format()`
- Type 1: format(obj, format_spec)
    ```python
    value = 1/2.43
    format(value, '.4f')
    ```
- Type 2: `{}` expression with format.
    ```python
    '2/3 = {value:.5f}'.format(value=2/3)
    ```
## Read-Only Access to attributes
- There is __no way to create__ `private` modifier in Python.
- However we can simply add two underline to say the attribute is protected or private `__` type. 
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def repr(self):
        return f"This person's name is {self.name}, {self.__age} years old."

if __name__ == '__main__':
    david = Person("David", 18)
    print(david.name) # Could access the name directly.
    #print(david.__age)
    print(david._Person__age) # Age Could not be used directly
```

## Saving Sapce with the __slots__
By definding `__slots__` in the class telling the interprter that those are all attributes used in this class. And then python will stores attributes in a tuple-like structure. This will avoid creat per-instance `__dict__`. 

```python
class Person:
    __slots__ = (__name, __age)
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def repr(self):
        return f"This person's name is {self.name}, {self.__age} years old."

>>> david = Person("David", 18)
>>> david.__dict__

# When use slots __dict__ is not created.
... AttributeError: 'Person' object has no attribute '__dict__'
```
### The problems with __slots__
- Inherited attribute is ignored by the interpreter.
- Instance will only be handled in `__slots__`
- Cannot be targets of weak references.




