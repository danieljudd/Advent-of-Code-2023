# AOC day 7 2023
# -- unfinished --

# Set up for camel card lookup table
cards = ["A",2,3,4,5,6,7,8,9,10,"J","K","Q"]
GivenCards = ["A","A",2,3,9]
def returnloc(loc):
    myindex = cards.index(loc)
    print(myindex)

for a in range(len(GivenCards)):
    returnloc(GivenCards[a])
