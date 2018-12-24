# Group ID, Army, Units, HP, Initiative, Bludgeoning, Cold, Fire, Radiation, Slashing, Attack Type, Attack Power
boost = 42
immune_wins = False
while not immune_wins:
    groups = [["M1","Immune",2749,8712,18,1,0,2,0,1,8,30+boost],
              ["M2","Immune",704,1890,17,1,1,1,1,1,7,26+boost],
              ["M3","Immune",1466,7198,6,0,2,1,1,2,5,44+boost],
              ["M4","Immune",6779,11207,4,1,1,1,1,1,6,13+boost],
              ["M5","Immune",1275,11747,2,1,1,1,1,1,6,66+boost],
              ["M6","Immune",947,5442,3,1,1,1,1,1,8,49+boost],
              ["M7","Immune",4319,2144,9,2,1,2,1,1,7,4+boost],
              ["M8","Immune",6315,5705,16,1,1,1,1,1,6,7+boost],
              ["M9","Immune",8790,10312,5,1,1,1,1,1,7,10+boost],
              ["M10","Immune",3242,4188,14,1,2,1,0,1,5,11+boost],
              ["F1","Infection",1230,11944,1,1,2,1,1,1,5,17],
              ["F2","Infection",7588,53223,12,0,1,1,1,1,6,13],
              ["F3","Infection",1887,40790,15,1,0,1,0,0,7,43],
              ["F4","Infection",285,8703,7,1,1,1,1,0,9,60],
              ["F5","Infection",1505,29297,8,1,1,1,1,1,7,38],
              ["F6","Infection",191,24260,20,0,1,1,1,2,6,173],
              ["F7","Infection",1854,12648,13,1,2,2,1,1,5,13],
              ["F8","Infection",1541,49751,19,2,2,1,1,1,9,62],
              ["F9","Infection",3270,22736,10,1,1,1,1,1,9,13],
              ["F10","Infection",1211,56258,11,1,0,1,1,0,5,73]]

    Fight = True
    winner = ""
    units = 0
    while Fight:
        # Target Selection
        groups.sort(key=lambda x: (-x[2]*x[11], -x[4]))
        avaliable_targets = groups.copy()
        fights = []
        for group in groups:
            potential_targets = [target for target in avaliable_targets if target[1] != group[1]]
            if len(potential_targets) > 0:
                effective_power = group[2]*group[3]
                potential_targets.sort(key=lambda y: (-y[group[10]], -y[2]*y[11], -y[4]))
                if potential_targets[0][group[10]] >= 1:
                    fights.append((group[4],group[0],potential_targets[0][0]))
                    avaliable_targets.remove(potential_targets[0])
        # Attack
        fights.sort(key = lambda z: -z[0])
        for fight in fights:
            atqs = groups.index([group for group in groups if group[0] == fight[1]][0])
            defs = groups.index([group for group in groups if group[0] == fight[2]][0])
            if groups[atqs][2] > 0:
                damages = groups[atqs][2]*groups[atqs][11]*groups[defs][groups[atqs][10]]
                killed = damages // groups[defs][3]
                groups[defs][2] = groups[defs][2] - killed
        # Clean
        groups = [group for group in groups if group[2] > 0]
        alives = list(set([group[1] for group in groups]))
        if len(alives) == 1:
            Fight = False
            winner = alives[0]
            units = sum([group[2] for group in groups])
    if winner == "Immune":
        immune_wins = True
        print(units)
    else:
        boost = boost + 1