'''
Monte Carlo Tree Search Algorithm for Pazaak game. 

The purpose of this code is to give the Pazaak game an A.I. that uses simulations to predit what the next best move is. 
The functions in this algorithm include Selection, Expansion, Simulation, and Backpropagation.
'''
from hashlib import new
from lib2to3.pgen2 import pgen
import math
import re
from traceback import print_tb
from turtle import back
from my_pazaak import *

# This class is used for the children of the game states in order to keep track of the move made, the state, number of wins, and number of games.
class RootKids:
    def __init__(self, pazaakGame: PazaakState, move: int, parenty: "RootKids") -> None :
        self.move: int = move
        self.state: PazaakState = pazaakGame
        self.wins: int = 0
        self.games: int = 0
        self.parent: RootKids = parenty
        self.expansions: List[RootKids] = None

# This algorithm is the main Tree Search function containing Selection, Expansion, Simulation, and Backpropagation.
def monte_carlo_algorithm(pazaakGame: PazaakState) -> PazaakState:

    ''' Pre-MCTS stuff '''
    #print("monteCarloAlgo", pazaakGame.player)
    #prevTempList: List[RootKids] = []
    prevSelect: List[int] = []
    currSelect: List[int] = []
    newCurrSelect: List[int] = []
    gameRoot: RootKids = RootKids(pazaakGame, 0, None)

    kidsList: List[RootKids] = []
    if pazaakGame.player == 2:
        kidsList= getKidsP2(gameRoot)
    else: 
        kidsList = getKidsP1(gameRoot)
    #print(kidsList)
    #print(kidsList[7].state.P2pop, "debuggerman", kidsList[7].move)
    #print(len(kidsList))
    gameRoot.expansions = kidsList
    #print(gameRoot.expansions[7].state.P2pop, "debuggerman2", gameRoot.expansions[7].move)
    #for kid in gameRoot.expansions: print("kid:","kid in kidslist moves:", kid.move, kid.state.P1setVal, kid.state.P2setVal)
    
    kidy: int = 0
    i: int = 0
    breakCond: bool = True
    breakCond2: bool = True
    breakCond3: bool = True

    tempList: List[RootKids] = []
    ''' End of Pre-MCTS stuff '''

    while i < 1000:
        breakCond = True
    
        '''
        #### ----- This is to test the selection functionality of the mcts... ----- ####
        gameRoot.expansions[0].wins+=66
        gameRoot.expansions[0].games+=101

        child = gameRoot.expansions[0].state.makeChild()
        childy = RootKids(child, gameRoot.expansions[0].move, gameRoot.expansions[0])

        childy.wins+=30
        childy.games+=50
        gameRoot.expansions[0].expansions = [childy]

        child2 = gameRoot.expansions[0].state.makeChild()
        childy2 = RootKids(child2, gameRoot.expansions[0].move, gameRoot.expansions[0])

        childy2.wins+=35
        childy2.games+=50
        gameRoot.expansions[0].expansions.append(childy2)

        gameRoot.expansions[1].wins+=0
        gameRoot.expansions[1].games+=50
        gameRoot.games+=151

        print(gameRoot.expansions[0].wins, gameRoot.expansions[0].games)

        #### ----- The previous was to test the selection functionality of the mcts (looking good) ----- ####
        '''

        ''' Selection '''
        tempList = gameRoot.expansions
        currSelect = []
        while (breakCond):
            kidy = selection(tempList)
            #kidy = 1
            currSelect.append(kidy)

            if tempList[kidy].expansions != None: 
                tempList = tempList[kidy].expansions
            else:
                breakCond = False
        ''' End of Selection '''


        ''' Expansion '''
        if ((tempList[kidy].state.P1stillPlaying == 1) or (tempList[kidy].state.P2stillPlaying == 1)):
            #print("Expansion Here", tempList[kidy].state.P1setVal, tempList[kidy].state.P2setVal)
            tempList[kidy].expansions = expansion(tempList[kidy])
            ''' End of Expansion '''
            #print("yo:", tempList[kidy].expansions[0].state.player)

            ''' Simulation After Expansion '''
            #if tempList[kidy].expansions != None:


            for expand in range(0, len(tempList[kidy].expansions)):
                simWinner = simulation(tempList[kidy].expansions[expand])
                ''' End of Simulation After Expansion '''

                ''' Backpropagation After Expansion '''
                backpropagation(simWinner, tempList[kidy].expansions[expand], gameRoot.state.player, 1)
                ''' End of Backpropagation After Expansion '''
            #else:
                #print("No Expansion Here")
                #exit(0)
                ''' Simulation After No Expansion '''
                #simWinner = simulation(tempList[kidy])
                ''' End of Simulation After No Expansion '''

                ''' Backpropagation After No Expansion '''
                #backpropagation(simWinner, tempList[kidy], gameRoot.state.player)
                ''' End of Backpropagation After No Expansion '''
        else:
            #print("heh", tempList[kidy].state.P1setVal, tempList[kidy].state.P2setVal, tempList[kidy].state.whoWon())
            pass
            ''' Prune Terminal States '''
            #county = 0
            #while county < 1:
            winner = tempList[kidy].state.whoWon()
            #print("WINNEERRR:", winner)
            mul: int = 650
            #if gameRoot.state.player == 2:
            #    if (gameRoot.state.P2setVal - gameRoot.state.P1setVal) >= 7:
            #        mul = 100 #gameRoot.state.P1setVal*3
            #elif gameRoot.state.player == 1:
            #    mul = gameRoot.state.P1setVal*1
            backpropagation(winner, tempList[kidy], gameRoot.state.player, mul)
                #county += 1
        i+=1

    win = [0, 0, 0, 0]    
    win2 = [0, 0, 0, 0]
    #print(len(gameRoot.expansions), gameRoot.expansions)
    for kidy in gameRoot.expansions: 
        #print(kidy.games, kidy.wins, kidy.move, kidy.state.P1setVal, kidy.state.P2setVal)
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

    #win2[0] = gameRoot.expansions[0].wins/gameRoot.expansions[0].games
    #win2[1] = gameRoot.expansions[0].games
    #win2[2] = gameRoot.expansions[0].wins
    #win2[3] = gameRoot.expansions[0].move
        #print(kidy.move, kidy.wins, kid.games, float(kidy.wins / kidy.games), kidy.state.P1setVal, kidy.state.P2setVal)
    #print(win)
    #print(win2)
    #print(gameRoot.games)
    returnState: PazaakState = None
    for exp in gameRoot.expansions:
        #print(exp.state.P2pop, "lkk")

        if exp.move == win[3]:
            #print(exp.state.P2pop)
            returnState = exp.state
            #print("move:", win[3], returnState.P1setVal, returnState.P2setVal)
            #print(exp.state.P2pop, "hereeeeebrooo")

    #print("premove Stats:", gameRoot.state.P2boardCards, len(gameRoot.state.P2boardCards))
    if returnState == None:
        returnState = gameRoot.state
        returnState.P2pop = -1

    #print(returnState.P2boardCards, len(returnState.P2boardCards), "hehe", returnState.P2pop)
    return returnState

