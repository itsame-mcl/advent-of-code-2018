import networkx

maze = dict()
depth = 6969
target = (9,796)

stuffs = [0,1,2]

for y in range(0,target[1] + 101):
    for x in range(0,target[0] + 101):
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

graph = networkx.Graph()
for y in range(0,target[1] + 101):
    for x in range(0,target[0] + 101):
        current_type = maze.get((x,y))
        valid_stuffs = stuffs.copy()
        valid_stuffs.remove(current_type)
        graph.add_edge((x, y, valid_stuffs[0]), (x, y, valid_stuffs[1]), weight=7)
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            target_x, target_y = x+dx, y+dy
            target_type = maze.get((target_x, target_y), -1)
            if target_type >= 0:
                target_valid_stuffs = stuffs.copy()
                target_valid_stuffs.remove(target_type)
                for item in set(valid_stuffs).intersection(set(target_valid_stuffs)):
                    graph.add_edge((x, y, item), (target_x, target_y, item), weight=1)
        
answer = networkx.dijkstra_path_length(graph, (0, 0, 1), (target[0], target[1], 1))
print(answer)