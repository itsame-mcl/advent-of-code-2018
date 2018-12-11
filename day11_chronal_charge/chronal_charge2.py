import numpy as np
serial = 8141

tanks = list()
for y in range(1, 301):
    for x in range(1, 301):
        rackID = x + 10
        power = ((rackID * y) + serial) * rackID
        power = int((power / 100) % 10) - 5
        tanks.append(power)

grid = np.reshape(tanks, (300,300))

best_square = [0] * 2
best_power = 0
for size in range(1,301):
    for i in range(0,301-size):
        for j in range(0,301-size):
            square_power = np.sum(grid[i:i+size,j:j+size])
            if square_power > best_power:
                    best_square = [(j+1), (i+1), size]
                    best_power = square_power

print(best_square)