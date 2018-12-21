# Reverse Engineering from Elf asm

halts_on = list()

r1 = 0
continuer = True
while continuer:
    r3 = r1 | 65536
    r1 = 6780005
    while True:
        r1 = (((r1 + (r3 & 255)) & 16777215) * 65899) & 16777215
        if 256 > r3:
            if r1 in halts_on:
                print(halts_on[-1])
                continuer = False
            else:
                halts_on.append(r1)
                break
        else:
            r3 //= 256