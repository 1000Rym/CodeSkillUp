#Introduction: Dunder(Double under) Method.
# __len__, __getitem__

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value*len(FrenchDeck.suit_values)+FrenchDeck.suit_values[card.suit]

class FrenchDeck:
    # Add 2 list. 
    # First list: Set n's type as string(The n is from 2 to 10) 
    # Second list: Add sliced'JQKA'.
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split( )
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in FrenchDeck.suits
                                        for rank in FrenchDeck.ranks]
    
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
    
    def spades_high(self, card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value*len(FrenchDeck.suit_values)+FrenchDeck.suit_values[card.suit]

deck = FrenchDeck()

print ('Lenght of deck is ' + str(len(deck)))
print (('First deck is the ' + str(deck[0])+', ' 
'Last deck is the '+str(deck[-1])))
print ('First 3 cards are' + str(deck[:3]))
print ('The cards from 12~15 are '+str(deck[12::15]))
print ('Reverse printing: ')
for card in reversed(deck):
    print (card)

for card in sorted(deck, key=spades_high):
    print (card)