''' Selection Function for MCTS '''
def selection(kidsList: List[RootKids]) -> int:
    selected: int = -1
    kidWinsPer: float = 0.0
    bestUCB: float = 0.0
    kidUCB: float = 0.0
    UCBbias: float = 1.1
    zeros: List[int] = []
    for kid in range(len(kidsList)):
        if ((kidsList[kid].games != 0) and (kidsList[kid].parent.games) != 0):
            kidWinsPer = (kidsList[kid].wins / kidsList[kid].games)
            kidUCB = kidWinsPer + UCBbias * \
                math.sqrt((2*math.log(kidsList[kid].parent.games)) / (kidsList[kid].games))
            if bestUCB < kidUCB:
                bestUCB = kidUCB
                selected = kid
        else:
            zeros.append(kid)
            
    # Random Selection
    if (selected == -1):
        selected = random.randrange(0, len(kidsList))
    elif ((selected > -1) and (len(zeros) > 0)):
        selected = zeros[random.randrange(0, len(zeros))]
    return selected
''' End of Selection Function for MCTS '''


''' Aye bro honestly fix the fuck out of the expansion. That is where a lot of the work is going to be.'''

''' Aye bro for the exapnasion, keep in mind that player 2 is going first in this order. A.I. has a turn and then the human player has a turn'''

