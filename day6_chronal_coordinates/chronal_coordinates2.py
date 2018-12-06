import os

data = list()
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    for line in f:
        str_line = line.replace('\n',"").split(",")
        data.append([int(str_line[0]), int(str_line[1])])

max_coord = [0] * 2
max_coord[0] = max(coord[0] for coord in data)
max_coord[1] = max(coord[1] for coord in data)

close_area = 0
for j in range(0,(max_coord[1] + 1)):
    for i in range(0,(max_coord[0] + 1)):
        total_dist = 0
        for point in range(0,len(data)):
            taxicab_dist = abs(data[point][0] - i) + abs(data[point][1] - j)
            total_dist += taxicab_dist
        if total_dist < 10000:
            close_area += 1

print(close_area)