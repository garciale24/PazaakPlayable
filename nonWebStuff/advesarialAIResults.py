''' This file is used to get all the advesarial AI reuslts and write them to a seperate file '''

''' Stuff to import '''
import sys
from types import ModuleType

import MCTSAIvsMCTSAI 
import MCTSAIvsMCTSnoUCBAI
import MCTSAIvsMCTSopAI
import MCTSAIvsSimpleAI

import MCTSnoUCBAIvsMCTSAI
import MCTSnoUCBAIvsMCTSnoUCBAI
import MCTSnoUCBAIvsMCTSopAI
import MCTSnoUCBAIvsSimpleAI

import MCTSopAIvsMCTSAI
import MCTSopAIvsMCTSnoUCBAI
import MCTSopAIvsMCTSopAI
import MCTSopAIvsSimpleAI

import SimpleAIvsSimpleAI 
import SimpleAIvsMCTSAI
import SimpleAIvsMCTSnoUCBAI
import SimpleAIvsMCTSopAI

from typing import List, Tuple
from types import ModuleType

UPPERBOUND: int = 1

LISTOFINFO: List[Tuple[str, ModuleType]] = [
    ("SimpleAI vs Simple AI:", SimpleAIvsSimpleAI),
    ("SimpleAI vs MCTSAI:", SimpleAIvsMCTSAI), 
    ("SimpleAI vs no UCB MCTSAI:", SimpleAIvsMCTSnoUCBAI), 
    ("SimpleAI vs Open Loop MCTSAI:", SimpleAIvsMCTSopAI),

    ("MCTSAI vs MCTSAI", MCTSAIvsMCTSAI),
    ("MCTSAI vs no UCB MCTSAI", MCTSAIvsMCTSnoUCBAI),
    ("MCTSAI vs Open Loop MCTSAI", MCTSAIvsMCTSopAI),
    ("MCTSAI vs SimpleAI", MCTSAIvsSimpleAI),
    
    ("no UCB MCTSAI vs MCTSAI", MCTSnoUCBAIvsMCTSAI),
    ("no UCB MCTSAI vs no UCB MCTSAI", MCTSnoUCBAIvsMCTSnoUCBAI),
    ("no UCB MCTSAI vs Open Loop MCTSAI", MCTSnoUCBAIvsMCTSopAI),
    ("no UCB MCTSAI vs SimpleAI", MCTSnoUCBAIvsSimpleAI),

    ("Open Loop MCTSAI vs MCTSAI", MCTSopAIvsMCTSAI),
    ("Open Loop MCTSAI vs no UCB MCTSAI", MCTSopAIvsMCTSnoUCBAI),
    ("Open Loop MCTSAI vs Open Loop MCTSAI", MCTSopAIvsMCTSopAI),
    ("Open Loop MCTSAI vs SimpleAI", MCTSopAIvsSimpleAI)]

def main():
    i: int = 0
    original_stdout = sys.stdout
    fileOut = open('advesarialAIResults1.txt', 'w')

    for info in LISTOFINFO:
        print("\nStarting " + info[0], end= "")
        sys.stdout = fileOut
        i = 0
        print(info[0])
        while (i < UPPERBOUND):
            info[1].main()
            i += 1
        print("")
        sys.stdout = original_stdout
        print("   ...done")

    sys.stdout = original_stdout
    fileOut.close()

if __name__ == "__main__":
    main()