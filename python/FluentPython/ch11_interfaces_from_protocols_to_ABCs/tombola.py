import abc
class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        """Add items from an iterable"""

    @abc.abstractmethod
    def pick(self):
        """Remove item at random, returning it.
        Raise `LookupError` When empty
        """

    def loaded(self):
        """Return `True` if there is at least 1 item.`Faslse` otherwise."""
        return bool(self.insepct())

    def inspect(self):
        items = []

        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        
        self.load(items)
        return tuple(sorted(items))

class Fake(Tombola):
        def pick(self):
            return 13

if __name__ == '__main__':
    f = Fake()