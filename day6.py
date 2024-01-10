# Day 6 AOC 2023

import re

input = """Time:      7  15   30
Distance:  9  40  200"""

with open("day6.txt") as f:
    input = f.read()
    f.close()
input = input.splitlines()

# Same solution as day 5
newthing=[]
for item in input:
    temp = re.split(":| ",item)
    temp = list(filter(None,temp))
    # if filtered item (temp) is empty, ignore it
    if temp:
        newthing.append(temp)

print(newthing)

# 1. We want to see which races are valid and not null, i.e., must have travelled any distance
# 2. Work out sum of array pairs by iterating 1 to (time constant)
## 2a. time held button multiplied by distance remaining
## 2b. AND condition, must not be multiplied by MAX time value or zero
# 3. Stop iterating if race is not possible / must be falsy in summary

countwinners = 1
for a, b in zip(newthing[0][1::],newthing[1][1::]):
    holdtime = 1
    arrayoftimes = []
    for c in range(int(a)):
        travel = holdtime*(int(a)-holdtime)
        # redundant not zero
        if not 0 and holdtime < int(a) and travel > int(b):
            arrayoftimes.append(travel)
        holdtime+=1
    print(arrayoftimes)
    countwinners*=len(arrayoftimes)
print("Your answer: " + str(countwinners))