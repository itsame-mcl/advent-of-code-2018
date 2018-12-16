import os

samples = list()
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    sample = [0] * 3
    for num, line in enumerate(f, 1):
        if (num%4) == 1 or (num%4) == 3:
            register = line.replace("\n","").replace(",","").replace("[","").replace("]","").split(" ")
            if (num%4) == 1:
                sample[1] = [int(register[1]), int(register[2]), int(register[3]), int(register[4])]
            elif (num%4) == 3:
                sample[2] = [int(register[2]), int(register[3]), int(register[4]), int(register[5])]
                samples.append(sample)
                sample = [0] * 3
        elif (num%4) == 2:
            op = line.replace("\n","").split(" ")
            sample[0] = [int(op[0]), int(op[1]), int(op[2]), int(op[3])]

prog = list()
with open(os.path.join(os.path.dirname(__file__), 'input2.txt'), "r", encoding="utf8") as f:
    for line in f:
        instr = line.replace("\n","").split(" ")
        prog.append([int(instr[0]), int(instr[1]), int(instr[2]), int(instr[3])])

# Addition

def addr(params, registers):
    result = registers[::]
    result[params[3]] = registers[params[1]] + registers[params[2]]
    return(result)

def addi(params, registers):
    result = registers[::]
    result[params[3]] = registers[params[1]] + params[2]
    return(result)

# Multiplication

def mulr(params, registers):
    result = registers[::]
    result[params[3]] = registers[params[1]] * registers[params[2]]
    return(result)

def muli(params, registers):
    result = registers[::]
    result[params[3]] = registers[params[1]] * params[2]
    return(result)

# Bitwise AND

def banr(params, registers):
    result = registers[::]
    result[params[3]] = registers[params[1]] & registers[params[2]]
    return(result)

def bani(params, registers):
    result = registers[::]
    result[params[3]] = registers[params[1]] & params[2]
    return(result)

# Bitwise OR

def borr(params, registers):
    result = registers[::]
    result[params[3]] = registers[params[1]] | registers[params[2]]
    return(result)

def bori(params, registers):
    result = registers[::]
    result[params[3]] = registers[params[1]] | params[2]
    return(result)

# Assignment

def setr(params, registers):
    result = registers[::]
    result[params[3]] = registers[params[1]]
    return(result)

def seti(params, registers):
    result = registers[::]
    result[params[3]] = params[1]
    return(result)

# Greater-than testing

def gtir(params, registers):
    result = registers[::]
    result[params[3]] = bool(params[1] > registers[params[2]])
    return(result)

def gtri(params, registers):
    result = registers[::]
    result[params[3]] = bool(registers[params[1]] > params[2])
    return(result)

def gtrr(params, registers):
    result = registers[::]
    result[params[3]] = bool(registers[params[1]] > registers[params[2]])
    return(result)

# Equality testing

def eqir(params, registers):
    result = registers[::]
    result[params[3]] = bool(params[1] == registers[params[2]])
    return(result)

def eqri(params, registers):
    result = registers[::]
    result[params[3]] = bool(registers[params[1]] == params[2])
    return(result)

def eqrr(params, registers):
    result = registers[::]
    result[params[3]] = bool(registers[params[1]] == registers[params[2]])
    return(result)

funs = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
match = [funs] * 16

max_len = 16
while max_len > 1:
    for sample in samples:
        inst = sample[0][0]
        for fun in match[inst]:
            try:
                result = fun(sample[0], sample[1])
            except Exception:
                match[inst] = [func for func in match[inst] if not(func == fun)]
            else:
                if result == sample[2]:
                    pass
                else:
                    match[inst] = [func for func in match[inst] if not(func == fun)]
    for j in range(0,16):
        if len(match[j]) == 1:
            unique = match[j][0]
            for k in range(0,16):
                if k != j:
                    match[k] = [func for func in match[k] if not(func == unique)]
    max_len = 0
    for l in range(0,16):
        if len(match[l]) > max_len:
            max_len = len(match[l])

registers = [0, 0, 0, 0]
for inst in prog:
    registers = match[inst[0]][0](inst, registers)
print(registers[0])