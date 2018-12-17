import os
from operator import itemgetter

clay = list()
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    for raw_line in f:
        line = raw_line.split(", ")
        first_coord = line[0].split("=")
        second_coord = line[1].split("=")
        min_x = -1
        max_x = -1
        min_y = -1
        max_y = -1
        if first_coord[0] == "x":
            min_x = int(first_coord[1])
            max_x = int(first_coord[1])
            y_split = second_coord[1].split("..")
            min_y = int(y_split[0])
            max_y = int(y_split[1])
        elif first_coord[0] == "y":
            min_y = int(first_coord[1])
            max_y = int(first_coord[1])
            x_split = second_coord[1].split("..")
            min_x = int(x_split[0])
            max_x = int(x_split[1])
        for x in range(min_x,max_x + 1):
            for y in range(min_y,max_y+1):
                if ((x,y) not in clay):
                    clay.append((x,y))

min_search = min([square[1] for square in clay])
max_search = max([square[1] for square in clay])

x_clay = dict()
for y in range(min_search, max_search+1):
    y_clay = [square[0] for square in clay if square[1] == y]
    y_clay.sort()
    x_clay[y] = y_clay

clay = set(clay)
water = set()
water.add((500,min_search))
rest = set()
loop = True
while loop:
    scan = water.copy()
    min_y = -1
    for square in scan:
        below = (square[0], square[1] + 1)
        if (below not in clay) and (below not in rest) and (below not in water):
            water.add(below)
            if (below[1] < min_y) or (min_y == -1):
                min_y = below[1]
        elif (below in clay) or (below in rest):
            left = (square[0] - 1, square[1])
            if (left not in clay) and (left not in rest) and (left not in water):
                water.add(left)
                if (left[1] < min_y) or (min_y == -1):
                    min_y = left[1]
            right = (square[0] + 1, square[1])
            if (right not in clay) and (right not in rest) and (right not in water):
                water.add(right)
                if (right[1] < min_y) or (right == -1):
                    min_y = right[1]
    for y in range(min_search, max_search+1):
        y_clay = x_clay[y]
        x_water = {square[0] for square in water if square[1] == y}
        if(len(x_water) > 0):
            if(len(y_clay) > 1):
                for i in range(0,len(y_clay)-1):
                    interval_full = True
                    interval = set(range(y_clay[i] + 1,y_clay[i+1]))
                    if interval.issubset(x_water):
                        for x in interval:
                            rest.add((x,y))
                            water.remove((x,y))
    print(min_y)
    if min_y > max_search:
        loop = False

scope_water = [square for square in water if square[1] >= min_search and square[1] <= max_search]
solve = len(scope_water) + len(rest)
print(solve)