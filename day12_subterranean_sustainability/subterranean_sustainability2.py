import os

pots = dict()
patterns = dict()
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    for num, line in enumerate(f, 1):
        if num == 1:
            state = (line.replace("\n","").split(" "))[2]
            pots_lst = list(state.replace("#","1").replace(".","0"))
            for id, initial_pot in enumerate(pots_lst, 0):
                pots[id] = int(initial_pot)
        if num >= 3:
            new_patern = line.replace("\n","").replace("#","1").replace(".","0").split(" => ")
            patterns[int(new_patern[0],2)] = int(new_patern[1],2)

sums = list()
step = 50
converged = False
last_mean = 0
current_gen = 0
while not converged:
    for gen in range(current_gen,current_gen+step):
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
        sums.append(sum_pots)
        current_gen += 1
    new_mean = (sums[current_gen - 1] - sums[current_gen - step]) / (step - 1)
    if new_mean == last_mean:
        converged = True
    last_mean = new_mean
    
final_gen = 50000000000
sum_final = int(sums[-1] + (final_gen - current_gen) * last_mean)
print(sum_final)