import os

rawdata = list()
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    for ligne in f:
        rawdata.append(ligne.replace('\n',""))

frequence = 0
for line in rawdata:
    signe = line[0]
    valeur = int(line[1:])
    if signe == "+":
        frequence += valeur
    elif signe == "-":
        frequence -= valeur

print(frequence)