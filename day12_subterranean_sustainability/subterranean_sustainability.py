import os

pots = dict()
patterns = dict()
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    for num, line in enumerate(f, 1):
        if num == 1:
            state = list((line.replace("\n","").split(" "))[2])
            for id, initial_pot in enumerate(state, 0):
                pots[id] = initial_pot
        if num >= 3:
            new_patern = line.replace("\n","").split(" => ")
            patterns[new_patern[0]] = new_patern[1]

for gen in range(0,20):
    next_gen = dict()
    for pot in range(min(pots)-2, max(pots)+2):
        pattern = ""
        for i in range((pot-2),(pot+3)):            
            if i in pots:
                pattern += pots[i]
            else:
                pattern += "."
        next_gen[pot] = patterns[pattern]
    pots = next_gen

sum_pots = 0
for key, value in pots.items():
    if value == "#":
        sum_pots += key

print(sum_pots)