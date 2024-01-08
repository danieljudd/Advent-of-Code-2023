# Day 5 AOC 2023

import re
input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

with open("day5.txt") as f:
    input = f.read()

    input = input.splitlines()

    # Create a clean array to filter section titles, and their values
    newthing=[]
    for item in input:
        temp = re.split(":| |map",item)
        temp = list(filter(None,temp))
        # if filtered item (temp) is empty, ignore it
        if temp:
            newthing.append(temp)
    # Manually move first string in index because it's irregular
    newthing.insert(0,[])
    newthing[0].insert(0, newthing[1].pop(0))
    f.close()

# -- Not needed anymore --
# # Make a dictionary key:value(list) pair
# dic = {}
# temp = ""
# for item in newthing[::]:
#     for things in item:
#         if not things.isdigit():
#             temp = things
#             dic.setdefault(temp,[])
#         else:
#             dic[temp].append(int(things))

# Make subarrays by with string/title at the header
maplist = []
tempcounter = -1
temp = ""
for item in newthing:
    for things in item:
        if not things.isdigit():
            temp = things
            maplist.append([temp])
            tempcounter+=1
        else:
            maplist[tempcounter].append(int(things))
    
def getlen(alist):
    # Divide each array by 3 to get N of array sections in subset of arrays
    newlist = int((len(alist)-1)/3)
    # Return int calculation
    return newlist


def CheckSeed(seed):
    for a in range(1,len(maplist)):
        counter=a
        # Get length of array in seed-to-soil map, etc...
        arraylines=int(getlen(maplist[counter]))
        for b in range(arraylines):
            
            # Next place to look in variable a
            destination=maplist[counter][(3*(b+1))-2]

            # See if input is in range
            source=maplist[counter][((3)*(b+1))-1]

            # Range variable
            seedrange=maplist[counter][(3)*(b+1)]

            if seed in range(source,source+seedrange):
                seed = (seed-source)+destination
                break
    return seed

# Create an array of results where the smallest number (i.e., distance) is the result
SeedArray = []
for i in range(len(maplist[0])-1):
    seed = maplist[0][i+1]
    SeedArray.append(CheckSeed(seed))
print(min(SeedArray))


# --Old stuff for when I used a dictionary--

# # print(list(dic.values())[::])
# print(len(dic.get(list(dic.keys())[2])))
# # print every 3rd from dic
# print(dic.get(list(dic.keys())[2])[2::3])


# graph = []
# # let's build a graph
# for item in dic.get('seeds'):
#     seed = []
#     seed.append(item)
#     for thing in dic.get('seed-to-soil'):
#         print(thing)

#     graph.extend(seed)
# print(graph)