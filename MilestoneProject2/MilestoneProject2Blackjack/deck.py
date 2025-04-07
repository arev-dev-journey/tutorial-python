'''Instantiate a deck of cards'''
import random
from card import Card, suits, ranks

class Deck:
    '''Class that defines a deck of cards'''
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))

    def shuffle(self):
        '''Randomly shuffle cards in a deck'''
        random.shuffle(self.all_cards)

    def deal_one(self):
        '''deal one card'''
        return self.all_cards.pop()
