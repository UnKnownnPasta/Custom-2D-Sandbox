import csv

load = []
terrainLoad = open('2DMC/terrainData.csv', 'r', encoding='utf-8')

reader = csv.reader(terrainLoad)
for row in reader:
    load.append(row)

TerrainOne, TerrainTwo, TerrainThree, CaveMap, hotbar, inventory, currentTerrain, errorList, terrainMapStorage, callLog = [list(row) for row in load]

placeableBlocks, noMoveBlocks = ['🟫', '🧮'], ['🔘', '🟪']
obtainableItems = ['stone|🔘', 'wood|🟫', 'craft|💠', 'furnace|🧮', 'iron|🟪']

def healthModify(listInv): # Register damage
    for i in range(8,-1,-1): # 0,1,..,8
        if listInv[i] == '💓':
            if i == 0: listInv[i] = '🖤'
            else: listInv[i] = '🖤'

def invModify(item, listPrim): # Register picking up wood from trees
    for i in range(12,len(listPrim)):
        found = -1
        if found == -1 and listPrim[i] == '🔲':
            found = i
            listPrim[found] = item
            break
    else:
        for i in range(0,len(inventory)):
            if inventory[i] == '🔲':
                inventory[i] = item
                break

def objEncounterCheck(terrainMap, xCord, yCord, listInv, bckpTerrain): # Check if you walked into lava or tree or walls of cave
    if terrainMap[6] == 'T-1' and bckpTerrain[yCord][xCord] in ['⬛', '  ']:
        match bckpTerrain[yCord][xCord]:
            case '⬛': callLog['cave'] = 'nomove'
            case '  ': callLog['cave'] = 'entercave'
    if bckpTerrain[yCord][xCord] == '🌳':
        invModify('🟫',listInv)
    elif bckpTerrain[yCord][xCord] == '🟧':
        hpCall = healthModify(listInv)
        if hpCall == 'dead':
            listInv[10] = '💀'
            mapLog(terrainMap)
            hbLog(listInv)
            print('\nYou Died by Stepping On Lava!')
            return callLog['']