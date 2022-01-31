#!/usr/bin/python3
import random

SUIT = '♠ ♥ ♦ ♣'.split()
RANK = [str(num) for num in range(2,11)] + 'J Q K A'.split()

 
class Deck:
    def __init__(self):
        self.cards = [(suit, rank) for suit in SUIT 
                                    for rank in RANK]
    def __repr__(self):
        return str(["suit:{}, color:{}".format(suit, rank) for suit, rank in self.cards])

    def __getitem__(self, index):
        return self.cards[index]

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

class Player:
    def __init__(self):
        self.cards = []

    def __len__(self):
        return len(self.cards)

    def add(self, cards):
        """Add new cards"""
        self.cards.append(cards)
    
    def hands_out(self):
        """pop a card from players if len is larger than 0"""
        return self.cards.pop()
    
    def __repr__(self):
        return "{}".format(self.cards)

    

class Game:
    def __init__(self):
        """Init the game"""
        self.cards = Deck()
        self.player1 = Player()
        self.player2 = Player()
        self.remain = []

    def __set_game(self):
        self.cards.shuffle()
        count = 0
        for card in self.cards:
            if count < len(self.cards)/2 : 
                self.player1.add(card)
            else:
                self.player2.add(card)
            count+=1

    def __add_card_to_winner(self, winner):
        while self.remain:
            winner.add(self.remain.pop())

    def __compare(self, card1, card2):
        return RANK.index(card1[1]) - RANK.index(card2[1])

    
    def start(self):
        self.__set_game()
        round = 1

        while len(self.player1) and len(self.player2) :
            card1 = self.player1.hands_out()
            card2 = self.player2.hands_out()

            self.remain.append(card1)
            self.remain.append(card2)

            if self.__compare(card1, card2) > 0 :
                print(f"round {round} player1{card1} > player2{card2}:")
                self.__add_card_to_winner(self.player1)
            elif self.__compare(card1, card2) < 0:
                print(f"round {round} player1{card1} < player2{card2}:")
                self.__add_card_to_winner(self.player2)
            else:
                print(f"round {round} draw game add to remain:{str(self.remain)}")

            round +=1
        
        winner = "player1" if len(self.player2)>0 else "player2"
        print("Game finished. winner is {}".format(winner))
            

    def __repr__(self):
        result = "player1 have:" + str(self.player1) + "\nplyar2 have:" + str(self.player2)
        return result
    


if __name__ == "__main__":
    print("Welcome to the war game!")
    my_game = Game()
    my_game.start()