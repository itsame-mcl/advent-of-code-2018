chocolates = [3,7]
elf1 = 0
elf2 = 1

pattern = [7,6,5,0,7,1]
location = -1

while location < 0:
    new_recipes = chocolates[elf1] + chocolates[elf2]
    recipe1 = new_recipes // 10
    recipe2 = new_recipes % 10
    if recipe1 > 0:
        chocolates.append(recipe1)
    chocolates.append(recipe2)
    elf1 = (elf1 + 1 + chocolates[elf1]) % len(chocolates)
    elf2 = (elf2 + 1 + chocolates[elf2]) % len(chocolates)
    if len(chocolates) > len(pattern):
        if chocolates[-(len(pattern) + 1):-1] == pattern:
            location = len(chocolates) - (len(pattern) + 1)
        elif chocolates[-len(pattern):] == pattern:
            location = len(chocolates) - len(pattern)
        else:
            location = -1
    else:
        location = -1

print(location)