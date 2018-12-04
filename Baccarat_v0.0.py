import random
import pandas as pd

# class Card:
#     def __init__(self, suit, rank, value):
#         self.suit = suit
#         self.rank = rank
#         self.value = value
#
# def deck_generator():
#     deck=[]
#     temp_card=Card
#     for suit in ("Clubs", "Diamonds", "Hearts", "Spades"):
#         for value in range(13):
#             temp_card.suit=suit
#             temp_card.value=value
#             if value<=10:
#                 temp_card.rank=str(value)
#             elif value==11:
#                 temp_card.rank="J"
#             elif value==12:
#                 temp_card.rank="Q"
#             elif value==13:
#                 temp_card.rank="K"
#             deck.append(temp_card)
#     return deck


# class Players:
#     def __init__(self, name, money):
#         self.name = name
#         self.money = money
#
#
# class Banker(Players):
#     def __init__(self, name, money):
#         Players.__init__(self, name, money)
#         pass
#
#
# class Player(Players):
#     def __init__(self, name, money):
#         Players.__init__(self, name, money)
#         pass


class Gambler:
    def __init__(self, name, balance, strategy, choice, chip, status, strategy_weight=(0.8, 0.1, 0.1)):
        self.name = name
        self.balance = balance
        self.strategy = strategy
        self.choice = choice
        self.chip = chip
        self.status = status
        self.strategy_weight = strategy_weight

    def description(self):
        print("Gambler name:{}, Gambler balance:{}, Gamber choice:{}, Status:{}, Strategy weight:{}."
              .format(self.name, self.balance, self.choice, self.status, self.strategy_weight))


# def create_test_gambler(gambler, name="Tester", balance=100, strategy="Random"):
#     gambler.name = name
#     gambler.balance = balance
#     gambler.strategy = strategy
#     print("Created a player named: {}, has balance: {}, with strategy: {}.".format(gambler.name, gambler.balance,
#                                                                                    gambler.strategy))


def generate_a_deck():
    """
    Generate a deck of standard game cards for baccarat which contains four suits:
    Clubs, Diamonds, Hearts, Spades from A-K without two joker cards.

    :return: A list contains a full deck of standard game cards for baccarat.
    """
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


def generate_decks(n) -> int:
    """
    Given a number of standard game decks of baccarat: n, return a list contains all cards in these n decks.

    :param n: number of decks
    :return: A list contains n decks of standard baccarat game cards.
    """
    decks = list(generate_a_deck().keys()) * n
    return decks


def rounds(n, gambler_list, min_cards=0.5, decks_num=8, results=True) -> (int, list, float, int, bool):
    """
    Given a number of rounds: n, minimum percentage of cards allowed in a baccarat game before shuffle: min_cards
    and the number of decks used in a baccarat game: decks_num, return the game results(in processing).

    :param n: number of rounds
    :param min_cards: minimum percentage of cards allowed in a baccarat game before shuffle
    :param decks_num: number of decks used in a baccarat game
    :return: a dataframe of game results (in processing)
    """
    standard_deck = generate_a_deck()
    decks = generate_decks(decks_num)
    random.shuffle(decks)
    for i in range(n):

        for gambler in gambler_list:
            gambler.choice = strategy_bet(gambler.strategy, gambler.strategy_weight)

        if len(decks) < min_cards * decks_num * 52:
            decks = generate_decks(decks_num)
            random.shuffle(decks)

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

        # print("Player's initial points:{}. Player's cards: {} {}".format(player_initial_value, card1, card2))
        # print("Banker's initial points:{}. Banker's cards: {} {}".format(banker_initial_value, card3, card4))
        if results == True:
            print("\nRound {} starts!".format(i + 1))
            print("Total cards in decks are {}".format(len(decks)))
            print("Player's total points:{}. Player's cards: {} {} {}".format(player_value, card1, card2, card5))
            print("Banker's total points:{}. Banker's cards: {} {} {}".format(banker_value, card3, card4, card6))

        if player_value > banker_value:
            for gambler in gambler_list:
                if gambler.status == "Dead":
                    continue
                elif gambler.choice == "Player":
                    gambler.balance += gambler.chip
                else:
                    gambler.balance -= gambler.chip

                if gambler.balance <= 0:
                    gambler.balance = 0
                    gambler.status = "Dead"
                    # player.money += 1
            # banker.money -= 1
            if results == True:
                print("Player won!")
        elif player_value < banker_value:
            for gambler in gambler_list:
                if gambler.status == "Dead":
                    continue
                elif gambler.choice == "Banker":
                    gambler.balance += gambler.chip * 0.95
                else:
                    gambler.balance -= gambler.chip

                if gambler.balance <= 0:
                    gambler.balance = 0
                    gambler.status = "Dead"
            # banker.money += 1
            # player.money -= 1
            if results == True:
                print("Banker won!")
        else:
            for gambler in gambler_list:
                if gambler.status == "Dead":
                    continue
                elif gambler.choice == "Tie":
                    gambler.balance += gambler.chip * 8
                else:
                    gambler.balance -= gambler.chip

                if gambler.balance <= 0:
                    gambler.balance = 0
                    gambler.status = "Dead"
            if results == True:
                print("Tie!")

        for gambler in gambler_list:
            gambler.balance = round(gambler.balance, 2)
            if results == True:
                gambler.description()
        # if player.money <= 0:
        #     print("Player game over!")
        #     break
        # print("round {}, Player money:{}, Banker money:{}.".format(n, player.money, banker.money))
        # print("At the end of round {}, Player money:{}.\n".format(i+1, player.money))
    final_balance = []
    for gambler in gambler_list:
        final_balance.append(gambler.balance)
    return final_balance


