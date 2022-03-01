'''
Open Loop Monte Carlo Tree Search Algorithm for Pazaak game. 

The purpose of this code is to give the Pazaak game an A.I. that uses simulations to predit what the next best move is. 
The functions in this algorithm include Selection, Expansion, Simulation, and Backpropagation.
'''

''' Stuff to import '''
from my_pazaak import *

''' This class is used for the children of the game states in order to keep track of the move made, the state, number of wins, and number of games. '''
class RootKids:
    def __init__(self, pazaakGame: PazaakState, move: int, parenty: "RootKids") -> None :
        self.move: int = move
        self.state: PazaakState = pazaakGame
        self.wins: int = 0
        self.games: int = 0
        self.parent: RootKids = parenty
        self.expansions: List[RootKids] = None

''' This algorithm is the main Tree Search function containing Selection, Expansion, Simulation, and Backpropagation. '''
def monte_carlo_algorithmOpenLoop(pazaakGame: PazaakState) -> PazaakState:

    # Pre-MCTS stuff 
    gameRoot: RootKids = RootKids(pazaakGame, 0, None)
    kidsList: List[RootKids] = []
    if pazaakGame.player == 2:
        kidsList= getKidsP2(gameRoot)
    else: 
        kidsList = getKidsP1(gameRoot)
    gameRoot.expansions = kidsList
    kidy: int = 0
    i: int = 0
    tempList: List[RootKids] = []
    # End of Pre-MCTS stuff 

    while i < 1000:

        # Selection 
        tempList = gameRoot.expansions
        for kid in tempList:

            # Simulation
            simWinner = simulation(kid)

            # Backpropagation
            backpropagation(simWinner, kid, gameRoot.state.player, 1)
        i+=1

    # Tally wins/losses for root children
    win = [0, 0, 0, 0]    
    for kidy in gameRoot.expansions: 
        if kidy.games == 0:
            win[0] = 0
            win[1] = 0
            win[2] = 0
            win[3] = kidy.move
        elif kidy.wins/kidy.games > win[0]:
            win[0] = kidy.wins/kidy.games
            win[1] = kidy.games
            win[2] = kidy.wins
            win[3] = kidy.move

    # Load return state with selected child 
    returnState: PazaakState = None
    for exp in gameRoot.expansions:
        if exp.move == win[3]:
            returnState = exp.state

    # Pop side card from side deck if one was used 
    if returnState == None:
        returnState = gameRoot.state
        returnState.P2pop = -1
    return returnState

''' This function performs the given A.I. move in a child state and returns the new child state. '''
def doMoveP2(pazaakGame: PazaakState, move: int) -> PazaakState:
    childState: PazaakState = pazaakGame.makeChild()
# -------------------------------------------#
    if move == -10:
        childState.P2setVal += -5
        childState.P2stillPlaying = 0        
    elif move == -9: 
        childState.P2setVal += -4
        childState.P2stillPlaying = 0        
    elif move == -8:
        childState.P2setVal += -3
        childState.P2stillPlaying = 0        
    elif move == -7:
        childState.P2setVal += -2
        childState.P2stillPlaying = 0        
    elif move == -6:
        childState.P2setVal += -1
        childState.P2stillPlaying = 0        
# -------------------------------------------#
    elif move == -5:
        childState.P2setVal += -5
    elif move == -4:
        childState.P2setVal += -4
    elif move == -3:
        childState.P2setVal += -3
    elif move == -2:
        childState.P2setVal += -2
    elif move == -1: 
        childState.P2setVal += -1
# -------------------------------------------#
    elif move == 1: 
        childState.P2setVal += 1
    elif move == 2:
        childState.P2setVal += 2
    elif move == 3:
        childState.P2setVal += 3
    elif move == 4:
        childState.P2setVal += 4
    elif move == 5:
        childState.P2setVal += 5
# -------------------------------------------#
    elif move == 6: 
        childState.P2setVal += 1
        childState.P2stillPlaying = 0         
    elif move == 7:
        childState.P2setVal += 2
        childState.P2stillPlaying = 0        
    elif move == 8:
        childState.P2setVal += 3
        childState.P2stillPlaying = 0        
    elif move == 9:
        childState.P2setVal += 4
        childState.P2stillPlaying = 0        
    elif move == 10:
        childState.P2setVal += 5
        childState.P2stillPlaying = 0        
# -------------------------------------------#
    elif move == 11: 
        pass
    elif move == 12:
        childState.P2stillPlaying = 0
    if childState.P2setVal >= 20:
        childState.P2stillPlaying = 0
    return childState

''' This function performs the given A.I. move in a child state and returns the new child state. '''
def doMoveP1(pazaakGame: PazaakState, move: int) -> PazaakState:
    childState: PazaakState = pazaakGame.makeChild()
