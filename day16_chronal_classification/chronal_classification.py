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
count = 0

for sample in samples:
    match = 0
    for fun in funs:
        try:
            result = fun(sample[0], sample[1])
        except Exception:
            pass
        else:
            if result == sample[2]:
                match += 1
    if match >= 3:
        count += 1

print(count)