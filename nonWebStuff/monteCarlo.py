from my_pazaak import *

class RootKids:
    def __init__(self, pazaakGame: PazaakState, move: int) -> None :
        self.move = move
        self.state = pazaakGame
        self.wins = 0
        self.games = 0

def monte_carlo_algorithm(pazaakGame: PazaakState) -> int:
    print("monteCarloAlgo", pazaakGame.player)
    kidsList: List[RootKids] = expansion(pazaakGame)
    kidsListREF: List[RootKids] = expansion(pazaakGame)

    kid: RootKids = RootKids(pazaakGame, 0)
    i: int = 0
    j: int = 0
    while i < 10000:
    #print("p2stillplaying: ", kidsList[1].state.P2stillPlaying, kidsList[1].move)
        j = 0
        for kidy in kidsList:
            #print(kidy.state.P1setVal, kidy.state.P1stillPlaying, kidy.state.P2setVal, kidy.state.P2stillPlaying)
            #print("player:", kidy.state.player)
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
    #print(kidsList[0].move, kidsList[0].wins / kidsList[0].games, kidsList[0].state.P1setVal, kidsList[0].state.P2setVal)
    #print(kidsList[1].move, kidsList[1].wins / kidsList[1].games, kidsList[1].state.P1setVal, kidsList[1].state.P2setVal)

    return 0

def doMove(pazaakGame: PazaakState, move: int) -> PazaakState:
    #print(move)
    childState: PazaakState = pazaakGame.makeChild()
# -------------------------------------------#
    if move == -10:
        childState.P2setVal += -5
        childState.P2stillPlaying = 0
        #return childState
        
    elif move == -9: 
        childState.P2setVal += -4
        childState.P2stillPlaying = 0
        #return childState
        
    elif move == -8:
        childState.P2setVal += -3
        childState.P2stillPlaying = 0
        #return childState
        
    elif move == -7:
        childState.P2setVal += -2
        childState.P2stillPlaying = 0
        #return childState
        
    elif move == -6:
        childState.P2setVal += -1
        childState.P2stillPlaying = 0
        #return childState
        
# -------------------------------------------#
    elif move == -5:
        childState.P2setVal += -5
        #return childState

    elif move == -4:
        childState.P2setVal += -4
        #return childState

    elif move == -3:
        childState.P2setVal += -3
        #return childState

    elif move == -2:
        childState.P2setVal += -2
        #return childState

    elif move == -1: 
        childState.P2setVal += -1
        #return childState

# -------------------------------------------#
    elif move == 1: 
        childState.P2setVal += 1
        #return childState

    elif move == 2:
        childState.P2setVal += 2
        #return childState

    elif move == 3:
        childState.P2setVal += 3
        #return childState

    elif move == 4:
        childState.P2setVal += 4
        #return childState

    elif move == 5:
        childState.P2setVal += 5
        #return childState

# -------------------------------------------#
    elif move == 6: 
        childState.P2setVal += 1
        childState.P2stillPlaying = 0
        #return childState
         
    elif move == 7:
        childState.P2setVal += 2
        childState.P2stillPlaying = 0
        #return childState
        
    elif move == 8:
        childState.P2setVal += 3
        childState.P2stillPlaying = 0
        #return childState
        
    elif move == 9:
        childState.P2setVal += 4
        childState.P2stillPlaying = 0
        #return childState
        
    elif move == 10:
        childState.P2setVal += 5
        childState.P2stillPlaying = 0
        #return childState
        

