'''
Monte Carlo Tree Search Algorithm for Pazaak game. 

The purpose of this code is to give the Pazaak game an A.I. that uses simulations to predit what the next best move is. 
The functions in this algorithm include Selection, Expansion, Simulation, and Backpropagation.
'''
from my_pazaak import *

# This class is used for the children of the game states in order to keep track of the move made, the state, number of wins, and number of games.
class RootKids:
    def __init__(self, pazaakGame: PazaakState, move: int) -> None :
        self.move = move
        self.state = pazaakGame
        self.wins = 0
        self.games = 0

# This algorithm is the main Tree Search function containing Selection, Expansion, Simulation, and Backpropagation.
def monte_carlo_algorithm(pazaakGame: PazaakState) -> int:
    print("monteCarloAlgo", pazaakGame.player)
    kidsList: List[RootKids] = expansion(pazaakGame)
    kidsListREF: List[RootKids] = expansion(pazaakGame)

    kid: RootKids = RootKids(pazaakGame, 0)
    i: int = 0
    j: int = 0
    while i < 10000:
        j = 0
        for kidy in kidsList:
            kid = simulation(kidy)
            kid = backpropagation(kid)
            kidy.state.P1setVal = pazaakGame.P1setVal
            kidy.state.P2setVal = kidsListREF[j].state.P2setVal
            kidy.state.P1stillPlaying = pazaakGame.P1stillPlaying
            kidy.state.P2stillPlaying = kidsListREF[j].state.P2stillPlaying
            #if kidy.state.P2stillPlaying == 1:
            #    pygame.quit()
            #    exit()
            kidy.state.player = pazaakGame.player
            j += 1
        i += 1
    
    for kidy in kidsList: 
        print(kidy.games, kidy.wins)
        print(kidy.move, kidy.wins, kid.games, float(kidy.wins / kidy.games), kidy.state.P1setVal, kidy.state.P2setVal)
    return 0

# This function performs the given A.I. move in a child state and returns the new child state. 
def doMove(pazaakGame: PazaakState, move: int) -> PazaakState:
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

def smartStop(child: RootKids) -> int:
    returnVal: int = 1
    if child.state.player == 1:
        if (child.state.P1setVal >= 18) or ((child.state.P1setVal > child.state.P2setVal) and (child.state.P2stillPlaying == 0)):
            child.state.P1stillPlaying = 0
            if child.state.P2stillPlaying == 0: returnVal = 0
    elif child.state.player == 2:
        if (child.state.P2setVal >= 18) or ((child.state.P2setVal > child.state.P1setVal) and (child.state.P1stillPlaying == 0)):
            child.state.P2stillPlaying = 0
            if child.state.P1stillPlaying == 0: returnVal = 0
    return returnVal

# function to expand the root node and return a list of kids
def expansion(pazaakGame: PazaakState) -> List[RootKids]:
    adder: int = 0
    childs: List[RootKids] = []
    childs.append(RootKids(doMove(pazaakGame, 11), 11))
    childs.append(RootKids(doMove(pazaakGame, 12), 12))
    for card in pazaakGame.P2sideCards:
        if pazaakGame.P2setVal >= 13:
            if card[0] < 0:
                if pazaakGame.P2setVal > 20:
                    adder = -5
                    childs.append(RootKids(doMove(pazaakGame, card[0]), card[0]))
                    childs.append(RootKids(doMove(pazaakGame, card[0]+adder), card[0]+adder))
            else:
                adder = +5
                childs.append(RootKids(doMove(pazaakGame, card[0]), card[0]))
                childs.append(RootKids(doMove(pazaakGame, card[0]+adder), card[0]+adder))
            if card[0] == card[1]:
                continue
            if pazaakGame.P2setVal > 20:
                childs.append(RootKids(doMove(pazaakGame, card[1]), card[1]))
                childs.append(RootKids(doMove(pazaakGame, card[1]-5), card[1]-5))
    return childs

# function to simulate children and return 
def simulation(child: RootKids) -> RootKids:
    nextCard: int = 0
    while child.state.P1stillPlaying == 1 or child.state.P2stillPlaying == 1:
        if (child.state.P2setVal > 20) or (child.state.P1setVal > 20):
            temp = child.state.whoWon()
            break
        if child.state.player == 1 and child.state.P2stillPlaying == 1:
            child.state.player = 2
        elif child.state.player == 2 and child.state.P1stillPlaying == 1:
            child.state.player = 1
        nextCard = child.state.nextCard()
        if child.state.player == 1 and child.state.P1stillPlaying == 1:
            child.state.P1setVal += nextCard
        elif child.state.player == 2 and child.state.P2stillPlaying == 1:
            child.state.P2setVal += nextCard
        if smartStop(child) == 0:
            temp = child.state.whoWon()
            break
    return child

def backpropagation(child: RootKids) -> RootKids:
    winner: int = 0
    winner = child.state.whoWon()
    if winner == 2:
        child.wins += 1
    child.games += 1
    return child

def main():
    pGame: PazaakState = PazaakState(2)
    pGame.P1setVal = 16
    pGame.P2setVal = 18
    pGame.P2sideCards = [[1, 1], [2, 2], [3, 3], [4, 4]]

    monte_carlo_algorithm(pGame)
    return 0

if __name__ == "__main__":
    main()
