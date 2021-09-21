from array import array
import reprlib
import math
import functools
import operator

class Vector:
    typecode = 'd'
    shortcut_names = 'xyzt'

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
        return len(self) == len(other) and all(a == b for a,b in zip(self, other))

    def __hash__(self):
        hashes = map(hash, self._components) # equal with hashes = (hash(x) for x in self._components)
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    def __getattr__(self, short_cut_name):
        cls = type(self) 
        if len(short_cut_name) == 1:
            pos = cls.shortcut_names.find(short_cut_name)
            
            # Two oprator in one line
            if 0 <= pos <len(self._components): 
                return self._components[pos]
            
            msg = '{.__name__!r} object has no attribute {!r}'
            raise AttributeError(msg.format(cls, short_cut_name))

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ""
            if error:
                msg = error.format(cls_name = cls.__name__, attr_name = name)
                raise AttributeError(msg)
        super().__setattr__(name, value)



if __name__ == '__main__' :
    print("Test code for the vector_v3")
    v1 = Vector(range(10))
    print(v1.x)
    print((v1.y, v1.z, v1.t))
    #v1.x = 10
    v1.a = 11
 