import os

grid = dict()
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    for y, line in enumerate(f):
        line = line.replace("\n","")
        for x, char in enumerate(line):
            if char == "|":
                grid[(x,y)] = 1
            elif char == "#":
                grid[(x,y)] = -1
            else:
                grid[(x,y)] = 0

xmin, xmax = min(grid, key=lambda square: square[0])[0], max(grid, key=lambda square: square[0])[0]
ymin, ymax = min(grid, key=lambda square: square[1])[1], max(grid, key=lambda square: square[1])[1]

def check_neighborhood(coords):
    trees = 0
    lumberyards = 0
    neighborhood = [(x,y) for x in range(coords[0]-1, coords[0]+2) for y in range(coords[1]-1, coords[1]+2) if x != coords[0] or y != coords[1]]
    for neighbor in neighborhood:
        item = grid.get(neighbor,0)
        if item > 0:
            trees += 1
        elif item < 0:
            lumberyards += 1
    return((trees, lumberyards))

for iter in range(10):
    new_grid = grid.copy()
    for coords, content in grid.items():
        neighborhood = check_neighborhood(coords)
        if content > 0:
            if neighborhood[1] >= 3:
                new_grid[coords] = -1
        elif content == 0:
            if neighborhood[0] >= 3:
                new_grid[coords] = 1
        elif content < 0:
            if neighborhood[0] * neighborhood[1] == 0:
                new_grid[coords] = 0
    grid = new_grid.copy()

trees = sum([x for x in grid.values() if x == 1])
lumberyards = sum([-x for x in grid.values() if x == -1])

answer = trees * lumberyards
print(answer)