''' Expansion Function for MCTS '''
def expansion(child: RootKids) -> List[RootKids]:
    expand: List[RootKids] = None
    playerToBe: int = child.state.player

    if child.state.player == 1:
        if child.state.P2stillPlaying == 1:
            playerToBe = 2
    elif child.state.player == 2:
        if child.state.P1stillPlaying == 1:
            playerToBe = 1

    #print("----------------------------------------------")
    #print("PlayerToBe:", playerToBe)
    #print("child.state.P1stillPlaying:", child.state.P1stillPlaying)
    #print("----------------------------------------------")


    if playerToBe == 1 and child.state.P1stillPlaying == 1:
        for i in range(1, 11):
            newState = child.state.makeChild()
            newState.P1setVal += i
            if newState.P1setVal >= 20:
                newState.P1stillPlaying = 0
            newState.player = playerToBe
            newKid = RootKids(newState, child.move, child)
            if expand == None: 
                if smartStop(newKid.state) == 0:
                    temp = newKid.state.whoWon()
                    #print("win1:",temp, newKid.move)
                #if child.state.P1stillPlaying == 0:
                #    newKid.state.P1stillPlaying = 0
                expand = [newKid]
            else: 
                if smartStop(newKid.state) == 0:
                    temp = newKid.state.whoWon()
                    #print("win2:",temp, newKid.move)
                #if child.state.P1stillPlaying == 0:
                #    newKid.state.P1stillPlaying = 0
                expand.append(newKid)
            #print("hereere:", newKid.state.P1setVal, newKid.state.P2setVal, newKid.state.whoWon())

    elif playerToBe == 2 and child.state.P2stillPlaying == 1:
        for i in range(1, 11):
            newState = child.state.makeChild()
            newState.P2setVal += i
            if newState.P2setVal >= 20:
                newState.P2stillPlaying = 0
            newState.player = playerToBe
            newKid = RootKids(newState, child.move, child)
            if expand == None: 
                if smartStop(newKid.state) == 0:
                    temp = newKid.state.whoWon()
                    #print("win1:",temp, newKid.move)
                #if child.state.P2stillPlaying == 0:
                #    newKid.state.P2stillPlaying = 0
                expand = [newKid]
            else: 
                if smartStop(newKid.state) == 0:
                    temp = newKid.state.whoWon()
                    #print("win2:",temp, newKid.move)
                #if child.state.P2stillPlaying == 0:
                #    newKid.state.P2stillPlaying = 0
                expand.append(newKid)
    return expand
''' End of Expansion Function for MCTS '''


# This function performs the given A.I. move in a child state and returns the new child state. 
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

def smartStop(child: PazaakState) -> int:
    returnVal: int = 1
    if child.player == 1:
        #print(child.P1setVal, child.P2setVal, child.P2stillPlaying)
        if ((child.P1setVal >= 18) and (child.P2setVal <= child.P1setVal)) or ((child.P1setVal >= child.P2setVal) and (child.P2stillPlaying == 0)):
            child.P1stillPlaying = 0
            #print("sanity check")
            if child.P2stillPlaying == 0: 
                returnVal = 0
                #print("smartStop", child.P1setVal, child.P2setVal, child.P1stillPlaying, child.P2stillPlaying)
    elif child.player == 2:
        if ((child.P2setVal >= 18) and (child.P1setVal <= child.P2setVal)) or ((child.P2setVal >= child.P1setVal) and (child.P1stillPlaying == 0)):
            child.P2stillPlaying = 0
            if child.P1stillPlaying == 0: returnVal = 0
    return returnVal

