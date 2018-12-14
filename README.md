# 590PR Final Project
# Title: Monte Carlo Method for Baccarat (card game)
## Team Member(s):
Xiaoliang Jiang and Te Lin

# Monte Carlo Simulation Scenario & Purpose:
## Senario:
Baccarat is a popular card game played at casinos, especially among Asian gamblers. It is a card game played between two hands, the "player" and the "banker". Each baccarat coup (round of play) has three possible outcomes: "player" (player has the higher score), "banker", and "tie". In baccarat, cards have a point value: cards two through nine are worth face value (in points); tens, jacks, queens and kings have no point value (i.e. are worth zero); aces are worth 1 point; jokers are not used. Hands are valued according to the rightmost digit of the sum of their constituent cards. For example, a hand consisting of 2 and 3 is worth 5, but a hand consisting of 6 and 7 is worth 3 (i.e., the 3 being the rightmost digit in the combined points total of 13). The highest possible hand value in baccarat is therefore nine.

### Rules of Baccarat:
If neither the player nor the banker is dealt a total of 8 or 9 in the first two cards (known as a "natural"), the tableau is consulted, first for the player's rules, then the banker's.

#### Player's rules
If the player has an initial total of 0–5, he draws a third card. If the player has an initial total of 6 or 7, he stands.
#### Banker's rules
If the player stood pat (i.e., has only two cards), the banker regards only his own hand and acts according to the same rule as the player. That means the banker draws a third card with hands 0–5 and stands with 6 or 7.

Hands: the "player" and the "banker." 

Possible outcomes each round of play: "player" (player has the higher score), "banker" (banker has the higher score), and "tie."

Rules: After assigning the first four cards to player and banker (the order is player-banker-player-banker), If neither the player nor the banker is dealt a total of 8 or 9 in the first two cards (the single-digit of the sum of two cards on hand), the tableau of drawing rules is consulted, first for the player's rules, then the banker's. 

Tableu of Drawing Rules:

If the player drew a third card, the banker acts according to the following more complex rules:
* If the banker total is 2 or less, then the banker draws a card, regardless of what the player's third card is.
* If the banker total is 3, then the banker draws a third card unless the player's third card was an 8.
* If the banker total is 4, then the banker draws a third card if the player's third card was 2, 3, 4, 5, 6, 7.
* If the banker total is 5, then the banker draws a third card if the player's third card was 4, 5, 6, or 7.
* If the banker total is 6, then the banker draws a third card if the player's third card was a 6 or 7.
* If the banker total is 7, then the banker stands.

### Payoffs:

#### Traditional Payoff Rules 

1. Gamblers place bets on Bankers and Banker wins, the ratio of payoff to stake is 1:1, while the casino takes 5% commission, so the overall payoff is 0.95:1.
2. Gamblers bet on Player and Player wins, the ratio of payoff to stake is 1:1.
3. Gamblers bet on tie and tie happens, then the ratio of payoff to stake is 8:1.

| Side  |  Stake  | Payoff |
| :---: |:-------:| :-----:|
| Banker|     1   |   0.95 |
| Player|     1   |   1    |
| Tie   |     1   |   8    |

**Besides the Traditional Payoff Rules above, we invented two new payoff rules to help a casino to attract more customers (we will exam the outcomes and compare each set of new rules with traditional pay off rules later):**

#### New Payoff Rule 1

If the side a gambler bet on has a pair (2 Aces, 2 eights, etc.), the gambler gains additional 6-time payoffs, the total payoff now is 6.95:1 (Banker), 7:1 (Player), and 14:1 (tie); 
    
if the side a gambler bets on has three of a kind (3 Aces, 3 eights, etc.), the gambler gains additional 36-time payoffs, the total payoff now is 36.95:1 (Banker), 37:1 (Player), and 44:1 (tie).

**A pair shows up on the side gambler bet:**

| Side  |  Stake  | Payoff |
| :---: |:-------:| :-----:|
| Banker|     1   |   6.95 |
| Player|     1   |   7    |
| Tie   |     1   |   14   |

**Three of a kind shows up on the side gambler bet:**

| Side  |  Stake  | Payoff |
| :---: |:-------:| :-----:|
| Banker|     1   |   36.95|
| Player|     1   |   37   |
| Tie   |     1   |   44   |

#### New Payoff Rule 2

If a pair show up on the table, disregarding which side the gambler bets on, the gambler gains additional 2-time payoffs, the ratio of payoff to stake is now 2.95:1 (Banker), 3:1 (Player), and 11:1 (tie) ;

if the side a gambler bet on has three of a kind (3 Aces, 3 eights, etc.), the gambler gain additional 100-time payoffs, the total payoff now is 100.95:1 (Banker), 101:1 (Player), and 108:1 (tie). 


**A pair shows up on the table (disregarding which side the gambler bets on):**

| Side  |  Stake  | Payoff |
| :---: |:-------:| :-----:|
| Banker|     1   |   2.95 |
| Player|     1   |   3    |
| Tie   |     1   |   11   |

