serial = 8141

grid = list()
for x in range(1, 301):
    for y in range(1, 301):
        rackID = x + 10
        power = ((rackID * y) + serial) * rackID
        power = int((power / 100) % 10) - 5
        grid.append([x, y, power])

best_square = [0] * 2
best_power = 0
for x in range(1, 299):
    for y in range(1, 299):
        square_power = sum([rack[2] for rack in grid if ((rack[0] >= x) and (rack[0] <= x + 2) and (rack[1] >= y) and (rack[1] <= y + 2))])
        if square_power > best_power:
            best_square = [x, y]
            best_power = square_power

print(best_square)