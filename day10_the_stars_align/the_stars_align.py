import os
import statistics

data = list()
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    for line in f:
        point = line.replace('\n',"").replace(' ',"").split("<")
        position = (point[1].split(">"))[0].split(",")
        position[0] = int(position[0])
        position[1] = int(position[1])
        velocity = point[2].replace(">","").split(",")
        velocity[0] = int(velocity[0])
        velocity[1] = int(velocity[1])
        data.append([position, velocity])

def calc_mstd(data):
    std0 = statistics.stdev(point[0][0] for point in data)
    std1 = statistics.stdev(point[0][1] for point in data)
    mstd = statistics.mean([std0, std1])
    return(mstd)

def apply_velocity(data):
    for point in data:
        point[0][0] = point[0][0] + point[1][0]
        point[0][1] = point[0][1] + point[1][1]

def display_points(data):
    limsx = [min(point[0][0] for point in data), max(point[0][0] for point in data)]
    limsy = [min(point[0][1] for point in data), max(point[0][1] for point in data)]
    display = ""
    for y in range(limsy[0], limsy[1] + 1):
        for x in range(limsx[0], limsx[1] + 1):
            found = False
            for point in data:
                if [point[0][0], point[0][1]] == [x,y]:
                    found = True
            if found:
                display = display + "#"
            else:
                display = display + "."
        display = display + "\n"
    return(display)

mstd0 = calc_mstd(data)
last_mstd = mstd0
desc = True

while desc:
    apply_velocity(data)
    new_mstd = calc_mstd(data)
    if new_mstd < 40:
        print(display_points(data))
    if new_mstd > last_mstd:
        desc = False
    else:
        last_mstd = new_mstd