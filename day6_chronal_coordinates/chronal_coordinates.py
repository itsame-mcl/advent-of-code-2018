import os
from operator import itemgetter

data = list()
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    for line in f:
        str_line = line.replace('\n',"").split(",")
        data.append([int(str_line[0]), int(str_line[1])])

max_coord = [0] * 2
max_coord[0] = max(coord[0] for coord in data)
max_coord[1] = max(coord[1] for coord in data)

def compute_grid(offset = 0):
    grid = list()
    for j in range(0,(max_coord[1] + 1 + 2*offset)):
        grid_line = list()
        for i in range(0,(max_coord[0] + 1 + 2*offset)):
            min_dist = None
            closest_point = None
            for point in range(0,len(data)):
                taxicab_dist = abs(data[point][0] + offset - i) + abs(data[point][1] + offset - j)
                if (min_dist == None) or (taxicab_dist < min_dist):
                    closest_point = point
                    min_dist = taxicab_dist
                elif taxicab_dist == min_dist:
                    closest_point = "."
            grid_line.append(closest_point)
        grid.append(grid_line)
    return(grid)

def comptute_areas(grid):
    areas = list()
    for point in range(0,len(data)):
        count = 0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == point:
                    count += 1
        areas.append([point, count])
    return(areas)

areas1 = comptute_areas(compute_grid())
areas2 = comptute_areas(compute_grid(50))

finites = list()
for point in range(0,len(data)):
    if areas1[point][1] == areas2[point][1]:
        finites.append(areas1[point])

finites.sort(key = itemgetter(1), reverse = True)
print(finites[0][1])