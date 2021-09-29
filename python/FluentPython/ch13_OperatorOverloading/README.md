## Chapter 13: Operator Overloading: Doing it Right
In the following sections, we will cover:
- How python support infix operators with operands of different types.
- Using duck typing or explict type checks to deal with operands of various types.
- How an infix operator method should signal it cannot handle an operand
- The special behavior of the rich comparision operators
- The default handling of argumented assignement operators, like +=, and how to overload them.

### Operator Overloading Basic 
Python strikes a good balance betweeen flexibility, usablility, and safety by imposing some limitations.
- We cannot overload operators for the built-in types.
- We canannot create new operator, only overload existing ones.
- A few operators can't be overloaded such as : is, and, or, not(however &,|, ~ can be overloaded)

|Operator|Forward|Reverse|In-place|Description|
|:---:|:---:|:---:|:---:|:---:|
| + | `__add__` | `__radd__` | `__iadd__` | Addition or concatenation|
| - | `__sub__` | `__rsub__ `| `__isub__` | Subtraction |
| * | ` __mul__ `| `__rmul__ ` | `__imul__ `| Multiplication or repetition |
| / | `__truediv__` | `__rtruediv__` | `__itruediv__`| True division |
| // |` __floordiv__`| `__rfloordiv__` | `__ifloordiv__` | Floor division |
| % |` __mod__`|`__rmod__`|`__imod__`| Modulo |
| divmod() |`__divmod__`|`__rdivmod__`|`__idivmod__`| Returns tuple of floor division quotient and modulo |
| **, pow()|`__pow__`|`__rpow__`|`__ipow__`|Exponentiation|
| @ |`__matmul__`|`__rmatmul__`|`__imatmul__`|Matrix multiplication|
| & |`__and__`|`__rand__`|`__iand__`|Bitwise and|
| \| |`__or__`|`__ror__`|`__ior__`| Bitwise or |
| ^ |`__xor__`|`__rxor__`|`__ixor__`| Bitwise xor |
| << |`__lshift__`|`__rlshift__`|`__ilshift__`| Bitwise shift left |
| >> |`__rshift__`|`__rrshift__`|`__irshift__`| Bitwise shift right |

- example code: 
    - `__add__()`, `__radd__()`, `__neg__()`, `__mul__()`:  [vector.py](vector.py) 
    - `__iadd__()`: [bingoaddeble.py](bingoaddable.py)