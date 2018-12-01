import os

rawdata = list()
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    for ligne in f:
        rawdata.append(ligne.replace('\n',""))

frequence = 0
valeurs = list()
index = 0

while True:
    if frequence in valeurs:
        print(frequence)
        break
    else:
        valeurs.append(frequence)
    signe = rawdata[index][0]
    valeur = int(rawdata[index][1:])
    if signe == "+":
        frequence += valeur
    elif signe == "-":
        frequence -= valeur
    index += 1
    if index == len(rawdata):
        index = 0