# Monte Carlo Tree Search for Pazaak; a Star Wars Card Game
## Project website link
https://garciale24.github.io/PazaakPlayable/

## Acknowledgements 
**Author:** Carlos García-Lemus

**Advisor:** Dr. Canaan

**Course:** CSC 491/492 Senior Project I & II 

**Affiliation:** California Polytechnic University, San Luis Obispo Computer Science Department

**Completion Date:** 03/18/2022 

## Instructions for this project
**Requirements:**
 
* Python 3.8.10 (To write the logic for the MCTS implementations)
* Pygame version 1.9.6 (For the game vizuals)
* React JS App version 0.1.0 (To create a website for the AI's)  
* Trinket (To create your own Pygame implementatioin of MCTS AI for a website)

**How to run this project:**

This project can be run using the website link provided above. There are instructions there for navigating the website as well as instructions for how to play against any of the MCTS agents in this project.

**How to play:**

Pazaak is played with two players, Player 1 and Player 2. These two players will play a ‘best-of-five’ (first to win three sets wins the game) series. Each set within the game will consist of both players attempting to reach as close to 20 (or 20 itself) without going over 20 (21 and over). The first set will begin with Player 1 receiving a card from a randomly generated infinite deck, this card will have a value of 1-10. After receiving the card from the deck, Player 1 may choose to select 1 ‘side card’ from their side deck in order to either add to their set value total or to reduce their set value total and then they will have the option to 'stand'. After Player 1 finishes their turn, Player 2 will have the same thing happen to them; receive a card from the deck, they will get a chance to play 1 ‘side card’ if there are any available, and finally they will have the option to 'stand'. Player 1 and Player 2 will continue alternating turns like this until both players are done playing at which point a winner will be calculated (or if a tie occurs, no wins are allotted and both players begin a new set). At the beginning of each new set, Player 1 and Player 2 will switch their ordering on who goes first. A player can choose to stop playing or ‘stand’ at the end of their turn which will allow them to stick with their current set value total and will make it so that said player will no longer receive cards from the deck (and it will also make it so that said player will no longer be able to play any ‘side cards’) until the current set is over. For example, suppose Player 1 has a set value of 14 and Player 2 has a set value of 17. Now let’s say that Player 1 gets a ‘+5’ card from the deck, thus putting their total set value up to 19 (14 + 5 = 19). In this instance, it would be smart for Player 1 to ‘stand’ and thus sticking with that 19 value for the rest of the set which would allow for a good chance of victory (Player 2 would need to get a perfect set value of 20 to win or a set value of 19 to tie Player 1). Now let’s suppose that from the previous example that Player 1 had a ‘+1’ ‘side card’. In that scenario, Player 1 could’ve played that ‘+1’ ‘side card’ at the end of their turn thus bringing their set value total up to 20 (14 + 5 + 1 = 20). This set value would be even better than 19 seeing as Player 2 will no longer be able to win (only tie) thus increasing the chances for victory even more. Here is a link to a Google Doc which has more examples: https://docs.google.com/document/d/1SgyQcBeaWXy5FqP7iBZUUl8MWtADo1wraGp5-ovZCGs/edit?usp=sharing

## Futher Acknowledgements

**[1] Procreate website link**

Procreate. 2022. Procreate® – Sketch, Paint, Create.. [online] Available at: https://procreate.art/ [Accessed 17 March 2022].

**[2] Article on Typed Python**

Radečić, D., 2022. How to Make Python Statically Typed — The Essential Guide. [online] Medium. Available at: https://towardsdatascience.com/how-to-make-python-statically-typed-the-essential-guide-e087cf4fa400  [Accessed 17 March 2022].

**[3] More on Typed Python**

Docs.python.org. 2022. typing — Support for type hints — Python 3.10.3 documentation. [online] Available at: https://docs.python.org/3/library/typing.html [Accessed 17 March 2022].

**[4] Pygame Wikipedia**

En.wikipedia.org. 2022. Pygame - Wikipedia. [online] Available at: https://en.wikipedia.org/wiki/Pygame [Accessed 17 March 2022].

**[5] React Wikipedia**

En.wikipedia.org. 2022. React (JavaScript library) - Wikipedia. [online] Available at: https://en.wikipedia.org/wiki/React_(JavaScript_library) [Accessed 17 March 2022].

**[6] Trinket website link**

Hauser, E., Marks, B. and Wheeler, B., 2022. Trinket. [online] Trinket.io. Available at: https://trinket.io/ [Accessed 17 March 2022].

**[7] Pazaak Wookieepedia (Wikipedia)**

“Pazaak/Legends.” Wookieepedia, starwars.fandom.com. Accessed 7 Feb. 2022, https://starwars.fandom.com/wiki/Pazaak/Legends 

**[8] Other MCTS Python implementations (GitHub repository)**

Bojinov, G., 2022. GitHub - Nimor111/pazaak-python: A pazaak game using Monte Carlo Tree Search, written in Python. [online] GitHub. Available at: https://github.com/Nimor111/pazaak-python [Accessed 17 March 2022].

**[9] MCTS image GeeksforGeeks**

GeeksforGeeks. 2022. ML | Monte Carlo Tree Search (MCTS) - GeeksforGeeks. [online] Available at: https://www.geeksforgeeks.org/ml-monte-carlo-tree-search-mcts/  [Accessed 17 March 2022].

**[10] Drawio website link**

App.diagrams.net. 2022. Flowchart Maker & Online Diagram Software. [online] Available at: https://app.diagrams.net/ [Accessed 17 March 2022].

**[11] Cameron Browne- MTCS slides**

Browne, Cameron. “Monte Carlo Tree Search - Goldsmiths, University of London.” Http://Ccg.doc.gold.ac.uk, Mar. 2012, http://ccg.doc.gold.ac.uk/ccg_old/teaching/ludic_computing/ludic16.pdf.

**[12] MCTS Wikipedia**

“Monte Carlo Tree Search.” Wikipedia, Wikimedia Foundation, 23 Jan. 2022, https://en.wikipedia.org/wiki/Monte_Carlo_tree_search.

**[13] UCB article**

SALLOUM, Z., 2022. Monte Carlo Tree Search in Reinforcement Learning. [online] Medium. Available at: https://towardsdatascience.com/monte-carlo-tree-search-in-reinforcement-learning-b97d3e743d0f [Accessed 17 March 2022].

**[14] Tableau website**

Stolte, C., Chabot, C. and Hanrahan, P., 2022. [online] Tableau. Available at: https://www.tableau.com/ [Accessed 18 March 2022].



