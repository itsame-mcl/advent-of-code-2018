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
            results.append([square[0], square[1], len(path) - 1, path[1]])
    return(results)

def find_next_move(start_x, start_y, target_x, target_y, len_min):
    base_matrix = grid_to_matrix(grid)
    if start_y > 0 and base_matrix[start_y - 1][start_x] == 1:
        up_matrix = base_matrix.copy()
        up_matrix[start_y][start_x] = 1
        up_matrix[start_y - 1][start_x] = 0
        up_maze = Grid(matrix=up_matrix)
        up_start = up_maze.node(start_x, start_y - 1)
        up_end = up_maze.node(target_x, target_y)
        up_path, up_runs = finder.find_path(up_start, up_end, up_maze)
        if len(up_path) > 0:
            up_move = [start_x, start_y - 1, len(up_path) - 1]
        else:
            up_move = [start_x, start_y - 1, -1]
    else:
        up_move = [start_x, start_y - 1, -1]
    if start_x > 0 and base_matrix[start_y][start_x - 1] == 1:
        left_matrix = base_matrix.copy()
        left_matrix[start_y][start_x] = 1
        left_matrix[start_y][start_x - 1] = 0
        left_maze = Grid(matrix=left_matrix)
        left_start = left_maze.node(start_x - 1, start_y)
        left_end = left_maze.node(target_x, target_y)
        left_path, left_runs = finder.find_path(left_start, left_end, left_maze)
        if len(left_path) > 0:
            left_move = [start_x - 1, start_y, len(left_path) - 1]
        else:
            left_move = [start_x - 1, start_y, -1]
    else:
        left_move = [start_x - 1, start_y, -1]
    if start_x < len_x - 1 and base_matrix[start_y][start_x + 1] == 1:
        right_matrix = base_matrix.copy()
        right_matrix[start_y][start_x] = 1
        right_matrix[start_y][start_x + 1] = 0
        right_maze = Grid(matrix=right_matrix)
        right_start = right_maze.node(start_x + 1, start_y)
        right_end = right_maze.node(target_x, target_y)
        right_path, right_runs = finder.find_path(right_start, right_end, right_maze)
        if len(right_path) > 0:
            right_move = [start_x + 1, start_y, len(right_path) - 1]
        else:
            right_move = [start_x + 1, start_y, -1]
    else:
        right_move = [start_x + 1, start_y, -1]
    if start_y < len_y - 1 and base_matrix[start_y + 1][start_x] == 1:
        down_matrix = base_matrix.copy()
        down_matrix[start_y][start_x] = 1
        down_matrix[start_y + 1][start_x] = 0
        down_maze = Grid(matrix=down_matrix)
        down_start = down_maze.node(start_x, start_y + 1)
        down_end = down_maze.node(target_x, target_y)
        down_path, down_runs = finder.find_path(down_start, down_end, down_maze)
        if len(down_path) > 0:
            down_move = [start_x, start_y + 1, len(down_path) - 1]
        else:
            down_move = [start_x, start_y + 1, -1]
    else:
        down_move = [start_x, start_y + 1, -1]
    if up_move[2] == len_min - 1:
        return(up_move)
    elif left_move[2] == len_min - 1:
        return(left_move)
    elif right_move[2] == len_min - 1:
        return(right_move)
    elif down_move[2] == len_min - 1:
        return(down_move)
    else:
        raise ValueError
        

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
                move = find_next_move(mobs[index][1], mobs[index][2], moves[0][0], moves[0][1], moves[0][2])
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