# function to expand the root node and return a list of kids
def getKidsP2(pazaak: RootKids) -> List[RootKids]:
    pazaakGame: PazaakState = pazaak.state
    adder: int = 0
    childs: List[RootKids] = []
    childs.append(RootKids(doMoveP2(pazaakGame, 11), 11, pazaak))
    if pazaak.state.P2setVal > 10: childs.append(RootKids(doMoveP2(pazaakGame, 12), 12, pazaak))

    rem: list[list[int]] = []
    if pazaak.move == 0:        
        #sideCards = pazaakGame.P2sideCards.copy()
        cty: int = -1

        for card in pazaakGame.P2sideCards:
            cty += 1
            rem = []
            sideCards = pazaakGame.P2sideCards.copy()
            #print(sideCards, "yeet", card)

            #rem = sideCards.remove(card)
            cardTemp = card.copy()
            for x in sideCards:
                if x == cardTemp:
                    cardTemp = None
                else:
                    rem.append(x)

            #print(rem, "yeet2")

            if card[0] < 0:
                if pazaakGame.P2setVal >= 20:
                    adder = -5
                    #pazaakGame.P2sideCards.remove(card)
                    childs.append(RootKids(doMoveP2(pazaakGame, card[0]), card[0], pazaak))
                    childs[-1].state.P2sideCards = rem
                    childs[-1].state.P2pop = cty
                    #childs[-1].state.P2boardCards.append(card[0])
                    childs.append(RootKids(doMoveP2(pazaakGame, card[0]+adder), card[0]+adder, pazaak))
                    childs[-1].state.P2sideCards = rem
                    childs[-1].state.P2pop = cty
                    #childs[-1].state.P2boardCards.append(card[0])

                    #childs[-1].state.P2sideCards.remove(card) 
                    #childs[-2].state.P2sideCards.remove(card)
            else:
                if pazaakGame.P2setVal >= 10:
                    adder = +5
                    #pazaakGame.P2sideCards.remove(card)
                    childs.append(RootKids(doMoveP2(pazaakGame, card[0]), card[0], pazaak))
                    childs[-1].state.P2sideCards = rem
                    childs[-1].state.P2pop = cty
                    #childs[-1].state.P2boardCards.append(card[0])

                    childs.append(RootKids(doMoveP2(pazaakGame, card[0]+adder), card[0]+adder, pazaak))
                    childs[-1].state.P2sideCards = rem
                    childs[-1].state.P2pop = cty
                    #childs[-1].state.P2boardCards.append(card[0])

                    #childs[-1].state.P2sideCards.remove(card) 
                    #childs[-2].state.P2sideCards.remove(card)
    return childs

def getKidsP1(pazaak: RootKids) -> List[RootKids]:
    pazaakGame: PazaakState = pazaak.state
    adder: int = 0
    childs: List[RootKids] = []
    childs.append(RootKids(doMoveP1(pazaakGame, 11), 11, pazaak))
    if pazaak.state.P1setVal > 10: childs.append(RootKids(doMoveP1(pazaakGame, 12), 12, pazaak))

    rem: list[list[int]] = []
    if pazaak.move == 0:        
        #sideCards = pazaakGame.P2sideCards.copy()
        cty: int = -1

        for card in pazaakGame.P1sideCards:
            cty += 1
            rem = []
            sideCards = pazaakGame.P1sideCards.copy()
            #print(sideCards, "yeet", card)

            #rem = sideCards.remove(card)
            cardTemp = card.copy()
            for x in sideCards:
                if x == cardTemp:
                    cardTemp = None
                else:
                    rem.append(x)

            #print(rem, "yeet2")

            if card[0] < 0:
                if pazaakGame.P1setVal >= 20:
                    adder = -5
                    #pazaakGame.P2sideCards.remove(card)
                    childs.append(RootKids(doMoveP1(pazaakGame, card[0]), card[0], pazaak))
                    childs[-1].state.P1sideCards = rem
                    childs[-1].state.P1pop = cty
                    #childs[-1].state.P2boardCards.append(card[0])
                    childs.append(RootKids(doMoveP1(pazaakGame, card[0]+adder), card[0]+adder, pazaak))
                    childs[-1].state.P1sideCards = rem
                    childs[-1].state.P1pop = cty
                    #childs[-1].state.P2boardCards.append(card[0])

                    #childs[-1].state.P2sideCards.remove(card) 
                    #childs[-2].state.P2sideCards.remove(card)
            else:
                if pazaakGame.P1setVal >= 10:
                    adder = +5
                    #pazaakGame.P2sideCards.remove(card)
                    childs.append(RootKids(doMoveP1(pazaakGame, card[0]), card[0], pazaak))
                    childs[-1].state.P1sideCards = rem
                    childs[-1].state.P1pop = cty
                    #childs[-1].state.P2boardCards.append(card[0])

                    childs.append(RootKids(doMoveP1(pazaakGame, card[0]+adder), card[0]+adder, pazaak))
                    childs[-1].state.P1sideCards = rem
                    childs[-1].state.P1pop = cty
                    #childs[-1].state.P2boardCards.append(card[0])

                    #childs[-1].state.P2sideCards.remove(card) 
                    #childs[-2].state.P2sideCards.remove(card)
    return childs

