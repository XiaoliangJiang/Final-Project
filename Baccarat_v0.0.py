import random


class Card:
    def __init__(self, suits, ranks):
        self.suits = suits
        self.ranks = ranks


class Players:
    def __init__(self, name, money):
        self.name = name
        self.money = money


class Banker(Players):
    def __init__(self, name, money):
        Players.__init__(self, name, money)
        pass


class Player(Players):
    def __init__(self, name, money):
        Players.__init__(self, name, money)
        pass


def generate_a_deck():
    deck = {}
    for suit in ("Clubs", "Diamonds", "Hearts", "Spades"):
        for rank in range(1, 14):
            if rank <= 10:
                card_name = suit + "_" + str(rank)
                deck[card_name] = rank
            elif rank == 11:
                card_name = suit + '_J'
                deck[card_name] = 10
            elif rank == 12:
                card_name = suit + '_Q'
                deck[card_name] = 10
            elif rank == 13:
                card_name = suit + '_K'
                deck[card_name] = 10
    return deck


def generate_decks(n):
    decks = list(generate_a_deck().keys()) * n
    return decks


def rounds(n, min_cards=0.5, decks_num=8):
    decks = generate_decks(decks_num)
    random.shuffle(decks)
    for i in range(n):
        print("\nRound {} starts!".format(i + 1))
        if len(decks) < min_cards * decks_num * 52:
            decks = generate_decks(decks_num)
            random.shuffle(decks)
        print("Total cards in decks are {}".format(len(decks)))
        card1 = decks.pop()
        card2 = decks.pop()
        card3 = decks.pop()
        card4 = decks.pop()
        card5 = ""
        card6 = ""
        player_initial_value = (standard_deck[card1] + standard_deck[card2]) % 10
        banker_initial_value = (standard_deck[card3] + standard_deck[card4]) % 10
        if player_initial_value > 7 or banker_initial_value > 7:
            player_value = player_initial_value
            banker_value = banker_initial_value
        elif player_initial_value < 6:
            card5 = decks.pop()
            player_value = (player_initial_value + standard_deck[card5]) % 10
            if banker_initial_value <= 2:
                card6 = decks.pop()
                banker_value = (banker_initial_value + standard_deck[card6]) % 10
            elif banker_initial_value == 3 and standard_deck[card5] != 8:
                card6 = decks.pop()
                banker_value = (banker_initial_value + standard_deck[card6]) % 10
            elif banker_initial_value == 4 and standard_deck[card5] in (2, 3, 4, 5, 6, 7):
                card6 = decks.pop()
                banker_value = (banker_initial_value + standard_deck[card6]) % 10
            elif banker_initial_value == 5 and standard_deck[card5] in (4, 5, 6, 7):
                card6 = decks.pop()
                banker_value = (banker_initial_value + standard_deck[card6]) % 10
            elif banker_initial_value == 6 and standard_deck[card5] in (6, 7):
                card6 = decks.pop()
                banker_value = (banker_initial_value + standard_deck[card6]) % 10
            else:
                banker_value = banker_initial_value
        else:
            player_value = player_initial_value
            if banker_initial_value < 6:
                card6 = decks.pop()
                banker_value = (banker_initial_value + standard_deck[card6]) % 10
            else:
                banker_value = banker_initial_value

        print("Player's initial points:{}. Player's cards: {} {}".format(player_initial_value, card1, card2))
        print("Banker's initial points:{}. Banker's cards: {} {}".format(banker_initial_value, card3, card4))

        print("Player's total points:{}. Player's cards: {} {} {}".format(player_value, card1, card2, card5))
        print("Banker's total points:{}. Banker's cards: {} {} {}".format(banker_value, card3, card4, card6))

        if player_value > banker_value:
            # player.money += 1
            # banker.money -= 1
            print("Player won!")
        elif player_value < banker_value:
            # banker.money += 1
            # player.money -= 1
            print("Banker won!")
        else:
            print("Tie!")

        # if player.money <= 0:
        #     print("Player game over!")
        #     break
        # print("round {}, Player money:{}, Banker money:{}.".format(n, player.money, banker.money))
        # print("At the end of round {}, Player money:{}.\n".format(i+1, player.money))

if __name__ == '__main__':
    standard_deck = generate_a_deck()

    # shadiao = Player("Shadiao", 5)
    # dalao = Banker("Casino", 9999)
    rounds(100)