def strategy_bet(strategy_type, weight=(0.8, 0.1, 0.1)):
    if strategy_type == "Random":
        decision = random.sample(["Banker", "Player", "Tie"], 1)
    else:
        a = round(100 * weight[0])
        b = round(100 * weight[1])
        c = round(100 * weight[2])
        if strategy_type == "Player":
            choices = ["Player"] * a + ["Banker"] * b + ["Tie"] * c
        elif strategy_type == "Banker":
            choices = ["Banker"] * a + ["Player"] * b + ["Tie"] * c
        else:
            choices = ["Tie"] * a + ["Banker"] * b + ["Player"] * c
        decision = random.sample(choices, 1)
    return "".join(decision)


def games(m, n, gambler_list, min_cards=0.5, decks_num=8, results=False) -> (int, int, list, float, int, bool):
    res = []
    for i in range(m):
        print("Game: {}".format(i))
        a = Gambler(name="Tester1", balance=1000, strategy="Random", choice="Player", chip=1, status="Alive")
        b = Gambler(name="Tester2", balance=1000, strategy="Player", choice="Banker", chip=1, status="Alive")
        c = Gambler(name="Tester3", balance=1000, strategy="Banker", choice="Tie", chip=1, status="Alive")
        d = Gambler(name="Tester4", balance=1000, strategy="Tie", choice="Tie", chip=1, status="Alive")
        res.append(rounds(n, gambler_list=[a, b, c, d], min_cards=min_cards, decks_num=decks_num, results=results))
    return res


if __name__ == '__main__':
    a = Gambler(name="Tester1", balance=1000, strategy="Random", choice="Player", chip=1, status="Alive")
    b = Gambler(name="Tester2", balance=1000, strategy="Player", choice="Banker", chip=1, status="Alive")
    c = Gambler(name="Tester3", balance=1000, strategy="Banker", choice="Tie", chip=1, status="Alive")
    d = Gambler(name="Tester4", balance=1000, strategy="Tie", choice="Tie", chip=1, status="Alive")
    res = rounds(5000, gambler_list=[a, b, c, d], results=False)
    print(res)

    a = Gambler(name="Tester1", balance=1000, strategy="Random", choice="Player", chip=1, status="Alive")
    b = Gambler(name="Tester2", balance=1000, strategy="Player", choice="Banker", chip=1, status="Alive")
    c = Gambler(name="Tester3", balance=1000, strategy="Banker", choice="Tie", chip=1, status="Alive")
    d = Gambler(name="Tester4", balance=1000, strategy="Tie", choice="Tie", chip=1, status="Alive")
    final_res = games(100, 5000, gambler_list=[a, b, c, d])
    print(final_res)
    df=pd.DataFrame.from_records(final_res)
    df.to_csv("output.csv")

    # for i in range(100):
    #     print(strategy_bet("Player"))

    # shadiao = Player("Shadiao", 5)
    # dalao = Banker("Casino", 9999
