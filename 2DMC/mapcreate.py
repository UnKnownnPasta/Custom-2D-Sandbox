# Creating Terrain
from copy import deepcopy
from random import randint
import subprocess
import csv

# This is where the lists for terrain is prepared
terrainOne, terrainTwo, terrainThree, caveMap = ([] for i in range(4)) # Unpack three uninitialized lists
for i in range(3):
    for j in range(6):
        ns = []
        for k in range(30):
            percent = randint(1,100)
            if percent > 80:
                ns.append('🟨')
            elif percent > 20 and percent < 80:
                ns.append('🟩')
            elif percent < 20 and percent > 10:
                ns.append('🟦')
            elif percent < 5:
                ns.append('🟧')
            else:
                ns.append('🌳')
        if i == 0: terrainOne.append(ns) 
        if i == 1: terrainTwo.append(ns)
        if i == 2: terrainThree.append(ns)

for j in range(7): # Cave map gen
    ns = []
    for k in range(30):
        if j%2 == 0:
            percent = randint(1,100)
            if percent > 70:
                ns.append('🔘')
            else:
                ns.append('🟪')
        else:
            if randint(0,10) < 1:
                ns.append('🟧')
            else:
                ns.append('  ')
    caveMap.append(ns)

caveMap[1][29] = caveMap[3][29] = caveMap[3][0] = caveMap[5][0] = '🔘'
caveMap[2][28] = caveMap[4][1] = '  ' # fixing walls

terrainOne += ['T-0', {'dropcount':0}]
terrainTwo += ['T-1', {'dropcount':0}]
terrainThree += ['T-2', {'dropcount':0}] # Just list identifiers
caveMap += ['C-0', {'dropcount':0}]

hotbar = ['💓']*9+[' '*11,'👨',' '*11]+['🔲']*9 # just a simpler way of making the list
inventory = ['🔲']*25

def createCave(x, y, gMap, bkpMap): # Generate the entrance to the cave in the map
    for i in range(y, y+3):
        for j in range(x,x+4):
            if i == y or i == y+2:
                gMap[i][j], bkpMap[i][j] = '⬛', '⬛'
                continue
            elif i == y+1:
                if j == x:
                    gMap[i][j], bkpMap[i][j] = '⬛', '⬛'
                if j in [x+1, x+2]:
                    gMap[i][j], bkpMap[i][j] = '  ', '  '

hotbar = ['💓']*9+[' '*11,'👨',' '*11]+['🔲']*9 # just a simpler way of making the list
inventory = ['🔲']*25

bckpT1 = deepcopy(terrainOne)
bckpT2 = deepcopy(terrainTwo)
bckpT3 = deepcopy(terrainThree)

dx, dy, dxy = randint(14,18), randint(1,3), []
createCave(dx, dy, terrainTwo, bckpT2)

currentTerrain, errorList, callLog = 0, [], {}
terrainMapStorage = {
    't0': terrainOne, 'b0': bckpT1,
    't1': terrainTwo, 'b1': bckpT2,
    't2': terrainThree, 'b2': bckpT3,
    't3': caveMap, 'b3': caveMap # supposed to be backup map
}

setup = [
    terrainOne,
    terrainTwo,
    terrainThree,
    caveMap, 
    hotbar, 
    inventory, 
    currentTerrain, 
    errorList, 
    terrainMapStorage
]


with open('2DMC/terrainData.csv', mode='w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for t in setup:
        writer.writerow(t)
