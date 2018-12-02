import os

data = list()
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    for ligne in f:
        data.append(ligne.replace('\n',""))

for item in data:
    char_list = list(item)
    for item2 in data:
        char_list2 = list(item2)
        commons = list()
        divgs = 0
        for i in range(0, len(char_list)):
            if char_list[i] == char_list2[i]:
                commons.append(char_list[i])
            else:
                divgs += 1
        if divgs == 1:
            print(''.join(commons))