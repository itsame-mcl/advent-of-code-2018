import os

stars = list()
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    for line in f:
        line_data = line.replace("\n","").split(",")
        stars.append((int(line_data[0]), int(line_data[1]), int(line_data[2]), int(line_data[3])))

def manhattan_distance(coords1, coords2):
    return abs(coords1[0] - coords2[0]) + abs(coords1[1] - coords2[1]) + abs(coords1[2] - coords2[2]) + abs(coords1[3] - coords2[3])

consts = list()
while len(stars) > 0:
    const = list()
    to_scan = [stars.pop(0)]
    while len(to_scan) > 0:
        scan_this_iter = to_scan.copy()
        for star in scan_this_iter:
            const.append(star)
            candidates = stars.copy()
            for candidate in candidates:
                if manhattan_distance(star, candidate) <= 3:
                    to_scan.append(candidate)
                    stars.remove(candidate)
            to_scan.remove(star)
    consts.append(const)

print(len(consts))