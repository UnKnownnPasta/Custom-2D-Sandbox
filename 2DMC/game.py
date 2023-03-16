import csv
import subprocess

p = subprocess.Popen(['python', '2DMC/mapcreate.py'], stderr=subprocess.PIPE)

output, _ = p.communicate() # Wait for the subprocess to complete and get its output
p.terminate() # Print the output and exit

load = []
terrainLoad = open('2DMC/terrainData.csv', 'r', encoding='utf-8')

reader = csv.reader(terrainLoad)
for row in reader:
    load.append(row)

TerrainOne, TerrainTwo, TerrainThree, CaveMap, hotbar, inventory = [list(row) for row in load]

x = 1

while True:
    pass