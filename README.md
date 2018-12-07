# 590PR Final_Project


# Title: Monte Carlo Method for Baccarat (card game)
## Team Member(s):
Xiaoliang Jiang and Te Lin

# Monte Carlo Simulation Scenario & Purpose:
(be sure to read the instructions given in course Moodle)
## Senario:
Baccarat is a popular card game played at casinos, especially among Asian gamblers. It is a comparing card game played between two hands, the "player" and the "banker". Each baccarat coup (round of play) has three possible outcomes: "player" (player has the higher score), "banker", and "tie". In baccarat, cards have a point value: cards two through nine are worth face value (in points); tens, jacks, queens and kings have no point value (i.e. are worth zero); aces are worth 1 point; jokers are not used. Hands are valued according to the rightmost digit of the sum of their constituent cards. For example, a hand consisting of 2 and 3 is worth 5, but a hand consisting of 6 and 7 is worth 3 (i.e., the 3 being the rightmost digit in the combined points total of 13). The highest possible hand value in baccarat is therefore nine.

### Rules of Baccarat:
If neither the player nor the banker is dealt a total of 8 or 9 in the first two cards (known as a "natural"), the tableau is consulted, first for the player's rules, then the banker's.

#### Player's rule
If the player has an initial total of 0–5, he draws a third card. If the player has an initial total of 6 or 7, he stands.
#### Banker's rule
If the player stood pat (i.e., has only two cards), the banker regards only his own hand and acts according to the same rule as the player. That means the banker draws a third card with hands 0–5 and stands with 6 or 7.
If the player drew a third card, the banker acts according to the following more complex rules:
* If the banker total is 2 or less, then the banker draws a card, regardless of what the player's third card is.
* If the banker total is 3, then the banker draws a third card unless the player's third card was an 8.
* If the banker total is 4, then the banker draws a third card if the player's third card was 2, 3, 4, 5, 6, 7.
* If the banker total is 5, then the banker draws a third card if the player's third card was 4, 5, 6, or 7.
* If the banker total is 6, then the banker draws a third card if the player's third card was a 6 or 7.
* If the banker total is 7, then the banker stands.

Hands: the "player" and the "banker." 

Possible outcomes each round of play: "player" (player has the higher score), "banker" (banker has the higher score), and "tie."

Rules: After assigning the first four cards to player and banker (the order is player-banker-player-banker), If neither the player nor the banker is dealt a total of 8 or 9 in the first two cards (the single-digit of the sum of two cards on hand), the tableau of drawing rules is consulted, first for the player's rules, then the banker's. We will include this tableau later.

## Purpose:
With Monte Carlo sampling method, we want to:

1.simulate the chance for each outcome;

2.consider in casinos, the bankers usually have unlimited funds, it will be interesting to simulate that with a certain amount of funds in player's hand, how long it will take for a player to lose all funds;

3.and based on different strategies a gambler has, we want to simulate the chance of winning accordingly.
 

## Simulation's variables of uncertainty

#### Class Baccarat:

Hands: Player, Banker

CardsDraw:

Result: PlayerWins, BankerWins, Tie

#### Class Gambler:

Name: string

Strategies:7 kinds-random, all banker, all player, all tie, dragon till 13th, 3 in a row, cross.

GamblerBalance: $100, $1,000, $10,000 or more

List and describe your simulation's variables of uncertainty (where you're using pseudo-random number generation). For each such variable, how did you decide the range and probability distribution to use?  Do you think it's a good representation of reality?

## Hypothesis or hypotheses before running the simulation:
#### Analytical variables: Strategies, Goals and Bets
Suppose gamblers carry the same balances before starting games, and the casino's balance is unlimited. Gamblers would have different strategies, goals, or bets.

On our analytical stage, we want to exam the outcome with two of them as controls, and the rest one as test, and make plots accordingly.
Plots will include but not limit to:

1) the time (round) a gambler first reach its goal (earn 10%, earn 20%, etc.) (hypothesis: the gambler is rational, and he/she will leave the casino once he/she reaches his/her goal); How many gamblers (proportion) can reach a given goal (earning 10%, 20%, etc. of the original balance)

10 gamblers (10 100-round trials): goal: 20%
100, 100, 48, 56, 99, 100, 100, 64, 100, 100

In barplots:

   a. given goal: 20%, dif bet ratio (in different colors): 5%, 10%, 15%, 20%, 25%, 50%, 75%, 100%... (several plots for dif stratergy)

   b. given ratio: 5%, possibility get dif goal: P(110%), P(120%), P(130%)... (several plots for dif stratergy)

   c. given goal and ratio (the best-performed combination we observed from previous two experiments) : dif statergy: random, player, banker, tie, dragon.... (several pair of goals and ratios)

2) the time (round) it takes for a gambler to die (lose all its balance to the casino); (bar plot or 堆叠点图）


3) the balance after n rounds of game (0 <n <= 5000) (bar plot or 堆叠点图）



## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)

## Instructions on how to use the program:

## All Sources Used:
Wikipedia (2018, Dec 02). *Baccarat (card game).* Retrieved from https://en.wikipedia.org/wiki/Baccarat_(card_game)
