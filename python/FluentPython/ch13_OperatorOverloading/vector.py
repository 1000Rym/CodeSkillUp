from array import array
import reprlib
import math
import functools
import operator
import itertools
import numbers

class Vector:
    typecode = 'd'

    def __init__(self, components):
        '''Recive value as the iterator'''
        self._components = array(self.typecode, components)
    
    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        # Note: safe representing with reprlib.repr -> array('d', [0.0, 1.0, 2.0, 3.0, 4.0, ...])
        components = reprlib.repr(self._components) 
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))

    def __eq__(self, other):
        if isinstance(other, Vector):
            return len(self) == len(other) and all(a == b for a,b in zip(self, other))
        else:
            return NotImplemented

    def __ne__(self, other):
        """
        Rich Comparison Method: 
        The truth of x==y does not imply that x!=y is false. 
        Accordingly when defining __eq__(), one should also define __ne__(), 
        so that the operatos will behave as expected.
        """
        eq_result = self == other
        if eq_result is NotImplemented:
            return NotImplemented
        else:
            return not eq_result


    def __hash__(self):
        hashes = map(hash, self._components) # equal with hashes = (hash(x) for x in self._components)
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))
    
    def __pos__(self):
        return Vector(self)

    def __neg__(self):
        return Vector(-x for x in self)

    def __add__(self, other):
        try: 
            pairs = itertools.zip_longest(self, other, fillvalue=0)
            return Vector(a+b for a,b in pairs)
        except TypeError: 
            return NotImplemented
    
    def __radd__(self, other):
        return self + other
    
    def __sub__(self, other):
        pairs  = itertools.zip_longest(self, other, fillvalue=0)
        return Vector(x-y for x,y in pairs)

    def __mul__(self, value):
        if isinstance(value, numbers.Real):
            return Vector(x*value for x in self)
        else : 
            raise NotImplemented
    
    def __rmul__(self, other):
        return self*other

    def __bool__(self):
        return bool(abs(self))


if __name__ == '__main__' :
    v1 = Vector([1,2,3,4])
    v2 = Vector([2,3,5,6])
    print(f"Test Vector v1:{v1}, v2:{v2}.")
    print(f"+v2 is {+v2}")
    print(f"-v1 is {-v1}")
    print(f"v1+v2 is {v1+v2}")
    print(f"v1-v2 is {v1-v2}")
    print(f"v1+(1,2,3) is {v1+(1,2,3)}")
    print(f"(1,2,3)+v1 is {(1,2,3)+v1}")
    print(f"v1*10 is {v1*10}")
    print(f"10*v1 is {10*v1}")
