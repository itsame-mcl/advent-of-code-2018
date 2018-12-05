import os

data = list()
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    for line in f:
        data = list(line.replace('\n',""))

best_polymer_len = len(data)
polymer_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for poly in polymer_list:
    reduced_poly = list(filter(lambda p: p != poly and p != str.upper(poly), data))
    polymer_len = len(reduced_poly)
    while True:
        for i in range(1,len(reduced_poly)):
            if (str.lower(reduced_poly[i-1]) == str.lower(reduced_poly[i])) and (reduced_poly[i-1] != " "):
                if (str.isupper(reduced_poly[i-1]) and str.islower(reduced_poly[i])) or (str.isupper(reduced_poly[i]) and str.islower(reduced_poly[i-1])):
                    reduced_poly[i-1] = ""
                    reduced_poly[i] = ""
        reduced_poly = list(filter(None, reduced_poly))
        if len(reduced_poly) == polymer_len:
            break
        else:
            polymer_len = len(reduced_poly)
    if polymer_len < best_polymer_len:
        best_polymer_len = polymer_len

print(best_polymer_len)