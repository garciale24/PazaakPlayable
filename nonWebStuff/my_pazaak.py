import random
import time

from typing import Any, Callable, List, Optional, Tuple

import pygame

STAND: str = "stand"
YES: str = "yes"


class PazaakState:
    def __init__(self, player: int) -> None:
        self.ties: int = 0
        self.player: int = player
        self.moves: list[int] = None
        self.selected: int = -1
        self.display: Callable[[], PazaakState] = \
            lambda: PazaakState._display(\
                self.P1setVal, self.P2setVal, self.P1gamesWon, self.P2gamesWon,\
                     self.P1stillPlaying, self.P2stillPlaying, self.P1boardCards,\
                          self.P2boardCards, self.P1sideCards, self.P2sideCards, self.ties)
        self.P1gamesWon: int = 0
        self.P2gamesWon: int = 0
        self.P1stillPlaying: int = 1
        self.P2stillPlaying: int = 1
        self.P1boardCards: list[int] = []
        self.P2boardCards: list[int] = []
        self.P1sideCards: list[list[int]] = []
        self.P2sideCards: list[list[int]] = []
        self.createSideDeck: Callable[[list[list[int]]], PazaakState] = \
            lambda sideDeck: PazaakState._side_card_pop(sideDeck)
        self.P1setVal: int = 0
        self.P2setVal: int = 0
        self.P2setValTemp: int = 0

        self.util: Callable[[int, int], PazaakState] = \
            lambda: PazaakState._get_utility(self.P1stillPlaying, self.P2stillPlaying)
        #self.traverse: Callable[[int], PazaakState] = \
        #    lambda index: PazaakState._performMove(player, index)
        self.whoWon: Callable[[], PazaakState] = \
            lambda: PazaakState._check_win(PazaakState._get_utility\
                (self.P1stillPlaying, self.P2stillPlaying), self.P1setVal, self.P2setVal)
        self.nextCard: Callable[[], PazaakState] = \
            lambda: PazaakState._next_card()

    def makeChild(self) -> "PazaakState":
        new_state: PazaakState = PazaakState(2)
        new_state.player = self.player
        new_state.P1gamesWon = self.P1gamesWon
        new_state.P2gamesWon = self.P2gamesWon
        new_state.P1stillPlaying = self.P1stillPlaying
        new_state.P2stillPlaying = self.P2stillPlaying
        new_state.P1boardCards = self.P1boardCards
        new_state.P2boardCards = self.P2boardCards
        new_state.P1sideCards = self.P1sideCards
        new_state.P2sideCards = self.P2sideCards
        new_state.P1setVal = self.P1setVal
        new_state.P2setVal = self.P2setVal
        return new_state

    def reset(self) -> None:
        self.moves = None
        self.selected = -1
        self.P1stillPlaying = 1
        self.P2stillPlaying = 1
        self.P1boardCards = []
        self.P2boardCards = []
        self.P1setVal = 0
        self.P2setVal = 0
        self.P2setValTemp= 0

        return None

    @staticmethod
    def _side_card_pop(sideCards: List[int]) -> None:
        i: int = 0
        randint: int = 0
        randint2: int = 0
        while i < 4:
            randint = 0
            randint2 = 0
            while randint == 0: randint = random.randrange(-5, 5) 
            while randint2 == 0: randint2 = random.randrange(-10, 10)
            if randint2 == randint and randint != 0: sideCards.append([randint, -1*randint])
            elif randint != 0 and randint != randint2: sideCards.append([randint, randint])
            i += 1
        return None
        
    @staticmethod
    def _display(p1sval: int, p2sval: int, p1gwon: int, p2gwon: int,\
         p1splay: int, p2splay: int, p1bcards: List[int], p2bcards: List[int], p1scards: List[int], p2scards: List[int], ties: int) -> str:
        print("-------DISPLAY-------")
        print("p1set val: ", p1sval)
        print("p2set val: ", p2sval)
        print("p1games won: ", p1gwon)
        print("p2games won: ", p2gwon)
        print("tie games: ", ties)
        print("p1still playing: ", p1splay)
        print("p2still playing: ", p2splay)
        print("p1board cards: ", p1bcards)
        print("p2board cards: ", p2bcards)
        print("p1side cards: ", p1scards, "p12side cards: ", p2scards)
        print("-------DISPLAY-------")
        return ""

    @staticmethod
    def _next_card() -> int:
        return random.randrange(1, 10)

    @staticmethod
    def _performMove(player: int, index: int) -> None:
        return None

    @staticmethod
    def _get_utility(p1sp: int, p2sp: int) -> int:
        if p1sp == 1 and p2sp == 1: return 0
        elif p1sp == 0 and p2sp == 1: return 2
        elif p1sp == 1 and p2sp == 0: return 1    
        return 3

    @staticmethod
    def _check_win(util: int, p1sv: int, p2sv) :
        if util == 3:
            if p2sv > 20: return 1
            if p1sv > 20: return 2
            if p1sv > p2sv: return 1
            if p1sv < p2sv: return 2
            if p1sv == p2sv: return -1
        elif util == 0:
            if p2sv > 20: return 1
            if p1sv > 20: return 2
        elif util == 1:
            if p1sv > 20: return 2
            if p2sv > 20: return 1
            if p1sv > p2sv: return 1   



            #if p1sv < p2sv: return 2
         
        elif util == 2:
            #print("here")
            #pygame.quit()
            #exit()
            if p2sv > 20: return 1
            if p1sv > 20: return 2
            if p1sv < p2sv: return 2


            #if p1sv > p2sv: return 1            

        return 0


