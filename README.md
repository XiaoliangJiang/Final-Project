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
1. Gamblers place bets on Bankers and Banker wins, the ratio of payoff to stake is 1:1, while the casino takes 5% commission, so the overall payoff is 0.95:1.
2. Gamblers bet on Player and Player wins, the ratio of payoff to stake is 1:1.
3. Gamblers bet on tie and tie happens, then the ratio of payoff to stake is 8:1.

**Besides the classic payoff rules above, we invented two new rules of payoff to help a casino to attract more customers (we will exam the outcomes and compare each one with traditional rules later):**
**1. If the side a gambler bet on has a pair (2 Aces, 2 eights, etc.), the gambler gains additional 6-time payoffs, the total payoff now is 6.95:1 (Banker), 7:1 (Player), and 14:1 (tie); **
    
    **if the side a gambler bets on has three of a kind (3 Aces, 3 eights, etc.), the gambler gains additional 36-time payoffs, the total payoff now is 36.95:1 (Banker), 37:1 (Player), and 44:1 (tie).**
**2. If a pair show up on the table, disregarding which side the gamblber bets on, the gambler gains additional 2-time payoffs, the ratio of payoff to stake is now 2.95:1 (Banker), 3:1 (Player), and 11:1 (tie) ;**

    **if the side a gambler bet on has three of a kind (3 Aces, 3 eights, etc.), the gambler gain additional 100-time payoffs, the total payoff now is 100.95:1 (Banker), 101:1 (Player), and 108:1 (tie). **

## Purposes:
With Monte Carlo sampling method, we want to:
1. Test the theoretical expectation of each strategy (gamlbers always bet on bankers, gamlbers always bet on players and gamblers always bet on tie) .
2. Compare different bet ratios while controling the strategies .
3. Explore the possibility of gamblers earning money from this game.
4. Besides the traditional rules, we want to exam the outcomes when a new rule is added: when 
 

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

1. 1/100,000 probability to get three exactly same card.


special>=2: if win and have 2 or 3 same card get additional money.
two same cards: 6 additional times of bet, three same cards: 36 additional times of bet
In this situation, it seems like it only affect the trends of each strategy. But the gamblers are still losing money whatever the strategy they chosed.

special<=-2: no matter win or loss, get additional money
current: 2 additional times of money if 2 cards of Bankers or Players are the same, and 100 additional times of money if 3 cards of Bankers or Players are the same.
In this situation, it will arise all trends of each strategy. But if the gamblers bet great proportion of their money (like 50%), the gamblers will earn money first (20%) and then loss money later. It is kind of a tricky strategy to hook the gamblers. But in this situation, one problem is that the gamblers only play few rounds with relative high bet proportion and leave the casino after they earned the money. So, our strategy is that force the player play 40 rounds in this special situation.

## Instructions on how to use the program:

## Our presentation slides:
https://docs.google.com/presentation/d/1yqReaaVZrzMYm1ZRf6JNUTihplAXr3Z5myLCViKRvLE/edit?usp=sharing

## All Sources Used:
Wikipedia (2018, Dec 02). *Baccarat (card game).* Retrieved from https://en.wikipedia.org/wiki/Baccarat_(card_game)
WikiHow. (2018, November 11). How to Play Baccarat. Retrieved from https://www.wikihow.com/Play-Baccarat
Kelly criterion. (2018, October 22). Retrieved from https://en.wikipedia.org/wiki/Kelly_criterion



