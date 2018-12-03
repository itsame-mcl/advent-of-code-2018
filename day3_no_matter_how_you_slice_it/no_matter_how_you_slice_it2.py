import os

data = list()
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    for ligne in f:
        data.append(ligne.replace('\n',"").replace('@',"").replace(':',"").replace('#',"").split(" "))

grid = [[0 for i in range(1000)] for j in range(1000)]

for claim in data:
    topleft_coords = claim[2].split(",")
    size = claim[3].split("x")
    for i in range(int(topleft_coords[0]),int(topleft_coords[0])+int(size[0])):
        for j in range(int(topleft_coords[1]),int(topleft_coords[1])+int(size[1])):
            if grid[i][j] == 0:
                grid[i][j] = int(claim[0])
            else:
                grid[i][j] = -1

unique_claims = list()
for i in range(0,1000):
    for j in range(0,1000):
        if (grid[i][j] > 0):
            unique_claims.append(grid[i][j])

claims_to_check = set(unique_claims)
for claim in claims_to_check:
    expected_size = data[claim-1][3].split("x")
    expected_area = int(expected_size[0]) * int(expected_size[1])
    valid_area = unique_claims.count(claim)
    if valid_area == expected_area:
        print(claim)
        break