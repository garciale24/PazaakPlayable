'''
This file contains code that allows for adversarial AI's (Vanialla MCTS vs Open Loop MCTS)
'''

''' Stuff to import '''
import time

from typing import Tuple
from my_pazaak import *
from monteCarlo import *
from monteCarloOpenLoop import *

''' Function to do Vanilla MCTS '''
def player2_AI(pazaakGame: PazaakState) -> None:
    if pazaakGame.P2setVal > 10: pazaakGame = monte_carlo_algorithmOpenLoop(pazaakGame)
    return pazaakGame

''' Function to do Open Loop MCTS '''
def player1_AI(pazaakGame: PazaakState) -> None:
    if pazaakGame.P1setVal > 10: pazaakGame = monte_carlo_algorithm(pazaakGame)
    return pazaakGame

''' Function to decide what action player2 takes '''
def player2Actions(pazaakGame: PazaakState, run2: bool) -> bool:
    if pazaakGame.player == 2:
        pazaakGame = player2_AI(pazaakGame)
        run2 = False
    else: run2 = True    
    return run2, pazaakGame

''' Function to decide what action player1 takes '''
def player1Actions(pazaakGame: PazaakState, run2: bool) -> bool:
    if pazaakGame.player == 1:
        pazaakGame = player1_AI(pazaakGame)
        run2 = False
    else: run2 = True
    return run2, pazaakGame

''' Funciton to check the turns for the rounds '''
def checkRounds(rounds_checker: int, rounds_flag: int) -> Tuple[int, int]:
    if rounds_checker == 1: 
        rounds_checker = 2
    elif rounds_checker == 2: 
        rounds_checker = 1
    rounds_flag = 1
    return rounds_checker, rounds_flag

''' Function to pick whos turn it is '''
def pickTurn(rounds_flag: int, rounds_checker: int, k: int, pazaakGame: PazaakState) -> Tuple[int, int, int]:
    if rounds_flag == 0:
        if k == 1 and pazaakGame.P2stillPlaying == 1: k = 2
        elif k == 2 and pazaakGame.P1stillPlaying == 1: k = 1
        pazaakGame.player = k
    else:
        rounds_flag = 0
        pazaakGame.player = rounds_checker
        if rounds_checker == 1: k = 1
        elif rounds_checker == 2: k = 2
    return rounds_flag, rounds_checker, k

''' Function to add wins to player1 or player2 win totals '''
def addWins(pazaakGame: PazaakState, rounds_checker: int, rounds_flag: int, breaky: bool) -> Tuple[int, int, bool]:
    winner: int = 0
    winner = pazaakGame.whoWon()
    breaky = False
    if winner == 1:

        # player1 wins
        pazaakGame.P1gamesWon += 1

        # funciton to check the turns for the rounds
        rounds_checker, rounds_flag = checkRounds(rounds_checker, rounds_flag)
        breaky = True
    elif winner == 2:

        # player 2 wins
        pazaakGame.P2gamesWon += 1
        rounds_checker, rounds_flag = checkRounds(rounds_checker, rounds_flag)
        breaky = True
    elif winner == -1:

        # tie
        rounds_checker, rounds_flag = checkRounds(rounds_checker, rounds_flag)
        breaky = True
    return rounds_checker, rounds_flag, breaky

''' Function to add card to board of player1 or player2 '''
def addBoardCard(pazaakGame: PazaakState, nextCard: int) -> None: 
    if pazaakGame.player == 1 and pazaakGame.P1stillPlaying == 1:
        pazaakGame.P1boardCards.append(nextCard)
        pazaakGame.P1setVal += nextCard
    elif pazaakGame.player == 2 and pazaakGame.P2stillPlaying == 1:
        pazaakGame.P2boardCards.append(nextCard)
        pazaakGame.P2setVal += nextCard
    return None

''' Function to play 1 game of pazaak '''
def play1game(pazaakGame: PazaakState, k: int, rounds_checker: int, rounds_flag: int) -> Tuple[int, int, int, int]:
    run2: bool = True
    run: bool = True
    breaky: bool = False
    nextCard: int = 0
    pazaakGame.reset()
    pazaakGame.player = k
    while run:
        nextCard = pazaakGame.nextCard()

        # function to pick whos turn it is
        rounds_flag, rounds_checker, k = pickTurn(rounds_flag, rounds_checker, k, pazaakGame)

        # function to add wins to player1 or player2 win totals
        rounds_checker, rounds_flag, breaky = addWins(pazaakGame, rounds_checker, rounds_flag, breaky)
        if breaky: break

        # function to add card to board of player1 or player2
        addBoardCard(pazaakGame, nextCard)

        # function to decide what action player2 takes
        run2, pazaakGame = player2Actions(pazaakGame, run2)

        # function to check what action player1 takes
        run2, pazaakGame = player1Actions(pazaakGame, run2)
    return rounds_checker, rounds_flag, k, pazaakGame

''' Main function to run this file '''
def main() -> None:
    p1Wins: int = 0
    p2Wins: int = 0
    gamesIdx: int = 0
    gamesAmt: int = 1000
    start_time = time.perf_counter ()

    # Start time for games to play
    print(start_time, "st")
    while gamesIdx < gamesAmt:
        playerTurn: int = 2
        rounds_checker:int = 1
        rounds_flag: int = 0
        pazaakGame = PazaakState(playerTurn)
        pazaakGame.createSideDeck(pazaakGame.P1sideCards)
        pazaakGame.createSideDeck(pazaakGame.P2sideCards)
        while (pazaakGame.P1gamesWon < 3) and (pazaakGame.P2gamesWon < 3):

            # function to play 1 game of pazaak
            rounds_checker, rounds_flag, playerTurn, pazaakGame = play1game(pazaakGame, playerTurn, rounds_checker, rounds_flag)
            
        if pazaakGame.whoWon() == 1:
            p1Wins += 1
            p = str(p1Wins) + " " + str(p2Wins)
            print(p)
        if pazaakGame.whoWon() == 2:
            p2Wins += 1
            p = str(p1Wins) + " " + str(p2Wins)
            print(p)
        gamesIdx += 1
    end_time = time.perf_counter ()

    # Print total time taken and player 1 and 2 wins
    print(end_time - start_time, "seconds")
    print("P1Wins:", p1Wins, "P2Wins:", p2Wins)
    return None

if __name__ == "__main__":
    main()