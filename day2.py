# Day 2, 2023

import re

with open("day2.txt") as f:
    input = f.read()

    # Regex to clean and structure string as list
    input = re.split(', |; |\n|: ', input)

    bluemax = 14
    greenmax = 13
    redmax = 12

    # if list item contains the colour we wantm add the NUMBER (only) to these lists
    BlueList = []
    GreenList = []
    RedList = []

    # Iterate over list, if the colour matches what we want, add extracted number to colour list 
    # upon finding the word "game" sum the already counted colours for that game
    # clear list before summing the next batch
    def ColourGame(Colour,Cubes,ColourList):
        List = []
        List.clear()
        for items in input:
            if Colour in items:
                List.extend(re.findall("\d+", items))
            if "Game" in items:
                # map to return list holding stringified integers converted to pure integers
                List = list(map(int,List))
                ColourList.append(List)

                List.clear()
        # (Repeat code) Sum last iteration without the "game" trigger
        List = list(map(int,List))
        ColourList.append(List)


    # Append each game to their respective lists (100 item in each = 100 games)
    # (String to search, colour limit, list to append it to)
    ColourGame("blue",bluemax,BlueList)
    ColourGame("green",greenmax,GreenList)
    ColourGame("red",redmax,RedList)
    # Process ith iteration from each colour, if all are below the "max" limit:
    # ... then store list iteration matching the game ID (in a list of its own)
    # sum all valid game IDs


    GamesPossible = 0

    # Note to self: had to refactor how arrays were made because colour arrays could be over
    # 100 count, now each colour array has a total of 100 "sets"
    # In fact, actual sets would be quicker to iterate over!
    greenset = set()
    blueset = set()
    redset = set()

    # --Repeated code for each colour--
    for i in range(len(GreenList)-1):
        # Not sure why key=int was required but it painfully fixed this part for me
        thing = max(GreenList[i], key=int)
        if int(thing) <= greenmax:
            greenset.add(i+1)
    print(greenset)

    for i in range(len(RedList)-1):
        # Not sure why key=int was required but it painfully fixed this part for me
        thing = max(RedList[i], key=int)
        if int(thing) <= redmax:
            redset.add(i+1)
    print(redset)

    for i in range(len(BlueList)-1):
        # Not sure why key=int was required but it painfully fixed this part for me
        thing = max(BlueList[i], key=int)
        if int(thing) <= bluemax:
            blueset.add(i+1)
    print(blueset)

    Intersect = greenset.intersection(blueset,redset)
    TotalID = str((sum(Intersect)))

    print("The sum of your valid IDs are: " + TotalID + ", what a high number!")

    # I will be embarrassed to look at this code in future