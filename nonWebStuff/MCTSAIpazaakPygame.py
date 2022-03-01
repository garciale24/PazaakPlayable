'''
This file contains code that allows for a playable version of the Pazaak game (Vanilla MCTS vs Human) 
'''

''' Stuff needed for import '''
import pygame

from typing import Tuple
from my_pazaak import *
from monteCarlo import *
from draw_stuff import *

''' Function to quit the game '''
def quit_game(event: pygame) -> None:
    if event.type == pygame.QUIT:
        pygame.quit()
        exit(0)
    return None

''' Function to run Vanilla MCTS AI '''
def player2_AI(pazaakGame: PazaakState) -> None:
    P2sideCardsTemp = pazaakGame.P2sideCards
    retpazaakGame = monte_carlo_algorithm(pazaakGame)
    if retpazaakGame.P2pop != -1:
        wait_timer(1)
        SIDE_DECK_DIS2.pop(retpazaakGame.P2pop)
        retpazaakGame.P2boardCards.append(P2sideCardsTemp[retpazaakGame.P2pop][0])
    return retpazaakGame

''' Timer with functionality to quit the game '''
def wait_timer(multiplier: int) -> None:
    run3: bool = True
    run3= True
    st = pygame.time.get_ticks()
    while run3:
        for event in pygame.event.get(): quit_game(event)
        et = pygame.time.get_ticks()
        if et - st >= 1000*multiplier: run3 = False
    return None

''' Function that checks to see if player 1 selected a side card '''
def player1SideCardSelection(selected_side_card: bool, pazaakGame: PazaakState, MOUSE_X: int, MOUSE_Y: int) -> bool:
    i: int = 0
    if pazaakGame.P1stillPlaying == 1 and selected_side_card:
        for card in SIDE_DECK_DIS:
            if card[0] <= MOUSE_X and MOUSE_X <= card[0] + 52* SIZE:
                if card[1] <= MOUSE_Y and MOUSE_Y <= card[1] + 60* SIZE:
                    SIDE_DECK_DIS.pop(i)
                    card = pazaakGame.P1sideCards.pop(i)
                    pazaakGame.P1boardCards.append(card[0])
                    pazaakGame.P1setVal += card[0]
                    draw_window(pazaakGame)
                    selected_side_card = False
                    if pazaakGame.P1setVal >= 20: 
                        pazaakGame.P1stillPlaying = 0
                        break
            i += 1
    return selected_side_card

''' Funciton that checks to see if player1 selected 'End Turn' or 'Stand' '''
def player1EndTurnStand(pazaakGame: PazaakState, MOUSE_X: int, MOUSE_Y: int, run2: bool) -> bool:
    if int(MOUSE_X) <= 520* SIZE and int(MOUSE_X) >= 380* SIZE:
        if int(MOUSE_Y) <= 300* SIZE and int(MOUSE_Y) >= 250* SIZE:
            if pazaakGame.player == 1: pazaakGame.P1stillPlaying = 0
            run2 = False
        if int(MOUSE_Y) <= 200* SIZE and int(MOUSE_Y) >= 150* SIZE:
            if pazaakGame.P1setVal >= 20: pazaakGame.P1stillPlaying = 0
            run2 = False
    return run2

''' Function to decide what action player2 takes '''
def player2Actions(pazaakGame: PazaakState, run2: bool) -> bool:
    if pazaakGame.player == 2:
        pazaakGame = player2_AI(pazaakGame)
        run2 = False
    else: run2 = True
    return run2, pazaakGame

''' Function call that checks what action player1 wants to take '''
def player1Actions(pazaakGame: PazaakState, run2: bool) -> bool:
    selected_side_card: bool = True
    while run2:     
        for event in pygame.event.get():
            quit_game(event)
            if run2 == False: break
            if event.type == pygame.MOUSEBUTTONDOWN:
                MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()

                # this function call checks to see if player2 selected a side card to play
                selected_side_card = player1SideCardSelection(selected_side_card, pazaakGame, int(MOUSE_X), int(MOUSE_Y))

                # this function call checks to see if player2 pressed, 'End Turn' or 'Stand'
                run2 = player1EndTurnStand(pazaakGame, int(MOUSE_X), int(MOUSE_Y), run2)
    draw_window(pazaakGame)
    return run2

