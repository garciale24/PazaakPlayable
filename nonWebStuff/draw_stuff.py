'''
This file is used to Draw out the UI for the Playable versions of the game.
'''

''' Stuff needed for import '''
import os
import pygame

from MCTSnoUCBAIpazaakPygame import *
from MCTSopAIpazaakPygame import *
from MCTSAIpazaakPygame import *
from SimpleAIpazaakPygame import *

from MCTSnoUCBAIpazaakPygameP2 import *
from MCTSopAIpazaakPygameP2 import *
from MCTSAIpazaakPygameP2 import *
from MCTSAIpazaakPygameP2 import *

''' Adjust size of game here '''
SIZE = 1.6

pygame.init()
pygame.font.init()

NUM_BOARD_CARDSP1: int = 0
NUM_BOARD_CARDSP2: int = 0

''' Colors '''
BLUEISH: Tuple = (52, 122, 235)
BLACK: Tuple = (0, 0, 0)
RED: Tuple = (180, 20, 5)
GREEN: Tuple = (0, 128, 0)
FPS: int = 60

''' Background '''
BACKG: pygame = pygame.image.load(os.path.join('assets/B.jpg'))
BG = pygame.transform.scale(BACKG, (int(900*SIZE), int(500*SIZE)))

WIDTH = int(900 * SIZE)
HEIGHT = int(500 * SIZE)
WIN: pygame = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("PazaakMCTS")

MOUSE_X: int = 0
MOUSE_Y: int = 0

''' Round circle locations for Player 1 '''
P1_CIRCLES: List[Tuple[int]] = [
    (int(253* SIZE), int(24* SIZE)), 
    (int(308* SIZE), int(24* SIZE)),
    (int(365* SIZE), int(24* SIZE))]

''' Round circle locations for Player 2 '''
P2_CIRCLES: List[Tuple[int]] = [
    (int(537* SIZE), int(24* SIZE)), 
    (int(593* SIZE), int(24* SIZE)),
    (int(649* SIZE), int(24* SIZE))]

''' Turn indicator Locations '''
Pturn: List[Tuple[int]] = [
    (int(40* SIZE), int(15* SIZE)),
    (int(860* SIZE), int(15* SIZE))
]

''' Board Card locations for Player 2 '''
P2_BOARD_DIS: List[Tuple[int]] = [
    (int(536* SIZE), int(101* SIZE)),
    (int(647* SIZE), int(101* SIZE)),
    (int(760* SIZE), int(101* SIZE)),
    (int(536* SIZE), int(184* SIZE)),
    (int(647* SIZE), int(184* SIZE)),
    (int(760* SIZE), int(184* SIZE)),
    (int(536* SIZE), int(270* SIZE)),
    (int(647* SIZE), int(270* SIZE)),
    (int(760* SIZE), int(270* SIZE))
]

''' Board Card locations for Player 1 '''
P1_BOARD_DIS: List[Tuple[int]] = [
    (int(88* SIZE), int(101* SIZE)),
    (int(200* SIZE), int(101* SIZE)),
    (int(311* SIZE), int(101* SIZE)),
    (int(88* SIZE), int(184* SIZE)),
    (int(200* SIZE), int(184* SIZE)),
    (int(311* SIZE), int(184* SIZE)),
    (int(88* SIZE), int(270* SIZE)),
    (int(200* SIZE), int(270* SIZE)),
    (int(311* SIZE), int(270* SIZE)),
]

''' Side Deck locations for Player 1 '''
SIDE_DECK_DIS: List[List[int]] = [
    [int(45* SIZE), int(367* SIZE)],
    [int(153* SIZE), int(367* SIZE)],
    [int(250* SIZE), int(367* SIZE)],
    [int(355* SIZE), int(367* SIZE)]]

''' Side Deck locations for Player 2 '''
SIDE_DECK_DIS2: List[List[int]] = [
    [int(494* SIZE), int(367* SIZE)],
    [int(599* SIZE), int(367* SIZE)],
    [int(696* SIZE), int(367* SIZE)],
    [int(802* SIZE), int(367* SIZE)]]

''' At the end of the game, draw the name of the Winner '''
def draw_winner(player: int, pazaakGame: PazaakState) -> None:
    font = pygame.font.Font(None, int(128* SIZE))
    text = font.render("Player" + str(player) + " Wins", True, RED)

    # This if-statement will give proper names for Vanilla MCTS vs Human 
    if pazaakGame.mctsVersion == "Vanilla":
        if player == 1:
            text = font.render("Human" + " player" + " Wins", True, RED)
        else:
            text = font.render("MCTS" + " player" + " Wins", True, RED)

    # This if-statement will give proper names for Vanilla MCTS vs Human 
    elif pazaakGame.mctsVersion == "VanillaP2":
        if player == 1:
            text = font.render("MCTS" + " player" + " Wins", True, RED)
        else:
            text = font.render("Human" + " player" + " Wins", True, RED)

    # This if-statement will give proper names for no UCB MCTS vs Human 
    elif pazaakGame.mctsVersion == "no UCB":
        if player == 1:
            text = font.render("Human" + " player" + " Wins", True, RED)
        else:
            text = font.render("No UCB" + " player" + " Wins", True, RED)

    # This if-statement will give proper names for Human vs no UCB MCTS 
    elif pazaakGame.mctsVersion == "no UCBP2":
        if player == 1:
            text = font.render("No UCB" + " player" + " Wins", True, RED)
        else:
            text = font.render("Human" + " player" + " Wins", True, RED)

    # This if-statement will give proper names for Open Loop MCTS vs Human 
    elif pazaakGame.mctsVersion == "Open Loop":
        if player == 1:
            text = font.render("Human" + " player" + " Wins", True, RED)
        else:
            text = font.render("O.L." + " player" + " Wins", True, RED)

    # This if-statement will give proper names for Human vs Open Loop MCTS 
    elif pazaakGame.mctsVersion == "Open LoopP2":
        if player == 1:
            text = font.render("O.L." + " player" + " Wins", True, RED)
        else:
            text = font.render("Human" + " player" + " Wins", True, RED)

    # This if-statement will give proper names for Simple AI vs Human 
    elif pazaakGame.mctsVersion == "Simple":
        text = font.render("Human" + " player" + " Wins", True, RED)

    # This else-statement will give default names of 'Player 1' and 'Player 2'
    else:
        img = font.render('Player 1', True, BLUEISH)
        WIN.blit(img, (int(63* SIZE), int(10* SIZE)))
        img2 = font.render('Player 2', True, BLUEISH)
        WIN.blit(img2, (int(732* SIZE), int(10* SIZE)))

    text_rect = text.get_rect(center=(int(450* SIZE), int(100* SIZE)))
    WIN.blit(text, text_rect)
    pygame.display.update()
    return None

''' This function will grab the selected card from the card images available '''
def get_card(nextCard: int) ->  pygame:
    i: int = -10
    while i < 10:
        if nextCard == i:
            plus: pygame = pygame.image.load(os.path.join('assets/plus' + str(i) + '.png'))
            Plus = pygame.transform.scale(plus, (int(52* SIZE), int(60* SIZE)))
            return Plus
        i += 1
    return None

''' This function draws the game boardin its current state '''
def draw_window(pazaakGame: PazaakState) -> None:
    i: int = 0
    WIN.blit(BG, (0, 0))
    font = pygame.font.Font("assets/times.ttf", int(32* SIZE))

    # This if-statement will place a Red 'S' next to the player 1 if they stand 
    if pazaakGame.P1stillPlaying == 0:
        S1 = font.render('S', True, RED)
        WIN.blit(S1, ( int(185* SIZE), int(10* SIZE)))

    # This if-statement will place a Red 'S' next to the player 2 if they stand 
    if pazaakGame.P2stillPlaying == 0:
        S2 = font.render('S', True, RED)
        WIN.blit(S2, ( int(700* SIZE), int(10* SIZE)))

    # This if-statement will give proper names for Vanilla MCTS vs Human 
    if pazaakGame.mctsVersion == "Vanilla":
        img = font.render('Human', True, BLUEISH)
        WIN.blit(img, (int(63* SIZE), int(10* SIZE)))
        img2 = font.render('MCTS', True, BLUEISH)
        WIN.blit(img2, (int(732* SIZE), int(10* SIZE)))

    # This if-statement will give proper names for Vanilla MCTS vs Human 
    elif pazaakGame.mctsVersion == "VanillaP2":
        img = font.render('MCTS', True, BLUEISH)
        WIN.blit(img, (int(63* SIZE), int(10* SIZE)))
        img2 = font.render('Human', True, BLUEISH)
        WIN.blit(img2, (int(732* SIZE), int(10* SIZE)))

    # This if-statement will give proper names for no UCB MCTS vs Human 
    elif pazaakGame.mctsVersion == "no UCB":
        img = font.render('Human', True, BLUEISH)
        WIN.blit(img, (int(63* SIZE), int(10* SIZE)))
        img2 = font.render('No UCB', True, BLUEISH)
        WIN.blit(img2, (int(732* SIZE), int(10* SIZE)))

    # This if-statement will give proper names for Human vs no UCB MCTS 
    elif pazaakGame.mctsVersion == "no UCBP2":
        img = font.render('No UCB', True, BLUEISH)
        WIN.blit(img, (int(63* SIZE), int(10* SIZE)))
        img2 = font.render('Human', True, BLUEISH)
        WIN.blit(img2, (int(732* SIZE), int(10* SIZE)))

    # This if-statement will give proper names for Open Loop MCTS vs Human 
    elif pazaakGame.mctsVersion == "Open Loop":
        img = font.render('Human', True, BLUEISH)
        WIN.blit(img, (int(63* SIZE), int(10* SIZE)))
        img2 = font.render('O.L.', True, BLUEISH)
        WIN.blit(img2, (int(732* SIZE), int(10* SIZE)))

    # This if-statement will give proper names for Human vs Open Loop MCTS 
    elif pazaakGame.mctsVersion == "Open LoopP2":
        img = font.render('O.L.', True, BLUEISH)
        WIN.blit(img, (int(63* SIZE), int(10* SIZE)))
        img2 = font.render('Human', True, BLUEISH)
        WIN.blit(img2, (int(732* SIZE), int(10* SIZE)))

    # This if-statement will give proper names for Simple AI vs Human 
    elif pazaakGame.mctsVersion == "Simple":
        img = font.render('Human', True, BLUEISH)
        WIN.blit(img, (int(63* SIZE), int(10* SIZE)))
        img2 = font.render('Simple AI', True, BLUEISH)
        WIN.blit(img2, (int(715* SIZE), int(10* SIZE)))

    # This else-statement will give default names of 'Player 1' and 'Player 2'
    else:
        img = font.render('Player 1', True, BLUEISH)
        WIN.blit(img, (int(63* SIZE), int(10* SIZE)))
        img2 = font.render('Player 2', True, BLUEISH)
        WIN.blit(img2, (int(732* SIZE), int(10* SIZE)))

    # This is to display the value totals of player 1 and 2's board cards
    img1 = font.render(str(pazaakGame.P1setVal), True, BLUEISH)
    WIN.blit(img1, (int(400* SIZE), int(10* SIZE)))
    img2_1 = font.render(str(pazaakGame.P2setVal), True, BLUEISH)
    WIN.blit(img2_1, (int(465* SIZE), int(10* SIZE)))

    # These 2 while loops add Red circles to indicate amount of sets won
    radius = int(10* SIZE)
    i = 0
    while i < pazaakGame.P1gamesWon:
        pygame.draw.circle(WIN, RED, P1_CIRCLES[i], radius)
        i += 1
    i = 0
    while i < pazaakGame.P2gamesWon:
        pygame.draw.circle(WIN, RED, P2_CIRCLES[i], radius)
        i += 1
    
    # Draw Green circle on side of current players turn
    if pazaakGame.player == 1:
        pygame.draw.circle(WIN, GREEN, Pturn[0], radius)
    else:
        pygame.draw.circle(WIN, GREEN, Pturn[1], radius)

    # Assets for 'End Game' and 'Stand' buttons
    ET = pygame.image.load('assets/ET.png')
    E = pygame.transform.scale(ET, (int(140* SIZE), int(50* SIZE)))
    WIN.blit(E, (int(380* SIZE), int(150* SIZE)))

    ET2 = pygame.image.load('assets/ET.png')
    E2 = pygame.transform.scale(ET2, (int(140* SIZE), int(50* SIZE)))
    WIN.blit(E2, (int(380* SIZE), int(250* SIZE)))

    font = pygame.font.Font(None, int(40* SIZE))
    text = font.render("End Turn", True, BLUEISH)
    text_rect = text.get_rect(center=(int(450* SIZE), int(175* SIZE)))
    WIN.blit(text, text_rect)

    font2 = pygame.font.Font(None, int(40* SIZE))
    text2 = font2.render("Stand", True, BLUEISH)
    text_rect2 = text2.get_rect(center=(int(450* SIZE), int(275* SIZE)))
    WIN.blit(text2, text_rect2)

    # Draw fancy lines across the board
    pygame.draw.line(WIN, BLACK, (int(450* SIZE), int(150* SIZE)), (int(450* SIZE), int(0* SIZE)), int(5* SIZE))
    pygame.draw.line(WIN, BLACK, (int(380* SIZE), int(150* SIZE)), (int(520* SIZE), int(150* SIZE)), int(5* SIZE))
    pygame.draw.line(WIN, BLACK, (int(380* SIZE), int(150* SIZE)), (int(380* SIZE), int(200* SIZE)), int(5* SIZE))
    pygame.draw.line(WIN, BLACK, (int(380* SIZE), int(200* SIZE)), (int(520* SIZE), int(200* SIZE)), int(5* SIZE))
    pygame.draw.line(WIN, BLACK, (int(520* SIZE), int(150* SIZE)), (int(520* SIZE), int(200* SIZE)), int(5* SIZE))
    pygame.draw.line(WIN, BLACK, (int(450* SIZE), int(200* SIZE)), (int(450* SIZE), int(250* SIZE)), int(5* SIZE))
    pygame.draw.line(WIN, BLACK, (int(380* SIZE), int(300* SIZE)), (int(520* SIZE), int(300* SIZE)), int(5* SIZE))
    pygame.draw.line(WIN, BLACK, (int(380* SIZE), int(250* SIZE)), (int(380* SIZE), int(300* SIZE)), int(5* SIZE))
    pygame.draw.line(WIN, BLACK, (int(380* SIZE), int(250* SIZE)), (int(520* SIZE), int(250* SIZE)), int(5* SIZE))
    pygame.draw.line(WIN, BLACK, (int(520* SIZE), int(250* SIZE)), (int(520* SIZE), int(300* SIZE)), int(5* SIZE))
    pygame.draw.line(WIN, BLACK, (int(450* SIZE), int(500* SIZE)), (int(450* SIZE), int(300* SIZE)), int(5* SIZE))

    # Display all the board cards and side cards for player 1 and player 2
    i = 0
    while i < len(pazaakGame.P1boardCards):
        card = get_card(pazaakGame.P1boardCards[i])
        WIN.blit(card, (P1_BOARD_DIS[i]))
        i += 1
    i = 0
    while i < len(pazaakGame.P2boardCards):
        card = get_card(pazaakGame.P2boardCards[i])
        WIN.blit(card, (P2_BOARD_DIS[i]))
        i += 1
    i = 0
    while i < len(SIDE_DECK_DIS):
        new_card = get_card(pazaakGame.P1sideCards[i][0])
        WIN.blit(new_card, (SIDE_DECK_DIS[i]))
        i += 1
    i = 0
    while i < len(SIDE_DECK_DIS2):
        new_card = get_card(pazaakGame.P2sideCards[i][0])
        WIN.blit(new_card, (SIDE_DECK_DIS2[i]))
        i += 1
    
    # Display all the new updates
    pygame.display.update()
    return None