#Introduction: Dunder(Double under) Method.
# __len__, __getitem__

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    # Add 2 list. 
    # First list: Set n's type as string(The n is from 2 to 10) 
    # Second list: Add sliced'JQKA'.
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split( )

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in FrenchDeck.suits
                                        for rank in FrenchDeck.ranks]
    
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()

print 'Lenght of deck is ' + str(len(deck))
print ('First deck is the ' + str(deck[0])+', ' 
'Last deck is the '+str(deck[1]))