def player2_playSideCard(pazaakGame: PazaakState, i: int, j: int) -> int:
    val: int = 0
    print(len(pazaakGame.P2sideCards), i, j)
    val = pazaakGame.P2sideCards[i][j] + pazaakGame.P2setVal
    if val >= 18 and val <= 20:
        if val > pazaakGame.P2setVal or pazaakGame.P2setVal > 20:
            pazaakGame.P2setValTemp = val
            #pazaakGame.P2stillPlaying = 0
            return 1
    return 0





















def player1_human_auto(pazaakGame: PazaakState, nextCard: int) -> None:
    if pazaakGame.P1stillPlaying == 1:
        pazaakGame.P1boardCards.append(nextCard)
        pazaakGame.P1setVal += nextCard
        if pazaakGame.P1setVal >= 18: pazaakGame.P1stillPlaying = 0
    pazaakGame.player = 2 
    return None

def player2_AI_auto(pazaakGame: PazaakState, nextCard: int) -> None:
    i: int = 0
    lencond: int = len(pazaakGame.P2sideCards)
    if pazaakGame.P2stillPlaying == 1:
        pazaakGame.P2boardCards.append(nextCard)
        pazaakGame.P2setVal += nextCard
        if pazaakGame.P2setVal >= 18: pazaakGame.P2stillPlaying = 0
        while i < lencond:
            i += 1
            if player2_playSideCard(pazaakGame, i-1, 0) == 1: break
            if pazaakGame.P2sideCards[i-1][0] == pazaakGame.P2sideCards[i-1][1]: continue
            if player2_playSideCard(pazaakGame, i-1, 1) == 1: break
    pazaakGame.player = 1 
    return None

#def monte_carlo_algorithm(pazaakGame: PazaakState) -> int:
#    return 0


def player1_move(pazaakGame: PazaakState) -> None:
    return None

def player1_human(pazaakGame: PazaakState, nextCard: int) -> None:
    if pazaakGame.P1stillPlaying == 1:
        pazaakGame.P1boardCards.append(nextCard)
        pazaakGame.P1setVal += nextCard
        pazaakGame.display()

        if pazaakGame.P1setVal >= 20: pazaakGame.P1stillPlaying = 0
        else: player1_move(pazaakGame)
    pazaakGame.player = 2 
    return None



def pazaak_main(event: pygame) -> bool:
    j: int = 0
    k: int = 2
    p1wins: int = 0
    p2wins: int = 0
    ties: int = 0
    pazaakGame = PazaakState(k)
    pazaakGame.createSideDeck(pazaakGame.P1sideCards)
    pazaakGame.createSideDeck(pazaakGame.P2sideCards)
    while (p1wins < 3) and (p2wins < 3):

        if k == 1: k = 2
        elif k == 2: k = 1
        pazaakGame.player = k
        endCond: int = 0
        while endCond == 0:

            if event.type == pygame.QUIT:
                return False


            pazaakGame.display()

            nextCard: int = pazaakGame.nextCard()

            if pazaakGame.player == 1: player1_human(pazaakGame, nextCard)
            #elif pazaakGame.player == 2: player2_AI(pazaakGame, nextCard)
            pazaakGame.display()

            endCond = pazaakGame.whoWon()
            if endCond == 1: 
                pazaakGame.P1gamesWon+=1
                p1wins += 1
            elif endCond == 2: 
                pazaakGame.P2gamesWon+=1
                p2wins += 1
            elif endCond == -1: 
                pazaakGame.ties+=1
                ties += 1
        time.sleep(5)
        pazaakGame.reset()
    j += 1
    print("p1wins: ", p1wins)
    print("p2wins: ", p2wins)
    print("ties: ", ties)
    #exit(0)
    return False

#if __name__ == "__main__":
#    main()