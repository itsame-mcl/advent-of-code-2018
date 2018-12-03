import os

data = list()
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    for ligne in f:
        data.append(ligne.replace('\n',"").replace('@',"").replace(':',"").split(" "))

grid = [[0 for i in range(1000)] for j in range(1000)]

for claim in data:
    topleft_coords = claim[2].split(",")
    size = claim[3].split("x")
    for i in range(int(topleft_coords[0]),int(topleft_coords[0])+int(size[0])):
        for j in range(int(topleft_coords[1]),int(topleft_coords[1])+int(size[1])):
            grid[i][j] += 1

overleap = 0
for i in range(0,1000):
    for j in range(0,1000):
        if grid[i][j] >= 2:
            overleap += 1

print(overleap)