# AOC day 7 2023
# Very difficult :-)

import re

input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

with open("day7.txt") as f:
    input = f.read()
    f.close()

input = re.split("\n| ",input)
GivenCards = []
for word in input[::2]:
    GivenCards.append(list(word))
# print(GivenCards)

ScoreCards = input[1::2]
# print(ScoreCards)

# List append converts items to strings
Cards = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]

# Abstract the value of a given card by value (strength) in ordered list "Cards"
def returnloc(loc):
    myindex = Cards.index(loc)
    # +1 needed because result of 0 is unworkable?
    return myindex+1


tally = []
# Iterate through cards only and translate individual cards to their strengths
for a in range(len(GivenCards)):
    temp = []
    for b in range(len(GivenCards[a])):
        temp.append(returnloc(GivenCards[a][b]))
    # do the if/else statements here
    tally.extend([temp])
# print(tally)

# Takes array called tally and returns dictionary containing count of numbers within
def counttally(i):
    count = {}
    for j in tally[i]:
        if not j in count:
            count[j] = 1
        else:
            count[j] +=1
    return count

# Take dictionary set of "Card Value : Card Count" and see if they qualify for points
# Make truth table?? count each instance of a qualifying hand

CHigh = []
CPair = []
CTwoPair = []
CThree = []
CHouse = []
CFour = []
CFive = []

for i in range(len(tally)):
    iterable = counttally(i)
    points = int(ScoreCards[i])
    Counter2 = 0
    Counter3 = 0
    LineHand = []

    Bucket = None
    CountCards = 0
    # j is value of card, k is count of that criterion
    for j,k in iterable.items():
        Hand = tally[i]
        Hand = Hand+[points]
        print(j,k)
        if k >= 5:
            LineHand.extend([[j,k,points]])
            print("Five of a kind",Hand)
            CFive.extend([Hand])

        elif k >= 4:
            LineHand.extend([[j,k,points]])
            print("Four of a kind",Hand)
            CFour.extend([Hand])

        elif k >= 3:
            LineHand.extend([[j,k,points]])
            Counter3+=1
            print("Three alone",Hand)
            CThree.extend([Hand])
            # Repeated below
            if Counter2 == 1 & Counter3 == 1:
                print("Full house - Three and a two",Hand)
                CHouse.extend([Hand])
                CThree.pop()
                CPair.pop()
        elif k >= 2:
            LineHand.extend([[j,k,points]])
            Counter2+=1
            if Counter2 == 2:
                print("Two Pairs",Hand)
                CTwoPair.extend([Hand])
                # Pop the "one pair" array as it would've naturally added it upon first detection
                CPair.pop()
            elif k == 2:
                print("Pair",Hand)
                CPair.extend([Hand])
            # Repeat of k>=3
            if Counter2 == 1 & Counter3 == 1:
                print("Full house - Three and a two",Hand)
                CHouse.extend([Hand])
                CThree.pop()
                CPair.pop()
        else:
            LineHand.extend([[j,k,points]])
            if len(LineHand) == 5:
                print("High Card - All unique",Hand)
                CHigh.extend([Hand])             
    # print(Bucket)

# Can't think of a simpler way of sorting by first value in each sub-array
CHigh.sort(key=lambda x:x)
CPair.sort(key=lambda x:x)
CTwoPair.sort(key=lambda x:x)
CThree.sort(key=lambda x:x)
CHouse.sort(key=lambda x:x)
CFour.sort(key=lambda x:x)
CFive.sort(key=lambda x:x)
MyHands = []
MyHands.extend([CHigh]+[CPair]+[CTwoPair]+[CThree]+[CHouse]+[CFour]+[CFive])

# Exclude empty arrays / none values i.e., []
MyHands = list(filter(None,MyHands))

Sum = 0
Count = 1
for n in MyHands:
    for m in n:
        Sum += (m[-1]*Count)
        Count+=1

print(Sum)