import os

data = list()
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    for ligne in f:
        data.append(ligne.replace('\n',""))

doubles = 0
triples = 0
for item in data:
    char_list = list(item)
    char_set = set(char_list)
    char_count = list()
    for char in char_set:
        char_count.append(char_list.count(char))
    if char_count.count(2) > 0:
        doubles += 1
    if char_count.count(3) > 0:
        triples += 1

print(doubles*triples)