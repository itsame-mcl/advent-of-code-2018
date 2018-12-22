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

risk_level = 0
for erosion_level in maze.values():
    risk_level = risk_level + (erosion_level % 3)

print(risk_level)