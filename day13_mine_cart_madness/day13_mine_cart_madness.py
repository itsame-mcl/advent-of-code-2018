import os
import operator

grid = list()
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    for line in f:
        grid.append(list(line.replace("\n","")))

vehicles = list()
next_vehicle = 0

for y, line in enumerate(grid):
    for x, square in enumerate(line):
        if grid[y][x] == "^":
            vehicles.append([next_vehicle,x+y*1j,-1j,0])
            next_vehicle += 1
            grid[y][x] = "|"
        elif grid[y][x] == ">":
            vehicles.append([next_vehicle,x+y*1j,1,0])
            next_vehicle += 1
            grid[y][x] = "-"
        elif grid[y][x] == "v":
            vehicles.append([next_vehicle,x+y*1j,+1j,0])
            next_vehicle += 1
            grid[y][x] = "|"
        elif grid[y][x] == "<":
            vehicles.append([next_vehicle,x+y*1j,-1,0])
            next_vehicle += 1
            grid[y][x] = "-"

collision = False
while not collision:
    vehicles = sorted(vehicles, key = lambda x: (x[1].imag, x[1].real))
    for vehicle in vehicles:
        vehicle[1] = vehicle[1] + vehicle[2]
        for other in vehicles:
            if other[0] != vehicle[0]:
                if (vehicle[1] == other[1]):
                    collision = True
                    print([int(vehicle[1].real),int(vehicle[1].imag)])
                    break
        new_square = grid[int(vehicle[1].imag)][int(vehicle[1].real)]
        if new_square == "/":
            if vehicle[2].real == 0:
                vehicle[2] = vehicle[2] * 1j
            else:
                vehicle[2] = vehicle[2] * -1j
        elif new_square == "\\":
            if vehicle[2].real == 0:
                vehicle[2] = vehicle[2] * -1j
            else:
                vehicle[2] = vehicle[2] * 1j
        elif new_square == "+":
            if vehicle[3] == 0:
                vehicle[2] = vehicle[2] * -1j
                vehicle[3] = 1
            elif vehicle[3] == 1:
                vehicle[3] = 2
            elif vehicle[3] == 2:
                vehicle[2] = vehicle[2] * 1j
                vehicle[3] = 0
        elif new_square == " ":
            raise IndexError("Off Road Vehicle")