# -------------------------------------------#
    if move == -10:
        childState.P1setVal += -5
        childState.P1stillPlaying = 0        
    elif move == -9: 
        childState.P1setVal += -4
        childState.P1stillPlaying = 0        
    elif move == -8:
        childState.P1setVal += -3
        childState.P1stillPlaying = 0        
    elif move == -7:
        childState.P1setVal += -2
        childState.P1stillPlaying = 0        
    elif move == -6:
        childState.P1setVal += -1
        childState.P1stillPlaying = 0        
# -------------------------------------------#
    elif move == -5:
        childState.P1setVal += -5
    elif move == -4:
        childState.P1setVal += -4
    elif move == -3:
        childState.P1setVal += -3
    elif move == -2:
        childState.P1setVal += -2
    elif move == -1: 
        childState.P1setVal += -1
# -------------------------------------------#
    elif move == 1: 
        childState.P1setVal += 1
    elif move == 2:
        childState.P1setVal += 2
    elif move == 3:
        childState.P1setVal += 3
    elif move == 4:
        childState.P1setVal += 4
    elif move == 5:
        childState.P1setVal += 5
# -------------------------------------------#
    elif move == 6: 
        childState.P1setVal += 1
        childState.P1stillPlaying = 0         
    elif move == 7:
        childState.P1setVal += 2
        childState.P1stillPlaying = 0        
    elif move == 8:
        childState.P1setVal += 3
        childState.P1stillPlaying = 0        
    elif move == 9:
        childState.P1setVal += 4
        childState.P1stillPlaying = 0        
    elif move == 10:
        childState.P1setVal += 5
        childState.P1stillPlaying = 0        
# -------------------------------------------#
    elif move == 11: 
        pass
    elif move == 12:
        childState.P1stillPlaying = 0
    if childState.P1setVal >= 20:
        childState.P1stillPlaying = 0
    return childState

#   Moves List:

#   move:   -10 -> -5 & Stand
#   move:    -9 -> -4 & Stand
#   move:    -8 -> -3 & Stand
#   move:    -7 -> -2 & Stand
#   move:    -6 -> -1 & Stand

#   move:    -5 -> -5 & End Turn
#   move:    -4 -> -4 & End Turn    
#   move:    -3 -> -3 & End Turn
#   move:    -2 -> -2 & End Turn
#   move:    -1 -> -1 & End Turn

#   move:     1 -> +1 & End Turn
#   move:     2 -> +2 & End Turn
#   move:     3 -> +3 & End Turn
#   move:     4 -> +4 & End Turn
#   move:     5 -> +5 & End Turn

#   move:     6 -> +1 & Stand
#   move:     7 -> +2 & Stand
#   move:     8 -> +3 & Stand
#   move:     9 -> +4 & Stand
#   move:    10 -> +5 & Stand

#   move:    11 -> End Turn
#   move:    12 -> Stand

''' Function to stop AI if set value is between 18 to 20 '''
def smartStop(child: PazaakState) -> int:
    returnVal: int = 1
    if child.player == 1:
        if ((child.P1setVal >= 18) and (child.P2setVal <= child.P1setVal)) or ((child.P1setVal >= child.P2setVal) and (child.P2stillPlaying == 0)):
            child.P1stillPlaying = 0
            if child.P2stillPlaying == 0: 
                returnVal = 0
    elif child.player == 2:
        if ((child.P2setVal >= 18) and (child.P1setVal <= child.P2setVal)) or ((child.P2setVal >= child.P1setVal) and (child.P1stillPlaying == 0)):
            child.P2stillPlaying = 0
            if child.P1stillPlaying == 0: returnVal = 0
    return returnVal

