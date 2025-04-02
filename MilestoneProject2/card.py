# CARD
# SUIT,RANK,VALUE
import random
suits = ("Hearts","Diamonds","Spades","Clubs")
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,
          'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

print(suits[0])

print(ranks[0])

two_hearts = Card(suits[0],ranks[0])
ace_spades = Card(suits[2],ranks[12])
print(two_hearts)
print(ace_spades)
print(two_hearts.rank)
print(ace_spades.rank)
print(two_hearts.value)
print(ace_spades.value)
print(values[two_hearts.rank])
print(values[ace_spades.rank])
