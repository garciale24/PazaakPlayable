''' 
This file is used to rework the Advesarial AI data so that it is easier to use with Tableau
'''

''' Importing panda library '''
import pandas as pd

''' This function will rework the data for the AI battles '''
def main():
    counter: int = 0
    file1 = open("advesarialAIResults1.txt", "r")
    outStr: str = "Battle, Time, Player 1 Wins, Player 2 Wins\n"
    outStrFR: str = "Battle, Time, Player 1 Wins, Player 2 Wins\n"
    for line in file1:
        outStr += line + ","
        if counter % 3 == 0:
            for char in line:
                if char == ":" or char == "\n":
                    break
                else:
                    outStrFR += char
        elif counter % 3 == 1:
            outStrFR += ", "
            for char in line:
                if char == " ":
                    break
                else:
                    outStrFR += char
        elif counter % 3 == 2:
            outStrFR += ", "
            flag1: int = 0
            for char in line:
                if char == " ":
                    if flag1 == 0:
                        flag1 = 1
                    else:
                        flag1 = 0
                        outStrFR += ", "
                if flag1 == 1:
                    outStrFR += char
        if counter == 3:
            counter = 0
        else:
            counter += 1
    file1.close()
    file2 = open("adResultsReworked.txt", "w")
    for line in outStrFR:
        file2.write(line)
    file2.close()

    # readinag given csv file
    # and creating dataframe
    dataframe1 = pd.read_csv("adResultsReworked.txt")

    # storing this dataframe in a csv file
    dataframe1.to_csv("adResultsReworked.csv", 
                  index = None)

    # The output schema looks something like this:

    # Battle, Time, Player 1 Wins, Player 2 Wins
    # SimpvSimp, 1.535, 4794, 5206
    # SimpvMCTS, 336.09, 309, 691

if __name__ == "__main__":
    main()