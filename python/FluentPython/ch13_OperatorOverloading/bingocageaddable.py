import itertools

from tombola import Tombola
from bingo import BingoCage

class AddableBingoCage(BingoCage):
    
    def __add__(self, other):
        if isinstance(other, Tombola):
            return AddableBingoCage(self.inspect() + other.inspect())
        else: 
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Tombola):
            other_iterable = other.inpect()
        else:
            try: 
                other_iterable = iter(other)
            except TypeError:
                self_cls = type(self).__name__
                msg = "right openrand in += ust be{!r} or an iterable"
                raise TypeError(msg.format(self_cls))

            self.load(other_iterable)
            return self
        

if __name__== '__main__':
    print("Test Addable BingoCage")
    bingo1 = AddableBingoCage([1,2,3])
    bingo2 = AddableBingoCage([4,5,6])
    print((bingo1+bingo2).inspect())
    bingo1 += [10,11,12]
    print(bingo1.inspect())