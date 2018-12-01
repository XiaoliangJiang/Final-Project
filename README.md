# 590PR Final_Project
Fork from here to create your final project repository.

Two things are different than all the previous assignments in 590PR regarding the permissions settings:

1. Please KEEP the "All_Students" team to have Read access.  
2. Whenever you choose to, you are welcome to change your Final Project repository to private or to public.  This will enable you to list it in your resume, website, or other portfolio.

DELETE these lines from TEMPLATE up.

TEMPLATE for your report to fill out:

# Title: Monte Carlo Method for Baccarat (card game)
## Team Member(s):
Xiaoliang Jiang and Te Lin

# Monte Carlo Simulation Scenario & Purpose:
(be sure to read the instructions given in course Moodle)
## Senario:
Baccarat is a popular card game played at casinos, especially among Asian gamblers.

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
List and describe your simulation's variables of uncertainty (where you're using pseudo-random number generation). For each such variable, how did you decide the range and probability distribution to use?  Do you think it's a good representation of reality?

## Hypothesis or hypotheses before running the simulation:


## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)

## Instructions on how to use the program:

## All Sources Used:
