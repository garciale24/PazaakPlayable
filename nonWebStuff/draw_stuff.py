import pygame
import os
import time

from MCTSopAIpazaakPygame import *
from MCTSAIpazaakPygame import *
from SimpleAIpazaakPygame import *

SIZE = 1.6

pygame.init()
pygame.font.init()

NUM_BOARD_CARDSP1: int = 0
NUM_BOARD_CARDSP2: int = 0

BLUEISH: Tuple = (52, 122, 235)
BLACK: Tuple = (0, 0, 0)
RED: Tuple = (180, 20, 5)
GREEN: Tuple = (0, 128, 0)
FPS: int = 60

#print(os.listdir('assets'))
BACKG: pygame = pygame.image.load(os.path.join('assets/B.jpg'))
BG = pygame.transform.scale(BACKG, (int(900*SIZE), int(500*SIZE)))

WIDTH = int(900 * SIZE)
HEIGHT = int(500 * SIZE)
#print(WIDTH)
#print(HEIGHT)
WIN: pygame = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("my_Pazaak")

MOUSE_X: int = 0
MOUSE_Y: int = 0

P1_CIRCLES: List[Tuple[int]] = [
    (int(253* SIZE), int(24* SIZE)), 
    (int(308* SIZE), int(24* SIZE)),
    (int(365* SIZE), int(24* SIZE))]

P2_CIRCLES: List[Tuple[int]] = [
    (int(537* SIZE), int(24* SIZE)), 
    (int(593* SIZE), int(24* SIZE)),
    (int(649* SIZE), int(24* SIZE))]

Pturn: List[Tuple[int]] = [
    (int(40* SIZE), int(15* SIZE)),
    (int(860* SIZE), int(15* SIZE))
]

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


SIDE_DECK_DIS: List[List[int]] = [
    [int(45* SIZE), int(367* SIZE)],
    [int(153* SIZE), int(367* SIZE)],
    [int(250* SIZE), int(367* SIZE)],
    [int(355* SIZE), int(367* SIZE)]]

SIDE_DECK_DIS2: List[List[int]] = [
    [int(494* SIZE), int(367* SIZE)],
    [int(599* SIZE), int(367* SIZE)],
    [int(696* SIZE), int(367* SIZE)],
    [int(802* SIZE), int(367* SIZE)]]



def draw_winner(player: int) -> None:
    font = pygame.font.Font(None, int(128* SIZE))
    text = font.render("Player" + str(player) + " Wins", True, RED)
    text_rect = text.get_rect(center=(int(450* SIZE), int(100* SIZE)))
    WIN.blit(text, text_rect)
    pygame.display.update()
    return None

def get_card(nextCard: int) ->  pygame:
    i: int = -10
    while i < 10:
        if nextCard == i:
            plus: pygame = pygame.image.load(os.path.join('assets/plus' + str(i) + '.png'))
            Plus = pygame.transform.scale(plus, (int(52* SIZE), int(60* SIZE)))
            return Plus
        i += 1

    return None

def draw_window(pazaakGame: PazaakState) -> None:
    i: int = 0

    #WIN.fill(BLUEISH)
    WIN.blit(BG, (0, 0))


    #time.sleep(10)

    font = pygame.font.Font("assets/times.ttf", int(32* SIZE))
    #time.sleep(10)
    print("yo", pazaakGame.P1stillPlaying)
    print("yee")
    if pazaakGame.P1stillPlaying == 0:
        S1 = font.render('S', True, RED)
        WIN.blit(S1, ( int(185* SIZE), int(10* SIZE)))
    if pazaakGame.P2stillPlaying == 0:
        S2 = font.render('S', True, RED)
        WIN.blit(S2, ( int(700* SIZE), int(10* SIZE)))

    if pazaakGame.mctsVersion == "Vanilla":
        img = font.render('Human', True, BLUEISH)
        WIN.blit(img, (int(63* SIZE), int(10* SIZE)))

        img2 = font.render('MCTS', True, BLUEISH)
        WIN.blit(img2, (int(732* SIZE), int(10* SIZE)))

    elif pazaakGame.mctsVersion == "VanillaP2":
        img = font.render('MCTS', True, BLUEISH)
        WIN.blit(img, (int(63* SIZE), int(10* SIZE)))
    
        img2 = font.render('Human', True, BLUEISH)
        WIN.blit(img2, (int(732* SIZE), int(10* SIZE)))

    elif pazaakGame.mctsVersion == "no UCB":
        img = font.render('Human', True, BLUEISH)
        WIN.blit(img, (int(63* SIZE), int(10* SIZE)))

        img2 = font.render('No UCB', True, BLUEISH)
        WIN.blit(img2, (int(732* SIZE), int(10* SIZE)))

    elif pazaakGame.mctsVersion == "no UCBP2":
        img = font.render('No UCB', True, BLUEISH)
        WIN.blit(img, (int(63* SIZE), int(10* SIZE)))

        img2 = font.render('Human', True, BLUEISH)
        WIN.blit(img2, (int(732* SIZE), int(10* SIZE)))

    elif pazaakGame.mctsVersion == "Open Loop":
        img = font.render('Human', True, BLUEISH)
        WIN.blit(img, (int(63* SIZE), int(10* SIZE)))

        img2 = font.render('Open Loop', True, BLUEISH)
        WIN.blit(img2, (int(704* SIZE), int(10* SIZE)))

    elif pazaakGame.mctsVersion == "Open LoopP2":
        img = font.render('Open Loop', True, BLUEISH)
        WIN.blit(img, (int(63* SIZE), int(10* SIZE)))

        img2 = font.render('Human', True, BLUEISH)
        WIN.blit(img2, (int(732* SIZE), int(10* SIZE)))
    else:
        img = font.render('Player 1', True, BLUEISH)
        WIN.blit(img, (int(63* SIZE), int(10* SIZE)))

        img2 = font.render('Player 2', True, BLUEISH)
        WIN.blit(img2, (int(732* SIZE), int(10* SIZE)))

    img1 = font.render(str(pazaakGame.P1setVal), True, BLUEISH)
    WIN.blit(img1, (int(400* SIZE), int(10* SIZE)))

    img2_1 = font.render(str(pazaakGame.P2setVal), True, BLUEISH)
    WIN.blit(img2_1, (int(465* SIZE), int(10* SIZE)))

    radius = int(10* SIZE)
    i = 0
    while i < pazaakGame.P1gamesWon:
        pygame.draw.circle(WIN, RED, P1_CIRCLES[i], radius)
        i += 1

    i = 0
    while i < pazaakGame.P2gamesWon:
        pygame.draw.circle(WIN, RED, P2_CIRCLES[i], radius)
        i += 1
    
    if pazaakGame.player == 1:
        pygame.draw.circle(WIN, GREEN, Pturn[0], radius)
    else:
        pygame.draw.circle(WIN, GREEN, Pturn[1], radius)

    
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

    i = 0
    while i < len(pazaakGame.P1boardCards):
        card = get_card(pazaakGame.P1boardCards[i])
        WIN.blit(card, (P1_BOARD_DIS[i]))
        i += 1
    i = 0
    print(len(pazaakGame.P2boardCards))
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
    pygame.display.update()
    return None