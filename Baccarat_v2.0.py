# -*- coding: utf-8 -*-
"""
This is a Monte Carlo simulation to simulate and analyze the results of Baccarat game which is one of the most popular
game in asian casino.
Basically, Baccarat is a comparing ard game played between two hands, the "player" and the "banker". Each baccarat coup
(round of play) has three possible outcomes: "player" (player has the higher score), "banker", and "tie". In baccarat,
cards have a point value: cards two through nine are worth face value (in points); tens, jacks, queens and kings have
no point value (i.e. are worth zero); aces are worth 1 point; jokers are not used. Hands are valued according to the
rightmost digit of the sum of their constituent cards. For example, a hand consisting of 2 and 3 is worth 5, but a hand
consisting of 6 and 7 is worth 3 (i.e., the 3 being the rightmost digit in the combined points total of 13). The highest
possible hand value in baccarat is therefore nine.
In our simulation, we set Gamblers as a class to track the attributes of the gamblers, and defined several functions to
simulate the game and analyze results of the game.
In the main function, we provided some example about how to use our python scripts to do the simulation. In general it
can return three different types of results based on a customized simulation processing.
 1. The first one focuses on the detailed information on each rounds in a game. It can return a list of lists which
    contains all gamblers balance information in each rounds. Usually, you can set show_results as True in rounds
    function to show the detailed information about the card type in each round.
 2. The second example is about comparing the differences between different strategy or chips in each round. It will run
    the simulation a*b times in total, a is the rounds in each game, and b is the number of games the function simulated
    It will return a n*m csv file, n is the number of gamblers, and m are the number of games divided by a given step.
    By using the output of this file, users could generate several plot to see the different trends of different strategy
    via Monte Carlo simulation.
 3. The last one aims to answer a question that in what possibility and how much money we expected to earn from this
    game. In this part, it will return a table with one single line which contains the probability in each earning ratio
    from 1.1, 1.2 to 7.5, 10. Users can run this example with different values to generate several lines of results and
    to check the differences.
More detailed information can be found in docstrings of each functions or you can visit our github repository as follows:
https://github.com/rita316/Final-Project/blob/master/README.md
"""

import random
import pandas as pd
import pickle
import numpy as np


class Gambler:
    def __init__(self, name, balance, strategy, choice, chip, status, strategy_weight=(1, 0, 0)):
        """
        This class is about the gambler who is the real player in this game. As you may notice that player and banker are
        the two sides of this game, so we use gambler to represent the participants of this game.
        For the Gambler class, it has several instance variables to describe the status of the gambler.
        :param name: a string represent the gambler's name
        :param balance: a float (round 2) represent how much money the gambler has
        :param strategy: a string represent the gambler's strategy with limited keywords: Random, Player, Banker, Tie.
        :param choice: a string shows the gambler's choice in this round.
        :param chip: an int shows how much money the gambler bet on this round.
        :param status: an string shows the gambler's status with limited keywords: Alive or Dead
        :param strategy_weight: an list shows the proportion of each choice which does not work when strategy is Random.

        >>> a = Gambler(name="Tester1", balance=1000, strategy="Random", choice="Player", chip=500, status="Alive")
        >>> a.balance
        1000
        >>> a.name
        'Tester1'
        """
        self.name = name
        self.balance = balance
        self.strategy = strategy
        self.choice = choice
        self.chip = chip
        self.status = status
        self.strategy_weight = strategy_weight

    def description(self):
        """
        This function will return current status of the gambler. It was designed to test the function and turned off in
        default settings.
        :return: nothing. But will print gambler's status.

        >>> b = Gambler(name="Tester2", balance=1000, strategy="Player", choice="Banker", chip=1, status="Alive")
        >>> b.description()
        Gambler name:Tester2, Gambler balance:1000, Gamber choice:Banker, Status:Alive, Strategy weight:(1, 0, 0).
        """
        print("Gambler name:{}, Gambler balance:{}, Gamber choice:{}, Status:{}, Strategy weight:{}."
              .format(self.name, self.balance, self.choice, self.status, self.strategy_weight))


