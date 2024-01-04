# Day 4, 2023

import re
input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

# Bug - don't have a trailing blank space after the day4.txt input
with open("day4.txt") as f:
    input = f.read()

    # split on bar and new line
    arrays = re.split("\||\n",input)

    # separate winning card numbers from my numbers
    Card = arrays[::2]
    MyNumbers = arrays[1::2]

    def stripper(thing):
        temp = []
        for item in thing:
            newthing = ""
            newthing = item.split()
            temp.append(newthing)
        return temp
        print(temp)
    Card = stripper(Card)
    MyNumbers = stripper(MyNumbers)

    # delete card numbers
    for n in range(len(Card)):
        Card[n].pop(0)
        Card[n].pop(0)

    # count n of cards
    length = int(len(arrays)/2)

    # count iteration of symmetrical inputs (maybe equal to number of lines in file)
    count = 0
    # tally every winning value and push it to the total variable
    coolsum = 0
    total = 0

    for i in MyNumbers:
        # N tally for number of matching outputs per card line
        N = 0
        # If "coolsum" isn't reset to zero after a falsy iteration, it will just add
        # the last truthy figure to the count
        coolsum=0
        for j in i:
            if j in Card[count]:
                # print(j,count)
                coolsum = pow(2,N)
                N += 1
        total += coolsum
        count += 1
    print(total)