**Three of a kind shows up on the table (disregarding which side the gamblber bets on):**

| Side  |  Stake  | Payoff |
| :---: |:-------:| :-----:|
| Banker|     1   |  100.95|
| Player|     1   |  101   |
| Tie   |     1   |  108   |

## Purposes:
With Monte Carlo sampling method, we want to:
1. Test the theoretical expectation of each strategy (gamblers always bet on bankers, gamblers always bet on players and gamblers always bet on tie) .
2. Compare different bet ratios while controlling the strategies .
3. Explore the possibility of gamblers earning money from this game.
4. Compare the performance of three different rule bundles: 1) Traditional Payoff Rules only; 2) Traditional Payoff Rules + New Payoff Rule 1; and 3) Traditional Payoff Rules + New Payoff Rule 2
 

## Simulation's variables of uncertainty
1. Strategies: a total four kinds of strategies, which are 
    1) gamblers always bet on Player;
    2) gamblers always bet on Banker;
    3) gamblers always bet on Tie;
    4) gamblers place bets randomly (Player, Banker or Tie).
2. Ratios of bets to initial balances (abbreviation: bet ratios): 1%, 2%, 5%, 10%, 20%, 50%.
3. rounds: not tested individually, but were shown on the charts.
4. Rule Bundles (abbreviation: rules):
    1) Traditional Payoff Rules only; 
    2) Traditional Payoff Rules + New Payoff Rule 1; and 
    3) Traditional Payoff Rules + New Payoff Rule 2.

## Hypothesis or hypotheses before running the simulation:
#### Analytical variables: Strategies, Goals and Bets
Suppose gamblers carry the same balances before starting games, and the casino's balance is unlimited. Gamblers would have different strategies, goals, or bets (variables).

On our analytical stage, we want to exam the outcomes with two of the variables as controlled variables, and the rest one as a test. After we gather the outcome, we will plot them accordingly.

|             | Control 1 |  Control 2  | Control 3   |      Test    |
|:-----------:| :-------: | :---------: | :---------: |:-----------: |
|Simulation 1 | Bet ratios|     Rounds  |   Rules     |**Strategies**|
|Simulation 2 | Strategies|     Rounds  |   Rules     |**Bet ratios**|
|Simulation 3 | Bet ratios|     Rounds  |   Strategies|**Rules**     |


1. In the simulation 1, we conducted 1000 times of simulations with 2000 rounds per simulation, a bet to initial balance ratio, Traditional Payoff Rules only, and returned outcomes with the following strategies: 
    1) gamblers always bet on Player;
    2) gamblers always bet on Banker;
    3) gamblers always bet on Tie;
    4) gamblers place bets randomly (Player, Banker or Tie).
    
2. In the simulation 2, we conducted 1000 times of simulations with 2000 rounds per simulation, Traditional Payoff Rules only, random strategy and returned outcomes with the following bet ratios: 1%, 2%, 5%, 10%, 20%, and 50%.

3. In simulation 3, we conducted 1000 times of simulations with 2000 rounds per simulation, random strategy, a bet to initial balance ratio of and returned outcomes with the following Rule Bundles (abbreviation: rules):
    1) Traditional Payoff Rules only; 
    2) Traditional Payoff Rules + New Payoff Rule 1; and 
    3) Traditional Payoff Rules + New Payoff Rule 2.
    
## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)

1. 1/100,000 probability to get three exactly same card.


special>=2: if win and have 2 or 3 same card get additional money.
two same cards: 6 additional times of bet, three same cards: 36 additional times of bet
In this situation, it seems like it only affect the trends of each strategy. But the gamblers are still losing money whatever the strategy they chosed.

special<=-2: no matter win or loss, get additional money
current: 2 additional times of money if 2 cards of Bankers or Players are the same, and 100 additional times of money if 3 cards of Bankers or Players are the same.
In this situation, it will arise all trends of each strategy. But if the gamblers bet great proportion of their money (like 50%), the gamblers will earn money first (20%) and then loss money later. It is kind of a tricky strategy to hook the gamblers. But in this situation, one problem is that the gamblers only play few rounds with relative high bet proportion and leave the casino after they earned the money. So, our strategy is that force the player play 40 rounds in this special situation.

## Instructions on how to use the program:
Please run Baccarat_v2.0.py in the home directory folder.

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

## Our presentation slides:
https://docs.google.com/presentation/d/1yqReaaVZrzMYm1ZRf6JNUTihplAXr3Z5myLCViKRvLE/edit?usp=sharing

## All Sources Used:
Wikipedia (2018, Dec 02). *Baccarat (card game).* Retrieved from https://en.wikipedia.org/wiki/Baccarat_(card_game)
WikiHow. (2018, November 11). How to Play Baccarat. Retrieved from https://www.wikihow.com/Play-Baccarat
Kelly criterion. (2018, October 22). Retrieved from https://en.wikipedia.org/wiki/Kelly_criterion



