import os
from operator import itemgetter
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

finder = AStarFinder(diagonal_movement=DiagonalMovement.never)

grid = list()
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    for line in f:
        grid.append(list(line.replace("\n","")))

len_x = len(grid[0])
len_y = len(grid)

mobs = list()
for y, line in enumerate(grid):
    for x, square in enumerate(line):
        if (grid[y][x] == "E") or (grid[y][x] == "G"):
            mobs.append([grid[y][x],x,y,200,3,True])

def list_range(targets, grid):
    range = list()
    for target in targets:
        if target[1] > 0:
            if grid[target[2]][target[1] - 1] == ".":
                range.append([target[1] - 1, target[2]])
        if target[1] < len_x - 1:
            if grid[target[2]][target[1] + 1] == ".":
                range.append([target[1] + 1, target[2]])
        if target[2] > 0:
            if grid[target[2] - 1][target[1]] == ".":
                range.append([target[1], target[2] - 1])
        if target[2] < len_y - 1:
            if grid[target[2] + 1][target[1]] == ".":
                range.append([target[1], target[2] + 1])
    range = sorted(range, key = lambda x: (x[1], x[0]))
    return(range)

def grid_to_matrix(grid):
    matrix = list()
    for y, line in enumerate(grid):
        new_line = list()
        for x, square in enumerate(line):
            if grid[y][x] == ".":
                new_line.append(1)
            else:
                new_line.append(0)
        matrix.append(new_line)
    return(matrix)

def find_moves(mob, range, grid):
    matrix = grid_to_matrix(grid)
    results = list()
    for square in range:
        maze = Grid(matrix=matrix)
        start = maze.node(mob[1], mob[2])
        end = maze.node(square[0], square[1])
        path, runs = finder.find_path(start, end, maze)
        if len(path) > 0:
            results.append([square[0], square[1], len(path), path[1]])
    return(results)

def action(index, mobs, grid):
    if mobs[index][0] == "E":
        ennemy = "G"
    elif mobs[index][0] == "G":
        ennemy = "E"
    targets = [x for x in mobs if x[0] == ennemy and x[5] == True]
    if len(targets) == 0:
        friends = targets = [x for x in mobs if x[0] != ennemy and x[5] == True]
        total_hp = sum([mob[3] for mob in friends])
        return(total_hp)
    else:
        neighbours_ennemies = list()
        if mobs[index][1] > 0:
            if grid[mobs[index][2]][mobs[index][1] - 1] == ennemy:
                neighbour = list(filter(lambda x: x[1] == (mobs[index][1] - 1) and x[2] == (mobs[index][2]), mobs))
                neighbours_ennemies.append(neighbour[0])
        if mobs[index][1] < len_x - 1:
            if grid[mobs[index][2]][mobs[index][1] + 1] == ennemy:
                neighbour = list(filter(lambda x: x[1] == (mobs[index][1] + 1) and x[2] == (mobs[index][2]), mobs))
                neighbours_ennemies.append(neighbour[0])
        if mobs[index][2] > 0:
            if grid[mobs[index][2] - 1][mobs[index][1]] == ennemy:
                neighbour = list(filter(lambda x: x[1] == (mobs[index][1]) and x[2] == (mobs[index][2] - 1), mobs))
                neighbours_ennemies.append(neighbour[0])
        if mobs[index][2] < len_y - 1:
            if grid[mobs[index][2] + 1][mobs[index][1]] == ennemy:
                neighbour = list(filter(lambda x: x[1] == (mobs[index][1]) and x[2] == (mobs[index][2] + 1), mobs))
                neighbours_ennemies.append(neighbour[0])
        if len(neighbours_ennemies) > 0:
            neighbours_ennemies.sort(key=itemgetter(3))
            lowest_hp = neighbours_ennemies[0][3]
            low_hp = [mob for mob in neighbours_ennemies if mob[3] == lowest_hp]
            low_hp = sorted(low_hp, key = lambda x: (x[2], x[1]))
            target = mobs.index(low_hp[0])
            mobs[target][3] = mobs[target][3] - mobs[index][4]
            if mobs[target][3] <= 0:
                mobs[target][5] = False
                grid[mobs[target][2]][mobs[target][1]] = "."
            return(-1)
        else:
            moves = find_moves(mobs[index], list_range(targets, grid), grid)
            if len(moves) > 0:
                moves.sort(key=itemgetter(2,1,0))
                move = list(moves[0][3])
                grid[mobs[index][2]][mobs[index][1]] = "."
                grid[move[1]][move[0]] = mobs[index][0]
                mobs[index][1] = move[0]
                mobs[index][2] = move[1]
                neighbours_ennemies = list()
                if mobs[index][1] > 0:
                    if grid[mobs[index][2]][mobs[index][1] - 1] == ennemy:
                        neighbour = list(filter(lambda x: x[1] == (mobs[index][1] - 1) and x[2] == (mobs[index][2]), mobs))
                        neighbours_ennemies.append(neighbour[0])
                if mobs[index][1] < len_x - 1:
                    if grid[mobs[index][2]][mobs[index][1] + 1] == ennemy:
                        neighbour = list(filter(lambda x: x[1] == (mobs[index][1] + 1) and x[2] == (mobs[index][2]), mobs))
                        neighbours_ennemies.append(neighbour[0])
                if mobs[index][2] > 0:
                    if grid[mobs[index][2] - 1][mobs[index][1]] == ennemy:
                        neighbour = list(filter(lambda x: x[1] == (mobs[index][1]) and x[2] == (mobs[index][2] - 1), mobs))
                        neighbours_ennemies.append(neighbour[0])
                if mobs[index][2] < len_y - 1:
                    if grid[mobs[index][2] + 1][mobs[index][1]] == ennemy:
                        neighbour = list(filter(lambda x: x[1] == (mobs[index][1]) and x[2] == (mobs[index][2] + 1), mobs))
                        neighbours_ennemies.append(neighbour[0])
                if len(neighbours_ennemies) > 0:
                    neighbours_ennemies.sort(key=itemgetter(3))
                    lowest_hp = neighbours_ennemies[0][3]
                    low_hp = [mob for mob in neighbours_ennemies if mob[3] == lowest_hp]
                    low_hp = sorted(low_hp, key = lambda x: (x[2], x[1]))
                    target = mobs.index(low_hp[0])
                    mobs[target][3] = mobs[target][3] - mobs[index][4]
                    if mobs[target][3] <= 0:
                        mobs[target][5] = False
                        grid[mobs[target][2]][mobs[target][1]] = "."
            return(-1)

fighting = True
round = 0

while fighting:
    mobs = sorted(mobs, key = lambda x: (x[2], x[1]))
    for index, mob in enumerate(mobs):
        if mob[5] == True:
            res = action(index, mobs, grid)
            if res >= 0:
                print(res*round)
                fighting = False
                break
    mobs = [mob for mob in mobs if mob[5] == True]
    round = round + 1