def generate_a_deck():
    """
    Generate a deck of standard game cards for baccarat which contains four suits:
    Clubs, Diamonds, Hearts, Spades from A-K without two joker cards.
    :return: A list contains a full deck of standard game cards for baccarat.

    >>> generate_a_deck()
    {'Clubs_1': 1, 'Clubs_2': 2, 'Clubs_3': 3, 'Clubs_4': 4, 'Clubs_5': 5, 'Clubs_6': 6, 'Clubs_7': 7, 'Clubs_8': 8, 'Clubs_9': 9, 'Clubs_10': 10, 'Clubs_J': 10, 'Clubs_Q': 10, 'Clubs_K': 10, 'Diamonds_1': 1, 'Diamonds_2': 2, 'Diamonds_3': 3, 'Diamonds_4': 4, 'Diamonds_5': 5, 'Diamonds_6': 6, 'Diamonds_7': 7, 'Diamonds_8': 8, 'Diamonds_9': 9, 'Diamonds_10': 10, 'Diamonds_J': 10, 'Diamonds_Q': 10, 'Diamonds_K': 10, 'Hearts_1': 1, 'Hearts_2': 2, 'Hearts_3': 3, 'Hearts_4': 4, 'Hearts_5': 5, 'Hearts_6': 6, 'Hearts_7': 7, 'Hearts_8': 8, 'Hearts_9': 9, 'Hearts_10': 10, 'Hearts_J': 10, 'Hearts_Q': 10, 'Hearts_K': 10, 'Spades_1': 1, 'Spades_2': 2, 'Spades_3': 3, 'Spades_4': 4, 'Spades_5': 5, 'Spades_6': 6, 'Spades_7': 7, 'Spades_8': 8, 'Spades_9': 9, 'Spades_10': 10, 'Spades_J': 10, 'Spades_Q': 10, 'Spades_K': 10}
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
    >>> generate_decks(2)
    ['Clubs_1', 'Clubs_2', 'Clubs_3', 'Clubs_4', 'Clubs_5', 'Clubs_6', 'Clubs_7', 'Clubs_8', 'Clubs_9', 'Clubs_10', 'Clubs_J', 'Clubs_Q', 'Clubs_K', 'Diamonds_1', 'Diamonds_2', 'Diamonds_3', 'Diamonds_4', 'Diamonds_5', 'Diamonds_6', 'Diamonds_7', 'Diamonds_8', 'Diamonds_9', 'Diamonds_10', 'Diamonds_J', 'Diamonds_Q', 'Diamonds_K', 'Hearts_1', 'Hearts_2', 'Hearts_3', 'Hearts_4', 'Hearts_5', 'Hearts_6', 'Hearts_7', 'Hearts_8', 'Hearts_9', 'Hearts_10', 'Hearts_J', 'Hearts_Q', 'Hearts_K', 'Spades_1', 'Spades_2', 'Spades_3', 'Spades_4', 'Spades_5', 'Spades_6', 'Spades_7', 'Spades_8', 'Spades_9', 'Spades_10', 'Spades_J', 'Spades_Q', 'Spades_K', 'Clubs_1', 'Clubs_2', 'Clubs_3', 'Clubs_4', 'Clubs_5', 'Clubs_6', 'Clubs_7', 'Clubs_8', 'Clubs_9', 'Clubs_10', 'Clubs_J', 'Clubs_Q', 'Clubs_K', 'Diamonds_1', 'Diamonds_2', 'Diamonds_3', 'Diamonds_4', 'Diamonds_5', 'Diamonds_6', 'Diamonds_7', 'Diamonds_8', 'Diamonds_9', 'Diamonds_10', 'Diamonds_J', 'Diamonds_Q', 'Diamonds_K', 'Hearts_1', 'Hearts_2', 'Hearts_3', 'Hearts_4', 'Hearts_5', 'Hearts_6', 'Hearts_7', 'Hearts_8', 'Hearts_9', 'Hearts_10', 'Hearts_J', 'Hearts_Q', 'Hearts_K', 'Spades_1', 'Spades_2', 'Spades_3', 'Spades_4', 'Spades_5', 'Spades_6', 'Spades_7', 'Spades_8', 'Spades_9', 'Spades_10', 'Spades_J', 'Spades_Q', 'Spades_K']
    """
    decks = list(generate_a_deck().keys()) * n
    return decks


