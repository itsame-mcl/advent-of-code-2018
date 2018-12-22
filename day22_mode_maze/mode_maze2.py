maze = dict()
depth = 6969
target = (9,796)

for y in range(0,target[1]+1):
    for x in range(0,target[0]+1):
        if x == 0 and y == 0:
            geologic_index = 0
        elif x == target[0] and y == target[1]:
            geologic_index = 0
        elif y == 0:
            geologic_index = x * 16807
        elif x == 0:
            geologic_index = y * 48271
        else:
            geologic_index = maze[(x-1,y)] * maze[(x,y-1)]
        erosion_level = (geologic_index + depth) % 20183
        maze[(x,y)] = erosion_level

for square, erosion_level in maze.items():
    maze[square] = (erosion_level % 3)

walkers = list()
minutes = list()
walkers.append([(0,0),(-1,-1),1,0])

for i in range(10000):
    moving = walkers[::]
    for walker in moving:
        if walker[0] == target:
            if walker[2] == 1:
                minutes.append(walker[3])
            else:
                minutes.append(walker[3] + 7)
        else:
            type_current = maze.get(walker[0], -1)
            move_up = (walker[0][0], walker[0][1] - 1)
            type_up = maze.get(move_up, -1)
            if (move_up != walker[1]) and type_up >= 0:
                if type_up != walker[2]:
                    walker_up = [move_up, walker[0], walker[2], walker[3] + 1]
                else:
                    stuff = [0,1,2]
                    stuff.remove(type_current)
                    stuff.remove(type_up)
                    walker_up = [move_up, walker[0], stuff[0], walker[3] + 8]
                walkers.append(walker_up)
            move_down = (walker[0][0], walker[0][1] + 1)
            type_down = maze.get(move_down, -1)
            if (move_down != walker[1]) and type_down >= 0:
                if type_down != walker[2]:
                    walker_down = [move_down, walker[0], walker[2], walker[3] + 1]
                else:
                    stuff = [0,1,2]
                    stuff.remove(type_current)
                    stuff.remove(type_down)
                    walker_down = [move_down, walker[0], stuff[0], walker[3] + 8]
                walkers.append(walker_down)
            move_left = (walker[0][0] - 1, walker[0][1])
            type_left = maze.get(move_left, -1)
            if (move_left != walker[1]) and type_left >= 0:
                if type_left != walker[2]:
                    walker_left = [move_left, walker[0], walker[2], walker[3] + 1]
                else:
                    stuff = [0,1,2]
                    stuff.remove(type_current)
                    stuff.remove(type_left)
                    walker_left = [move_left, walker[0], stuff[0], walker[3] + 8]
                walkers.append(walker_left)
            move_right = (walker[0][0] + 1, walker[0][1])
            type_right = maze.get(move_right, -1)
            if (move_right != walker[1]) and type_right >= 0:
                if type_right != walker[2]:
                    walker_right = [move_right, walker[0], walker[2], walker[3] + 1]
                else:
                    stuff = [0,1,2]
                    stuff.remove(type_current)
                    stuff.remove(type_right)
                    walker_right = [move_right, walker[0], stuff[0], walker[3] + 8]
                walkers.append(walker_right)
        walkers.remove(walker)
        
print(min(minutes))