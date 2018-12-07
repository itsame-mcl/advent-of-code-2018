import os
import string

data = list()
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    for line in f:
        line_splitted = line.replace('\n',"").split(" ")
        data.append([line_splitted[1],line_splitted[7]])

steps = list(string.ascii_uppercase)

graph = list()
for step in steps:
    prereq = list()
    for instruction in data:
        if instruction[1] == step:
            prereq.append(instruction[0])
    graph.append([step,prereq])

pattern = ""
while len(graph) > 0:
    selected_step = list()
    for step in graph:
        if len(step[1]) == 0:
            selected_step = step
            break
    pattern += selected_step[0]
    graph.remove(selected_step)
    for step in graph:
        try:
            step[1].remove(selected_step[0])
        except ValueError:
            pass

print(pattern)