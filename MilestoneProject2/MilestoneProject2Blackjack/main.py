from deck import Deck
from hand import Hand
from card import Card

test_deck = Deck()
test_deck.shuffle()
test_player = Hand()
pulled_card = test_deck.deal()
print(pulled_card)
print(test_player.value)