def rounds(n, gambler_list, min_cards=0.5, decks_num=8, show_result=True, scale=10, output='Default', special=0) -> (
        int, list, float, int, bool, int, str):
    """
    Given a number of rounds: n, minimum percentage of cards allowed in a baccarat game before shuffle: min_cards
    and the number of decks used in a baccarat game: decks_num, return the game results.
    As you may notice that several other parameters are designed for changing the setting. show_result aims to control
    whether print the detailed information about the game with True as default value. scale represent how many rounds
    we recorded a data with default value 10. output is a setting for the type of output with limited keyword: Default
    or possibility with default value 'Default'.
    In addition, special was added in the latest version. After received the feedback from class, we would like to design
    several special rules for this game to encourage more people playing this game. We have designed two new rules for
    this game, both of them are base on appearing two same card or three same card.
        1. First attempt is trying to add additional bonus if the winner side contains two or three identical card.
        2. The second one is trying to bonus all gambler who participated the game no matter which side win the game if
        two identical card or three identical card appeared on Banker or Player.
    Since this function contains several random generating processing, it is difficult to add a doctest on this function.

    :param n: number of rounds
    :param min_cards: minimum percentage of cards allowed in a baccarat game before shuffle
    :param decks_num: number of decks used in a baccarat game
    :param gambler_list: a list of gamblers
    :param show_result: a bool value for printing detailed information or not.
    :param scale: a int value for setting the period between each recording after a given rounds
    :param output: a string with limited keywords to control different types of output
    :param special: a int to control two special game rules.
    :return: a list of recorded data as result

    >>> a = Gambler(name="Tester1", balance=1000, strategy="Random", choice="Player", chip=1, status="Alive")
    >>> b = Gambler(name="Tester2", balance=1000, strategy="Player", choice="Banker", chip=1, status="Alive")
    >>> c = Gambler(name="Tester3", balance=1000, strategy="Banker", choice="Tie", chip=1, status="Alive")
    >>> d = Gambler(name="Tester4", balance=1000, strategy="Tie", choice="Tie", chip=1, status="Alive")
    >>> res = rounds(5000, gambler_list=[a, b, c, d], show_result=False)
    >>> print(len(res))
    501
    """
    final_balance = []
    if output == 'possibility':
        initial_balance = gambler_list[0].balance
        percentage_list = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 7.5, 10]
        round_balance = [-1] * len(percentage_list)
    standard_deck = generate_a_deck()
    decks = generate_decks(decks_num)
    random.shuffle(decks)
    k = 0
    if output == 'Default':
        for gambler in gambler_list:
            final_balance += [gambler.balance]
    for i in range(n):

        for gambler in gambler_list:
            gambler.choice = strategy_bet(gambler.strategy, gambler.strategy_weight)

        if int(len(decks)) < min_cards * decks_num * 52:
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

        if show_result:
            print("\nRound {} starts!".format(i + 1))
            print("Total cards in decks are {}".format(len(decks)))
            print("Player's total points:{}. Player's cards: {} {} {}".format(player_value, card1, card2, card5))
            print("Banker's total points:{}. Banker's cards: {} {} {}".format(banker_value, card3, card4, card6))

        for gambler in gambler_list:
            if gambler.status == "Dead":
                continue
            elif special <= -1 and (card1 == card2 or card1 == card5 or card2 == card5):
                gambler.balance += gambler.chip * 2
                if special <= -2 and (card1 == card2 and card2 == card5):
                    gambler.balance += gambler.chip * 100
                    print("Round: {}".format(i + 1))
                    print(
                        "Player's total points:{}. Player's cards: {} {} {}".format(player_value, card1, card2,
                                                                                    card5))
                    print(
                        "Banker's total points:{}. Banker's cards: {} {} {}".format(banker_value, card3, card4,
                                                                                    card6))

        if player_value > banker_value:
            for gambler in gambler_list:
                if gambler.status == "Dead":
                    continue
                elif gambler.choice == "Player":
                    gambler.balance += gambler.chip
                    if special >= 1 and (card1 == card2 or card1 == card5 or card2 == card5):
                        gambler.balance += gambler.chip * 6
                        if special >= 2 and (card1 == card2 and card2 == card5):
                            gambler.balance += gambler.chip * 36
                            print("Round: {}".format(i + 1))
                            print(
                                "Player's total points:{}. Player's cards: {} {} {}".format(player_value, card1, card2,
                                                                                            card5))
                            print(
                                "Banker's total points:{}. Banker's cards: {} {} {}".format(banker_value, card3, card4,
                                                                                            card6))
                else:
                    gambler.balance -= gambler.chip

                if gambler.balance <= 0:
                    gambler.balance = 0
                    gambler.status = "Dead"
            if show_result:
                print("Player won!")
        elif player_value < banker_value:
            for gambler in gambler_list:
                if gambler.status == "Dead":
                    continue
                elif gambler.choice == "Banker":
                    gambler.balance += gambler.chip * 0.95
                    if special >= 1 and (card3 == card4 or card3 == card6 or card4 == card6):
                        gambler.balance += gambler.chip * 6
                        if special >= 2 and (card3 == card4 and card4 == card6):
                            gambler.balance += gambler.chip * 36
                            print("Round: {}".format(i + 1))
                            print(
                                "Player's total points:{}. Player's cards: {} {} {}".format(player_value, card1, card2,
                                                                                            card5))
                            print(
                                "Banker's total points:{}. Banker's cards: {} {} {}".format(banker_value, card3, card4,
                                                                                            card6))

                else:
                    gambler.balance -= gambler.chip

                if gambler.balance <= 0:
                    gambler.balance = 0
                    gambler.status = "Dead"
            if show_result:
                print("Banker won!")
        else:
            for gambler in gambler_list:
                if gambler.status == "Dead":
                    continue
                elif gambler.choice == "Tie":
                    gambler.balance += gambler.chip * 8
                    if special >= 1 and (card3 == card4 or card3 == card6 or card4 == card6):
                        gambler.balance += gambler.chip * 25
                        if special >= 2 and (card3 == card4 and card4 == card6):
                            gambler.balance += gambler.chip * 125
                            print("Round: {}".format(i + 1))
                            print(
                                "Player's total points:{}. Player's cards: {} {} {}".format(player_value, card1, card2,
                                                                                            card5))
                            print(
                                "Banker's total points:{}. Banker's cards: {} {} {}".format(banker_value, card3, card4,
                                                                                            card6))
                else:
                    gambler.balance -= gambler.chip

                if gambler.balance <= 0:
                    gambler.balance = 0
                    gambler.status = "Dead"
            if show_result:
                print("Tie!")

        for gambler in gambler_list:
            gambler.balance = round(gambler.balance, 2)
            if show_result:
                gambler.description()
        if i != 0 and i % scale == 0 and output == 'Default':
            for gambler in gambler_list:
                final_balance += [gambler.balance]
        elif output == "possibility":
            if len(percentage_list) == k:
                break
            else:
                for j in range(k, len(percentage_list)):
                    if gambler_list[0].balance >= round(percentage_list[j] * initial_balance):
                        round_balance[j] = i
                        k += 1

                    else:
                        break

        elif output != "possibility" and output != "Default":
            print(
                "Please use Default output setting, or input only one Gambler to check to the possibility of earning money.")
            break

    if output == 'Default':
        for gambler in gambler_list:
            final_balance.append(gambler.balance)
        final_balance = chunkIt(final_balance, round(n / scale) + 1)
        return final_balance
    elif output == "possibility":
        return round_balance


