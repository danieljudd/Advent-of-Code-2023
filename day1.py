# Day 1, 2023

with open("day1.txt") as f:
    InputString = f.read()

    def StripCharacters(myinput):
        NumbersOnly = myinput.splitlines()
        FirstArray = []
        for item in NumbersOnly:
            thing = (''.join(i for i in item if i.isdigit()))
            FirstArray.append(thing)
        
        SecondArray = []
        for item in FirstArray:
                nFirst = item[0]
                nLast = item[-1]
                Calculate = str(nFirst)+str(nLast)
                SecondArray.append(int(Calculate))
        return SecondArray

    print(StripCharacters(InputString))
    Sum = (sum(StripCharacters(InputString)))

    print("The sum of all of the calibration values for you is " + str(Sum))
