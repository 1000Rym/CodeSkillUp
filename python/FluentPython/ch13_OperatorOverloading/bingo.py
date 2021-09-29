import random

from tombola import Tombola

class BingoCage(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()

    
if __name__ == '__main__':
    bingo = BingoCage(range(1,46))
    for i in range(50): print(f"Picked up new number:{bingo()}")