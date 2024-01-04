
# Day 3, 2023
# Bug/Requirement: you have to add a BLANK row of dots above and below the text file (day3.txt)
# ...for this to work. 
# Number of dots must equal to standard line length.

input = """..........
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
.........."""

with open("day3.txt") as f:
    input = f.read()

# take whole input as one line, if next character is a number add to variable


    WholeList = []
    # Returns dictionary with key Position and value Number
    def GetPos():
        temp = ""
        count = 0

        for i in input:
            if i.isdigit():
                # Count position
                count += 1
                # print("int")
                # Add digit to string
                temp = temp+i
            else:
                # Count position
                count += 1
                # print("dot")
                # Store digit string to return
                wholenum = temp
                if wholenum.isdigit():
                    # Store number by a position (i.e., rightmost digit position)
                    sublist = [int(wholenum),count-1]
                    WholeList.append(sublist)
                # Reset string
                temp = ""
        return WholeList


    def GetLineLength(Input):
        count = 0
        for i in Input:
            if i == "\n":
                return count
            else:
                pass
            count += 1



    def CheckSides(thing):
        SideList = {}
        for i in thing:
            WL = len(str(i[0]))
            LeftPos = i[1]-WL-1
            RightPos = i[1]
            # See if either side of number word is permissible
            if (input[LeftPos]  == ".") and (input[RightPos] == "."):
                # if either side has a dot, return true
                # print(True,thing[i],"dots")
                pass
            elif (input[LeftPos]  == "\n") and (input[RightPos] == "."):
                # print(True,thing[i],"right dot")
                pass
            elif (input[LeftPos]  == ".") and (input[RightPos] == "\n"):
                # print(True,thing[i],"left dot")
                pass
            else:
                SideList[i[1]]=i[0]
            
        return(SideList)

    # print(CheckSides(GetPos()))

    # See if every other character that is not on side passes
    def EverythingElse(thing):
        temp = {}
        temp2 = {}

        for i in thing:
            LL = GetLineLength(input)+1
            WL = len(str(i[0]))
            WL = int(WL)+2
            
            checklist = [".","\n",1,2,3,4,5,6,7,8,9,0]
            for num in range(WL):
                # We want a number as a position to match the input position
                upperstart = i[1]-LL-WL+num+1
                lowerstart = i[1]+LL-WL+num+1
                # print(input[upperstart],input[lowerstart])
                # if upperstart >= 0 and lowerstart <= len(input):
                if input[upperstart] in checklist and input[lowerstart] in checklist:
                    pass
                else:
                    temp[i[1]] = i[0]
            # print("adding "+str(temp))
            temp2.update(temp)
            temp.clear()
        return(temp2)

    def SumPartNumbers():
        # Create list of invalid numbers
        test1=CheckSides(Dict)
        test2=EverythingElse(Dict)

        print(test1,"Check sides \n")
        print(test2,"Check outer but not sides \n")
        # print(test1.intersection(test2))
        # SumParts = sum((test1.intersection(test2)))
        # print(SumParts)
        # print(sum(c))
        newDict = []
        for item in Dict:
            newDict.append(item[0])
        GrandTotalSum = sum(newDict)
        
        
        verycool = test1|test2
        
        print("Test1: ",test1,"Test2: ",test2,"Final: ",verycool)
        CollectValues = verycool.values()
        # for item in newDict:
        #     remove()
        SumValues = sum(CollectValues)
        print(str(GrandTotalSum) + " - " + str(SumValues) + " = " + str(GrandTotalSum-SumValues))
        print("it's the second value above ^ : " + str(SumValues))
Dict = GetPos()
SumPartNumbers()
