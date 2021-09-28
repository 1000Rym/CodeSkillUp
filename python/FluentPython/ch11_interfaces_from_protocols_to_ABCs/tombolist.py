from random import randrange

from tombola import Tombola

@Tombola.register
class TomboList(list):
    def pick(self):
        if self: 
            pos = range(len(self))
        else:
            raise LookupError('pop from empty TomboList')
    
    load = list.extend

    def loaded(self):
        return bool(self)
    
    def inspect(self):
        return tuple(sorted(self))

if __name__ == '__main__':
    t = TomboList(range(100))
    print(f"TomboList is the subclass of tombola: {issubclass(TomboList, Tombola)}")
    print(f"Instance of tombolist t is the instance of tombola: {isinstance(t, Tombola)}")
    print(f"TomboList's mro(Method Resolution Order):{TomboList.__mro__}")