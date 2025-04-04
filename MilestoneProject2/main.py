'''Instantiate main program to play a game of war between two computer opponents'''
from deck import Deck
from player import Player

player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

print(len(new_deck.all_cards))
print(len(player_one.all_cards))
print(len(player_two.all_cards))

GAME_ON = True

ROUND_NUM = 0
while GAME_ON:

    ROUND_NUM += 1
    print(f"Round {ROUND_NUM}")

    if len(player_one.all_cards) == 0:
        print("Player One out of cards! Game Over")
        print("Player Two Wins!")
        GAME_ON = False
        break
    if len(player_two.all_cards) == 0:
        print("Player Two out of cards! Game Over")
        print("Player Two Wins!")
        GAME_ON = False
        break

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    AT_WAR = True

    while AT_WAR:

        if player_one_cards[-1].value > player_two_cards[-1].value:

            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            AT_WAR = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:

            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            AT_WAR = False

        else:
            print('WAR!')
            if len(player_one.all_cards) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                GAME_ON = False
                break
            if len(player_two.all_cards) < 5:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player Two Loses!")
                GAME_ON = False
                break
            for num in range(5):
                player_one_cards.append(player_one.remove_one())
                player_two_cards.append(player_two.remove_one())
