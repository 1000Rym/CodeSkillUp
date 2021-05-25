## Special method
### Special method names
|       Category                    |    Method Names                                                                     |
|:---                               |:---                                                                                 |
|String/bytes representation        |`__repr__`, `__str__`, `__format__`, `__bytes__`                                     |
|Conversion to number               |`__abs__`, `__bool__`, `__complex__`, `__int__`, `__float__`, `__hash__`, `__index__`|
|Emulating collections              |`__len__`, `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`,              |
|Iteration                          |`__iter__`, `__reversed__`, `__next__`                                               |
|Emulating callables                |`__call__`                                                                           |
|Context management                 |`__enter__`, `__exit__`                                                              |
|Instance creation and destruction  |`__new__`, `__init__`, `__del__`                                                     |
|Attribute management               |`__getattr__`, `__getattribute__`, `__setattr__`, `__delattr__`, `__dir__`           |
|Attribute descriptors              |`__get__`, `__set__`, `__delete__`                                                   |
|Class services                     |`__prepare__`, `__instancecheck__`, `__subclasscheck__`                              |
---
### Special method names for operatiors
|       Category                           |    Method names and related operators                                       |
|:---                                      |:---                                                                         |
|Unary numeric operators                   |`__neg__` - ,`__pos__` + ,`__abs__` abs()                                    |
|Rich comparison operators                 |`__lt__` > , `__le__`<= ,`__eq__` == , `__ne__` !=, `__gt__` > , `__ge__` >= | 
|Arithmetic operators                      |`__add__` + ,`__sub__` - ,`__mul__` * , `__truediv__` / , `__floordiv__` // , `__mod__` % , `__divmod__` divmod() , `__pow__` ** or pow() , `__round__` round()|
|Reversed arithmetic operators             |`__radd__`, `__rsub__` , `__rmul__`, `__rtruediv__`, `__rfloordiv__`, `__rmod__`, `__rdivmod__`, `__rpow__`|
|Augmented assignment arithmetic operators |`__iadd__`, `__isub__`, `__imul__`, `__itruediv__`, `__ifloordiv__`, `__imod__`, `__ipow__`|
|Bitwise operators                         |`__invert__` ~ , `__lshift__` << , `__rshift__` >> , `__and__` & , `__or__` \| , `__xor__` ^|
|Reversed bitwise operators                |`__rlshift__`, `__rrshift__` , `__rand__` , `__rxor__` , `__ror__`           |
|Augmented assignment bitwise              |`__ilshift__`, `__irshift__`, `__iand__`, `__ixor__`, `__ior__`              |
---

Note: 
* Reversed operators: Instead of using `a*b`, use `b*a`.
* Augmented assignment: Express statement `a= a*b` as `a*=b`. 
* Rich comparison operators: 향상 된 비교 연산자.
* Augmented assignment arithmetic operators: 복합 할당 산술 연산자(`x+=1`)
* Augmented assignment bitwise: 복합 할당 비트 연산자.(`x&=y`, `x>>y` 오른쪽으로 y bit 이동)

