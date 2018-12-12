import os

pots = dict()
tmp_patterns = dict()
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    for num, line in enumerate(f, 1):
        if num == 1:
            state = (line.replace("\n","").split(" "))[2]
            pots_lst = list(state.replace("#","1").replace(".","0"))
            for id, initial_pot in enumerate(pots_lst, 0):
                pots[id] = int(initial_pot)
        if num >= 3:
            new_patern = line.replace("\n","").replace("#","1").replace(".","0").split(" => ")
            tmp_patterns[int(new_patern[0],2)] = int(new_patern[1],2)

patterns = [0] * len(tmp_patterns)
for key, value in tmp_patterns.items():
    patterns[key] = value

sums = [0] * 1000
for gen in range(0,1000):
    next_gen = dict()
    for pot in range(min(pots)-2, max(pots)+3):
        pattern = pots.get(pot-2,0)*16 + pots.get(pot-1,0)*8 + pots.get(pot,0)*4 + pots.get(pot+1,0)*2 + pots.get(pot+2,0)
        next_gen[pot] = patterns[pattern]
    if next_gen.get(min(pots)-2,0) == 0:
        del next_gen[min(pots)-2]
    if next_gen.get(min(pots)-2,0) + next_gen.get(min(pots)-1,0) == 0:
        del next_gen[min(pots)-1]
    if next_gen.get(max(pots)+1,0) + next_gen.get(max(pots)+2,0) == 0:
        del next_gen[max(pots)+1]
    if next_gen.get(min(pots)+2,0) == 0:
        del next_gen[min(pots)+2]
    pots = next_gen
    sum_pots = 0
    for key, value in pots.items():
        if value == 1:
            sum_pots += key
    sums[gen] = sum_pots

sum_final = sums[999] + 49999999000 * (sums[999] - sums[998])
print(sum_final)