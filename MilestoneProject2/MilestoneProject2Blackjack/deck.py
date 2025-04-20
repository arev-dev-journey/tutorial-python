import random
'''Instantiate a deck of cards'''
from card import Card, suits, ranks

class Deck:
    '''Class that defines a deck of cards'''
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has:' + deck_comp
    
    def shuffle(self):
        '''Randomly shuffle cards in a deck'''
        random.shuffle(self.deck)

    def deal(self):
        '''deal one card'''
        single_card = self.deck.pop()
        return single_card