def chunkIt(seq, num):
    """
    A function belongs to rounds function which can generate lists of list by a given step

    :param seq: a list of list contains integer which represent the results of each rounds
    :param num: an int represent the steps
    :return: a list of lists represent the results
    """
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out


def strategy_bet(strategy_type, weight=(0.8, 0.1, 0.1)):
    """
    Given a strategy type, return a decision from Banker, Player or Tie based on a given weight.

    :param strategy_type: a string with limited keywords form Random Banker, Player or Tie.
    :param weight: a tuple contains different weight for each choice.
    :return: a string with limited keywords from Banker, Player or Tie

    >>> strategy_bet("Player",weight=(1, 0, 0))
    'Player'
    """
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


def games(m, n, gambler_list_all, min_cards_all=0.5, decks_num_all=8, m_results=False, m_scale=10,
          m_output='Default', m_special=0) -> (
        int, int, list, float, int, bool, int, str, int):
    """
    Given same inputs as rounds return a list of results.

    :param m: An int represent number of games in this simulation
    :param n: An int represent number of rounds in each game
    :param gambler_list_all: a list of gamblers
    :param min_cards_all: minimum percentage of cards allowed in a baccarat game before shuffle
    :param decks_num_all: number of decks used in a baccarat game
    :param m_results: a bool value for printing detailed information or not.
    :param m_scale: a int value for setting the period between each recording after a given rounds
    :param m_output: a string with limited keywords to control different types of output
    :param m_special: a int to control two special game rules.
    :return: a list of recorded data as result
    :return: a list of result

    """
    res = []
    with open('gambler_setting.pkl', 'wb') as output:
        for i in gambler_list_all:
            pickle.dump(i, output, -1)
    for i in range(m):
        gambler_list_in_game = []
        print("Game: {}".format(i))
        for gambler in pickled_items('gambler_setting.pkl'):
            gambler_list_in_game.append(gambler)
        res.append(rounds(n, gambler_list=gambler_list_in_game, min_cards=min_cards_all, decks_num=decks_num_all,
                          show_result=m_results, scale=m_scale, output=m_output, special=m_special))
    return res


