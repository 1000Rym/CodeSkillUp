import random
class NumberPicker:
    def __init__(self, items):
        # It is suggested to add an under line in front of class variable.
        self._items = list(items)
        random.shuffle(self._items)
    
    def pick(self):
        try :
            number = self._items.pop()
            return number
        except IndexError :
            # raise a look up error.
            raise LookupError("Pick a number from the empty list.")
    
    # Implement a callable function 
    def __call__(self):
        return self.pick()

if __name__ == '__main__':
    number_picker = NumberPicker(range(10))
    print(f'Picked number by function call number_picker.pick():{number_picker.pick()}')
    print(f'Picked number by callable type number_picker(): {number_picker()}')