''' Function to expand the root node and return a list of kids '''
def getKidsP2(pazaak: RootKids) -> List[RootKids]:
    pazaakGame: PazaakState = pazaak.state
    adder: int = 0
    childs: List[RootKids] = []
    childs.append(RootKids(doMoveP2(pazaakGame, 11), 11, pazaak))
    if pazaak.state.P2setVal > 10: childs.append(RootKids(doMoveP2(pazaakGame, 12), 12, pazaak))

    rem: list[list[int]] = []
    if pazaak.move == 0:        
        cty: int = -1
        for card in pazaakGame.P2sideCards:
            cty += 1
            rem = []
            sideCards = pazaakGame.P2sideCards.copy()
            cardTemp = card.copy()
            for x in sideCards:
                if x == cardTemp:
                    cardTemp = None
                else:
                    rem.append(x)
            if card[0] < 0:
                if pazaakGame.P2setVal >= 20:
                    adder = -5
                    childs.append(RootKids(doMoveP2(pazaakGame, card[0]), card[0], pazaak))
                    childs[-1].state.P2sideCards = rem
                    childs[-1].state.P2pop = cty
                    childs.append(RootKids(doMoveP2(pazaakGame, card[0]+adder), card[0]+adder, pazaak))
                    childs[-1].state.P2sideCards = rem
                    childs[-1].state.P2pop = cty
            else:
                if pazaakGame.P2setVal >= 10:
                    adder = +5
                    childs.append(RootKids(doMoveP2(pazaakGame, card[0]), card[0], pazaak))
                    childs[-1].state.P2sideCards = rem
                    childs[-1].state.P2pop = cty
                    childs.append(RootKids(doMoveP2(pazaakGame, card[0]+adder), card[0]+adder, pazaak))
                    childs[-1].state.P2sideCards = rem
                    childs[-1].state.P2pop = cty
    return childs

''' Function to expand the root node and return a list of kids '''
def getKidsP1(pazaak: RootKids) -> List[RootKids]:
    pazaakGame: PazaakState = pazaak.state
    adder: int = 0
    childs: List[RootKids] = []
    childs.append(RootKids(doMoveP1(pazaakGame, 11), 11, pazaak))
    if pazaak.state.P1setVal > 10: childs.append(RootKids(doMoveP1(pazaakGame, 12), 12, pazaak))

    rem: list[list[int]] = []
    if pazaak.move == 0:        
        cty: int = -1
        for card in pazaakGame.P1sideCards:
            cty += 1
            rem = []
            sideCards = pazaakGame.P1sideCards.copy()
            cardTemp = card.copy()
            for x in sideCards:
                if x == cardTemp:
                    cardTemp = None
                else:
                    rem.append(x)
            if card[0] < 0:
                if pazaakGame.P1setVal >= 20:
                    adder = -5
                    childs.append(RootKids(doMoveP1(pazaakGame, card[0]), card[0], pazaak))
                    childs[-1].state.P1sideCards = rem
                    childs[-1].state.P1pop = cty
                    childs.append(RootKids(doMoveP1(pazaakGame, card[0]+adder), card[0]+adder, pazaak))
                    childs[-1].state.P1sideCards = rem
                    childs[-1].state.P1pop = cty
            else:
                if pazaakGame.P1setVal >= 10:
                    adder = +5
                    childs.append(RootKids(doMoveP1(pazaakGame, card[0]), card[0], pazaak))
                    childs[-1].state.P1sideCards = rem
                    childs[-1].state.P1pop = cty
                    childs.append(RootKids(doMoveP1(pazaakGame, card[0]+adder), card[0]+adder, pazaak))
                    childs[-1].state.P1sideCards = rem
                    childs[-1].state.P1pop = cty
    return childs

''' Simulation Function for MCTS '''
def simulation(rent: RootKids) -> int:
    tempRent: RootKids = RootKids(rent.state.makeChild(), rent.move, rent.parent)
    temp: int = 0
    if tempRent.state.P2stillPlaying == 0 and tempRent.state.P1stillPlaying == 0:
        temp = tempRent.state.whoWon()
    else:
        while tempRent.state.P1stillPlaying == 1 or tempRent.state.P2stillPlaying == 1:
            if (tempRent.state.P2setVal > 20) or (tempRent.state.P1setVal > 20):
                temp = tempRent.state.whoWon()
                break
            if tempRent.state.player == 1 and tempRent.state.P2stillPlaying == 1:
                tempRent.state.player = 2
            elif tempRent.state.player == 2 and tempRent.state.P1stillPlaying == 1:
                tempRent.state.player = 1
            nextCard = tempRent.state.nextCard()
            if tempRent.state.player == 1 and tempRent.state.P1stillPlaying == 1:
                tempRent.state.P1setVal += nextCard
            if rent.state.player == 1:
                if smartStop(tempRent.state) == 0:
                    temp = tempRent.state.whoWon()
                    break
            if tempRent.state.player == 2 and tempRent.state.P2stillPlaying == 1:
                tempRent.state.P2setVal += nextCard
            if rent.state.player == 2:
                if smartStop(tempRent.state) == 0:
                    temp = tempRent.state.whoWon()
                    break
    return temp

''' Backpropagation Function for MCTS '''
def backpropagation(winner: int, child: RootKids, player: int, multiplier: int) -> None:
    tempy: RootKids = child
    if ((winner == 2 and player == 2) or (winner == 1 and player == 1)): # or winner == -1):
        tempy.wins += 1*multiplier
    if winner == -1:
        tempy.wins += 0.5*multiplier
    tempy.games += 1*multiplier
    return None