''' Funciton to check the turns for the rounds '''
def checkRounds(rounds_checker: int, rounds_flag: int) -> Tuple[int, int]:
    if rounds_checker == 1: rounds_checker = 2
    elif rounds_checker == 2: rounds_checker = 1
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
    P1Wins: int = 0
    P2Wins: int = 0
    winner: int = 0
    winner = pazaakGame.whoWon()
    breaky = False
    if winner == 1:
        pazaakGame.P1gamesWon += 1
        P1Wins += 1
        rounds_checker, rounds_flag = checkRounds(rounds_checker, rounds_flag)
        breaky = True
    elif winner == 2:
        pazaakGame.P2gamesWon += 1
        P2Wins +=1
        rounds_checker, rounds_flag = checkRounds(rounds_checker, rounds_flag)
        breaky = True
    elif winner == -1:
        rounds_checker, rounds_flag = checkRounds(rounds_checker, rounds_flag)
        breaky = True
    return rounds_checker, rounds_flag, breaky, pazaakGame

''' Function to add card to board of player1 or player2 '''
def addBoardCard(pazaakGame: PazaakState, nextCard: int) -> None: 
    if pazaakGame.player == 1 and pazaakGame.P1stillPlaying == 1:
        pazaakGame.P1boardCards.append(nextCard)
        pazaakGame.P1setVal += nextCard
    elif pazaakGame.player == 2 and pazaakGame.P2stillPlaying == 1:
        pazaakGame.P2boardCards.append(nextCard)
        pazaakGame.P2setVal += nextCard
    draw_window(pazaakGame)
    return None

''' Function to play 1 game of pazaak '''
def play1game(pazaakGame: PazaakState, k: int, rounds_checker: int, rounds_flag: int) -> Tuple[int, int, int]:
    run2: bool = True
    run: bool = True
    breaky: bool = False
    nextCard: int = 0
    clock: pygame = pygame.time.Clock()
    pazaakGame.reset()
    pazaakGame.player = k
    for event in pygame.event.get(): quit_game(event)
    while run:
        clock.tick(FPS)
        wait_timer(1) 
        nextCard = pazaakGame.nextCard()

        # function to pick whos turn it is
        rounds_flag, rounds_checker, k = pickTurn(rounds_flag, rounds_checker, k, pazaakGame)

        # function to add wins to player1 or player2 win totals
        rounds_checker, rounds_flag, breaky, pazaakGame = addWins(pazaakGame, rounds_checker, rounds_flag, breaky)
        if breaky: break

        # function to add card to board of player1 or player2
        addBoardCard(pazaakGame, nextCard)

        # function to decide what action player2 takes
        run2, pazaakGame = player2Actions(pazaakGame, run2)

        # function to check what action player1 takes
        player1Actions(pazaakGame, run2)
    draw_window(pazaakGame)
    return rounds_checker, rounds_flag, k, pazaakGame

''' Main function to run playable version '''
def main() -> None:
    playerTurn: int = 2
    rounds_checker:int = 1
    rounds_flag: int = 0
    pazaakGame = PazaakState(playerTurn)
    pazaakGame.createSideDeck(pazaakGame.P1sideCards)
    pazaakGame.createSideDeck(pazaakGame.P2sideCards)
    pazaakGame.mctsVersion = "Vanilla"
    draw_window(pazaakGame)
    while (pazaakGame.P1gamesWon < 3) and (pazaakGame.P2gamesWon < 3):

        # function to play 1 game of pazaak
        rounds_checker, rounds_flag, playerTurn, pazaakGame = play1game(pazaakGame, playerTurn, rounds_checker, rounds_flag)
        wait_timer(1)
    draw_window(pazaakGame)

    if pazaakGame.P1gamesWon == 3:
        draw_winner(1)
        wait_timer(5)
    elif pazaakGame.P2gamesWon == 3:
        draw_winner(2)
        wait_timer(5)

    # Game is over
    pygame.quit()
    return None

if __name__ == "__main__":
    main()