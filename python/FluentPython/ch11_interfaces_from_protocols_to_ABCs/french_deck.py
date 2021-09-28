import collections
from random import shuffle

Card = collections.namedtuple('Card', ['suit','rank'])

class FrenchDeck:
    suits = 'diamond spades clubs hearts'.split()
    ranks = [str (i) for i in range(2, 11)] + list('JQKA')

    def __init__(self):
        self._cards = [Card(suit, rank) for suit in self.suits
                                        for rank in self.ranks]
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, pos):
        return self._cards[pos]
    
    def __setitem__(self, pos, card):
        self._cards[pos] = card
    
    def __repr__(self):
        return str(deck[:])

        

if __name__ == '__main__':
   deck = FrenchDeck()
   shuffle(deck)
   print(deck[:5])