''' Simulation Function for MCTS '''
def simulation(rent: RootKids) -> int:
    tempRent: RootKids = RootKids(rent.state.makeChild(), rent.move, rent.parent)
    temp: int = 0
    if tempRent.state.P2stillPlaying == 0 and tempRent.state.P1stillPlaying == 0:
        temp = tempRent.state.whoWon()
    else:
        while tempRent.state.P1stillPlaying == 1 or tempRent.state.P2stillPlaying == 1:
            #print("INFO1:",tempRent.state.P1setVal, tempRent.state.P2setVal, tempRent.state.P1stillPlaying, tempRent.state.P2stillPlaying)

            if (tempRent.state.P2setVal > 20) or (tempRent.state.P1setVal > 20):
                temp = tempRent.state.whoWon()
                break
            if tempRent.state.player == 1 and tempRent.state.P2stillPlaying == 1:
                tempRent.state.player = 2
            elif tempRent.state.player == 2 and tempRent.state.P1stillPlaying == 1:
                tempRent.state.player = 1

            nextCard = tempRent.state.nextCard()
            #print("nextCard:", nextCard)
            if tempRent.state.player == 1 and tempRent.state.P1stillPlaying == 1:
                tempRent.state.P1setVal += nextCard
            if rent.state.player == 1:
                if smartStop(tempRent.state) == 0:
                    #rent.state.P1stillPlaying = 0
                    temp = tempRent.state.whoWon()
                    break

            if tempRent.state.player == 2 and tempRent.state.P2stillPlaying == 1:
                tempRent.state.P2setVal += nextCard
            if rent.state.player == 2:
                if smartStop(tempRent.state) == 0:
                    #rent.state.P2stillPlaying = 0
                    temp = tempRent.state.whoWon()
                    break
            #print("simulation iterations", tempRent.state.P1setVal, tempRent.state.P2setVal)
        #print("INFO2:",tempRent.state.P1setVal, tempRent.state.P2setVal, tempRent.state.P1stillPlaying, tempRent.state.P2stillPlaying, temp)

    return temp
''' End of Simulation Function for MCTS '''

''' Backpropagation Function for MCTS '''
def backpropagation(winner: int, child: RootKids, player: int, multiplier: int) -> None:
    tempy: RootKids = child
    while tempy.parent != None:
        if ((winner == 2 and player == 2) or (winner == 1 and player == 1)): # or winner == -1):
            tempy.wins += 1*multiplier
        if winner == -1:
            tempy.wins += 0.5*multiplier
            #tempy.wins *= 0.85
        tempy.games += 1*multiplier
        tempy = tempy.parent
    tempy.games += 1*multiplier
    return None
''' End Backpropagation Function for MCTS '''

def main():
    pGame: PazaakState = PazaakState(2)
    pGame.P1setVal = 12
    pGame.P2setVal = 17
    pGame.P1stillPlaying = 1
    pGame.P2sideCards = [[1,1], [2,2], [3, 3]] #only positives get loaded into moves list
    pGame = monte_carlo_algorithm(pGame)
    #print(pGame.P1setVal, pGame.P2setVal, pGame.whoWon())
    return 0

if __name__ == "__main__":
    main()
