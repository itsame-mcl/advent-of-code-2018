import os
import networkx

regex = ""
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
   for line in f:
        regex = line.replace("\n","").replace("^","").replace("$","")

facility = networkx.Graph()

start_position = 0
walkers = [start_position]
stack = list()
sub_start, sub_end = [start_position], set()

for char in regex:
    if char == "N":
        for i, walker in enumerate(walkers):
            go_to = walker + 1j
            facility.add_edge(walker, go_to)
            walkers[i] = go_to
    elif char == "S":
        for i, walker in enumerate(walkers):
            go_to = walker - 1j
            facility.add_edge(walker, go_to)
            walkers[i] = go_to
    elif char == "E":
        for i, walker in enumerate(walkers):
            go_to = walker + 1
            facility.add_edge(walker, go_to)
            walkers[i] = go_to
    elif char == "W":
        for i, walker in enumerate(walkers):
            go_to = walker - 1
            facility.add_edge(walker, go_to)
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
        
lengths = networkx.algorithms.shortest_path_length(facility, 0)
print(max(lengths.values()))
print(sum(1 for length in lengths.values() if length >= 1000))