# -------------------------------------------#
    elif move == 11: 
        pass
        #return childState
    elif move == 12:
        childState.P2stillPlaying = 0
        #return childState
    #print(childState.player)
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
    #print("in smart stop func")

    returnVal: int = 1
    if child.state.player == 1:
        if (child.state.P1setVal >= 18) or ((child.state.P1setVal > child.state.P2setVal) and (child.state.P2stillPlaying == 0)):
            child.state.P1stillPlaying = 0
            if child.state.P2stillPlaying == 0: returnVal = 0

        '''
        if child.state.P1setVal >= 18 or ((child.state.P2setVal < child.state.P1setVal) and (child.state.P2stillPlaying == 0)):
            child.state.P1stillPlaying = 0
            #print("1 ", child.state.P1setVal, child.state.P2setVal)
            returnVal = 0
            #print("smartStop")
        '''
    elif child.state.player == 2:
        if (child.state.P2setVal >= 18) or ((child.state.P2setVal > child.state.P1setVal) and (child.state.P1stillPlaying == 0)):
            child.state.P2stillPlaying = 0
            #returnVal = 0
            if child.state.P1stillPlaying == 0: returnVal = 0
        '''
        if child.state.P2setVal >= 18 or ((child.state.P1setVal < child.state.P2setVal) and (child.state.P1stillPlaying == 0)):
            child.state.P2stillPlaying = 0
            #print("2, ", child.state.P1setVal, child.state.P2setVal)
            returnVal = 0
        '''
    '''
    if child.move == 12:
        print("player1 stats: ", child.state.P1stillPlaying, child.state.P1setVal)
        print("player2 stats: ", child.state.P2stillPlaying, child.state.P2setVal)

        print(returnVal)
    
        pygame.quit()
        exit()
    '''
    #print(child.state.P1setVal, child.state.P2setVal, "move:", child.move)



    #time.sleep(5)
    return returnVal

# function to expand the root node and return a list of kids
def expansion(pazaakGame: PazaakState) -> List[RootKids]:
    #print("expand")
    adder: int = 0
    childs: List[RootKids] = []

    #pstate = doMove(pazaakGame, 12)
    #print(pstate.P2stillPlaying)

    #pygame.quit()
    #exit()


    childs.append(RootKids(doMove(pazaakGame, 11), 11))
    childs.append(RootKids(doMove(pazaakGame, 12), 12))
    #print(childs[0].state.P2stillPlaying)

    #print(childs[1].state.P2stillPlaying)
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
        #print(card)
    #for kid in childs:
    #    print(kid.state.P2setVal)
    return childs

# function to simulate children and return 
def simulation(child: RootKids) -> RootKids:
    #print("simulate")
    nextCard: int = 0
    while child.state.P1stillPlaying == 1 or child.state.P2stillPlaying == 1:

        if (child.state.P2setVal > 20) or (child.state.P1setVal > 20):
            #print(child.state.P1setVal, child.state.P2setVal, "move:", child.move)

            temp = child.state.whoWon()

            #print("p1 still playing", child.state.P1stillPlaying, "setVal", child.state.P1setVal)
            #print("p2 still playing", child.state.P2stillPlaying, "setVal", child.state.P2setVal)
            #print("broken2!", temp)
            break

        if child.state.player == 1 and child.state.P2stillPlaying == 1:
            child.state.player = 2
        elif child.state.player == 2 and child.state.P1stillPlaying == 1:
            child.state.player = 1
        


        nextCard = child.state.nextCard()
        #print(child.state.P1stillPlaying, child.state.P2stillPlaying)
        #pygame.quit()
        #exit()
        if child.state.player == 1 and child.state.P1stillPlaying == 1:
            child.state.P1setVal += nextCard
        elif child.state.player == 2 and child.state.P2stillPlaying == 1:
            #print("what the f")
            child.state.P2setVal += nextCard


        if smartStop(child) == 0:
            temp = child.state.whoWon()

            #if temp == 2:
            #    print(child.state.P1setVal, child.state.P2setVal)
            #print("p1 still playing", child.state.P1stillPlaying, "setVal", child.state.P1setVal)
            #print("p2 still playing", child.state.P2stillPlaying, "setVal", child.state.P2setVal)
            #print("broken!", temp)
            break
        



        #print(child.state.player)

        #print(nextCard, child.state.P1setVal, child.state.P2setVal)



    #print(child.state.whoWon())
    return child

def backpropagation(child: RootKids) -> RootKids:
    #print("backpropagate")
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
