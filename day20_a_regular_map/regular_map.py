import os

regex = ""
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
   for line in f:
        regex = line.replace("\n","").replace("^","").replace("$","")

rooms = set()
doors = set()

start_position = (0,0)
walkers = [start_position]
stack = list()
sub_start, sub_end = [start_position], set()

rooms.add(start_position)
for char in regex:
    if char == "N":
        for i, walker in enumerate(walkers):
            go_to = (walker[0], walker[1] + 1)
            doors.add((walker, go_to))
            rooms.add(go_to)
            walkers[i] = go_to
    elif char == "S":
        for i, walker in enumerate(walkers):
            go_to = (walker[0], walker[1] - 1)
            doors.add((go_to, walker))
            rooms.add(go_to)
            walkers[i] = go_to
    elif char == "E":
        for i, walker in enumerate(walkers):
            go_to = (walker[0] + 1, walker[1])
            doors.add((walker, go_to))
            rooms.add(go_to)
            walkers[i] = go_to
    elif char == "W":
        for i, walker in enumerate(walkers):
            go_to = (walker[0] - 1, walker[1])
            doors.add((go_to, walker))
            rooms.add(go_to)
            walkers[i] = go_to
    elif char == "(":
        stack.append((sub_start, sub_end))
        sub_start, sub_end = walkers.copy(), set()
    elif char == "|":
        for walker in walkers:
            sub_end.add(walker)
        walkers = sub_start.copy()
    elif char == ")":
        for walker in walkers:
            sub_end.add(walker)
        walkers = list(sub_end).copy()
        sub_start, sub_end = stack.pop()
        

print(rooms)