import os

data = list()
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    for line in f:
        data = list(line.replace('\n',""))

polymer_len = len(data)
while True:
    for i in range(1,len(data)):
        if (str.lower(data[i-1]) == str.lower(data[i])) and (data[i-1] != " "):
            if (str.isupper(data[i-1]) and str.islower(data[i])) or (str.isupper(data[i]) and str.islower(data[i-1])):
                data[i-1] = ""
                data[i] = ""
    data = list(filter(None, data))
    if len(data) == polymer_len:
        print(polymer_len)
        break
    else:
        polymer_len = len(data)