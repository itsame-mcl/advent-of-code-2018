import os

clay = set()
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    for raw_line in f:
        line = raw_line.split(", ")
        first_coord = line[0].split("=")
        second_coord = line[1].split("=")
        min_x = -1
        max_x = -1
        min_y = -1
        max_y = -1
        if first_coord[0] == "x":
            min_x = int(first_coord[1])
            max_x = int(first_coord[1])
            y_split = second_coord[1].split("..")
            min_y = int(y_split[0])
            max_y = int(y_split[1])
        elif first_coord[0] == "y":
            min_y = int(first_coord[1])
            max_y = int(first_coord[1])
            x_split = second_coord[1].split("..")
            min_x = int(x_split[0])
            max_x = int(x_split[1])
        for x in range(min_x,max_x + 1):
            for y in range(min_y,max_y+1):
                    clay.add((x,y))

ymin, ymax = min(clay, key=lambda square: square[1])[1], max(clay, key=lambda square: square[1])[1]

settled = set()
flowing = set()

def fill(square, direction="below"):
    flowing.add(square)

    below = (square[0], square[1] + 1)
    if (below not in clay) and (below not in flowing) and (ymin <= below[1] <= ymax):
        fill(below)
    if (below not in clay) and (below not in settled):
        return False

    left = (square[0] - 1, square[1])
    left_filled = (left in clay) or (left not in flowing) and fill(left, direction="left")

    right = (square[0] + 1, square[1])
    right_filled = (right in clay) or (right not in flowing) and fill(right, direction="right")

    if direction == "below" and left_filled and right_filled:
        settled.add(square)
        while left in flowing:
            settled.add(left)
            left = (left[0] - 1, left[1])
        while right in flowing:
            settled.add(right)
            right = (right[0] + 1, right[1])

    return (direction == "left") and (left_filled or (left in clay)) or (direction == "right") and (right_filled or (right in clay))

fill((500, ymin))
print(len([pt for pt in flowing | settled if ymin <= pt[1] <= ymax]))
print(len([pt for pt in settled if ymin <= pt[1] <= ymax]))

# Version based on sciyoshi : https://www.reddit.com/r/adventofcode/comments/a6wpup/2018_day_17_solutions/ebyq6mj