def pickled_items(filename):
    """
    Unpickle a file of pickled data.
    :param filename: a string represent a filename
    :return: none
    """
    with open(filename, "rb") as f:
        while True:
            try:
                yield pickle.load(f)
            except EOFError:
                break


def print_avg(a, n) -> (np.ndarray, int):
    """
    given a ndarray and an int return the average value for each list in same position.
    :param a: an ndarray in 3-dimensions
    :param n: the number of element in each list in this ndarray
    :return: a list contains
    >>> matrix=np.array([[[1,1,1],[2,2,2],[3,3,3]],[[2,2,2],[3,3,3],[4,4,4]],[[3,3,3],[4,4,4],[5,5,5]]])
    >>> a=print_avg(matrix, 3)
    [2. 3. 4.]
    [2. 3. 4.]
    [2. 3. 4.]

    """
    res = []
    for i in range(n):
        temp_res = sum(a[:, :, i]) / len(a)
        print(temp_res)
        res.append(temp_res)
    return res


def print_possibility(b) -> (np.ndarray):
    """
    Given a ndarray get the possibility in a given situation. This function aims to find out a number that the gambler
    could get a target earning ratio.
    :param b: A ndarray contains all of the information about number of rounds when gambler get a given earning ratio
    :return: A list contains proportions
    """
    res = []
    for i in range(18):
        a = 0
        for j in b[:, i]:
            if j != -1:
                a += 1
        res.append("{0:.2f}%".format(a * 100 / len(b[:, i])))
    return res


if __name__ == '__main__':
    """
    Example 1

    The first one focuses on the detailed information on each rounds in a game. It can return a list of lists which
    contains all gamblers balance information in each rounds. Usually, you can set show_results as True in rounds
    function to show the detailed information about the card type in each round.

    """
    a = Gambler(name="Tester1", balance=1000, strategy="Random", choice="Player", chip=1, status="Alive")
    b = Gambler(name="Tester2", balance=1000, strategy="Player", choice="Banker", chip=1, status="Alive")
    c = Gambler(name="Tester3", balance=1000, strategy="Banker", choice="Tie", chip=1, status="Alive")
    d = Gambler(name="Tester4", balance=1000, strategy="Tie", choice="Tie", chip=1, status="Alive")
    res = rounds(5000, gambler_list=[a, b, c, d], show_result=False)
    print(res)

    """
    Example 2

    The second example is about comparing the differences between different strategy or chips in each round. It will run
    the simulation a*b times in total, a is the rounds in each game, and b is the number of games the function simulated
    It will return a n*m csv file, n is the number of gamblers, and m are the number of games divided by a given step.
    By using the output of this file, users could generate several plot to see the different trends of different strategy
    via Monte Carlo simulation.

    """
    a = Gambler(name="Tester1", balance=1000, strategy="Random", choice="Player", chip=500, status="Alive")
    b = Gambler(name="Tester2", balance=1000, strategy="Player", choice="Banker", chip=500, status="Alive")
    c = Gambler(name="Tester3", balance=1000, strategy="Banker", choice="Tie", chip=500, status="Alive")
    d = Gambler(name="Tester4", balance=1000, strategy="Tie", choice="Tie", chip=500, status="Alive")
    final_res = games(1000, 1000, gambler_list_all=[a, b, c, d])
    print(final_res)

    a = np.array(final_res)
    final_data = print_avg(a, 4)
    df = pd.DataFrame.from_records(final_data)
    df.to_csv("sp-2_1000Games_1000roundsPerGames_Balance1000_chip500_by10.csv")

    """
    Example 3

    The last one aims to answer a question that in what possibility and how much money we expected to earn from this
    game. In this part, it will return a table with one single line which contains the probability in each earning ratio
    from 1.1, 1.2 to 7.5, 10. Users can run this example with different values to generate several lines of results and
    to check the differences.

    """
    e = Gambler(name="Tester4", balance=1000, strategy="Tie", choice="Tie", chip=100, status="Alive")
    final_res = games(1000, 100, gambler_list_all=[e], m_output="possibility", m_results=False)
    print(final_res)
    b = np.array(final_res)

    pr = print_possibility(b)
    print(pr)
    with open("pTie_10000Games_1000rounds_chip500.csv", 'w') as f:
        f.write("1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 7.5, 10\n")
        f.write(str(pr).replace("\'", "")[1:-1])

    df = pd.DataFrame.from_records(pr)
