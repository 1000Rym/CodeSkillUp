import random

from tombola import Tombola

class LotteryBlower(Tombola):
    def __init__(self, iterable):
        self._balls = list(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try: 
            pos = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('Pick from empty BingoCage')
        return self._balls.pop(pos)
    
    def loaded(self):
        return bool(self._balls)
    
    def inspect(self):
        return tuple(sorted(self._balls))

if __name__ == '__main__':
    lottery = LotteryBlower([7,3,2,4])
    print(lottery.inspect())
    lottery.pick()
    print(lottery.inspect())
    print(lottery.loaded())
