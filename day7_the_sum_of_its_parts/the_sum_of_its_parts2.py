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

workers = [0] * 5
workers_steps = ["."] * 5
seconds = 0
while len(graph) > 0 or sum(workers) > 0:
    for i in range(0,5):
        if workers[i] == 0:
            if (workers_steps[i] != "."):
                for step in graph:
                    try:
                        step[1].remove(workers_steps[i])
                    except ValueError:
                        pass
            selected_step = list()
            for step in graph:
                if len(step[1]) == 0:
                    selected_step = step
                    break
            if selected_step:
                workers[i] += 60 + steps.index(selected_step[0])
                workers_steps[i] = selected_step[0]
                graph.remove(selected_step)
            else:
                workers_steps[i] = "."
        else:
            workers[i] -= 1
    seconds += 1

print(seconds)