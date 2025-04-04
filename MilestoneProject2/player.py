'''Instantiate a Player class'''
class Player:
    '''Create a class that defines a player with a name and modifies their cards'''

    def __init__(self,name):
        self.name = name
        # A new player has no cards
        self.all_cards = []

    def remove_one(self):
        '''remove one card'''
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        '''add one card'''
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
