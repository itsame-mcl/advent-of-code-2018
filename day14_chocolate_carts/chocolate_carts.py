chocolates = [3, 7]
elf1 = 0
elf2 = 1

target = 765071
while len(chocolates) < (target + 10):
    new_recipes = chocolates[elf1] + chocolates[elf2]
    recipe1 = new_recipes // 10
    recipe2 = new_recipes % 10
    if recipe1 > 0:
        chocolates.append(recipe1)
    chocolates.append(recipe2)
    elf1 = (elf1 + 1 + chocolates[elf1]) % len(chocolates)
    elf2 = (elf2 + 1 + chocolates[elf2]) % len(chocolates)

print(chocolates[-10:])