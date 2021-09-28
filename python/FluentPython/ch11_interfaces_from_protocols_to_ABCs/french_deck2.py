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

    def __delitem__(self, pos):
        del self._cards[pos]
    
    def __repr__(self):
        return str(deck[:])

    def insert(self, pos, card):
        self._cards.insert(pos, card)

        

if __name__ == '__main__':
   deck = FrenchDeck()
   print(deck[0])
   print("Delete first item")
   del deck[0]
   print(deck[0])
   print("Add first item")
   deck.insert(0, Card("diamond",'A'))
   print(deck[0])
