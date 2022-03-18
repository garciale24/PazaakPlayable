'''
This file contains the code for the Pazaak game node States
'''

''' Stuff to import '''
import random
from typing import Callable, List

''' This class State is used for the nodes that are created within the MCTS implementations of this project '''
class PazaakState:
    def __init__(self, player: int) -> None:

        # Tally of games won
        self.P1gamesWon: int = 0
        self.P2gamesWon: int = 0

        # MCTS version being used
        self.mctsVersion: str = ""

        # Flag to check which players turn it is during a specific state
        self.player: int = player

        # Flags to check if player 1 and player 2 are still playing
        self.P1stillPlaying: int = 1
        self.P2stillPlaying: int = 1

        # Board Cards
        self.P1boardCards: list[int] = []
        self.P2boardCards: list[int] = []

        # Side Cards
        self.P1sideCards: list[list[int]] = []
        self.P2sideCards: list[list[int]] = []

        # Generate a side deck
        self.createSideDeck: Callable[[list[list[int]]], PazaakState] = \
            lambda sideDeck: PazaakState._side_card_pop(sideDeck)

        # Board values for both players
        self.P1setVal: int = 0
        self.P2setVal: int = 0

        # Used to select side cards
        self.P2pop: int = -1
        self.P1pop: int = -1

        # Check who won the game
        self.util: Callable[[int, int], PazaakState] = \
            lambda: PazaakState._get_utility(self.P1stillPlaying, self.P2stillPlaying)
        self.whoWon: Callable[[], PazaakState] = \
            lambda: PazaakState._check_win(PazaakState._get_utility\
                (self.P1stillPlaying, self.P2stillPlaying), self.P1setVal, self.P2setVal)

        # Generate new card
        self.nextCard: Callable[[], PazaakState] = \
            lambda: PazaakState._next_card()

    ''' Class method to create a child/copy state from the current state '''
    def makeChild(self) -> "PazaakState":
        new_state: PazaakState = PazaakState(2)
        new_state.mctsVersion = self.mctsVersion
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

    ''' Class method to reset the current states variables '''
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

    ''' Static class method to populate a side deck '''
    @staticmethod
    def _side_card_pop(sideCards: List[int]) -> None:
        i: int = 0
        randint: int = 0
        while i < 4:
            randint = 0
            while randint == 0: randint = random.randrange(-5, 5) 
            if randint != 0 : sideCards.append([randint, randint])
            i += 1
        return None

    ''' Static class method to generate a new card '''
    @staticmethod
    def _next_card() -> int: return random.randrange(1, 10)

    ''' Static class method to create a utility value based on which players are still playing at a specific state '''
    @staticmethod
    def _get_utility(p1sp: int, p2sp: int) -> int:
        if p1sp == 1 and p2sp == 1: return 0
        elif p1sp == 0 and p2sp == 1: return 2
        elif p1sp == 1 and p2sp == 0: return 1    
        return 3

    ''' Static class method to check who won based off a utility value '''
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
        elif util == 2:
            if p2sv > 20: return 1
            if p1sv > 20: return 2  
        return 0

''' Function for the Simple AI to play a side card (player 2) '''
def player2_playSideCard(pazaakGame: PazaakState, i: int, j: int) -> int:
    val: int = 0
    val = pazaakGame.P2sideCards[i][j] + pazaakGame.P2setVal
    if val >= 18 and val <= 20:
        if val > pazaakGame.P2setVal or pazaakGame.P2setVal > 20:
            pazaakGame.P2setValTemp = val
            return 1
    return 0

''' Function for the Simple AI to play a side card (player 1) '''
def player1_playSideCard(pazaakGame: PazaakState, i: int, j: int) -> int:
    val: int = 0
    val = pazaakGame.P1sideCards[i][j] + pazaakGame.P1setVal
    if val >= 18 and val <= 20:
        if val > pazaakGame.P1setVal or pazaakGame.P1setVal > 20:
            pazaakGame.P1setValTemp = val
            return 1
    return 0