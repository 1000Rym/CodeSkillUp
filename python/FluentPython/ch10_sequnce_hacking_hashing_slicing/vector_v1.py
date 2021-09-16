from array import array
import reprlib
import math

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
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(tyypecode)
        return cls(memv)

if __name__ == '__main__' :
    print("Test code for the vector_v1")
    v1 = Vector(range(4))
    v2 = Vector([0,1,2,3])
    print(f'repr:{repr(v1)}')
    print(f'str:{v1}')
    print(f'bytes:{bytes(v1)}')
    print(f'v1 eaqual v2 is {v1 == v2}')
    print(f'abs(v1) == {abs(v1)}')
    