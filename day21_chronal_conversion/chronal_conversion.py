import os

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
    result[params[3]] = int(bool(params[1] > registers[params[2]]))
    return(result)

def gtri(params, registers):
    result = registers[::]
    result[params[3]] = int(bool(registers[params[1]] > params[2]))
    return(result)

def gtrr(params, registers):
    result = registers[::]
    result[params[3]] = int(bool(registers[params[1]] > registers[params[2]]))
    return(result)

# Equality testing

def eqir(params, registers):
    result = registers[::]
    result[params[3]] = int(bool(params[1] == registers[params[2]]))
    return(result)

def eqri(params, registers):
    result = registers[::]
    result[params[3]] = int(bool(registers[params[1]] == params[2]))
    return(result)

def eqrr(params, registers):
    result = registers[::]
    result[params[3]] = int(bool(registers[params[1]] == registers[params[2]]))
    return(result)

registers = [0] * 6
instruction_register = -1
instructions = list()

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    for num, line in enumerate(f, 1):
        inst = line.replace("\n","").split(" ")
        if num == 1:
            instruction_register = int(inst[1])
        else:
            instructions.append([inst[0], int(inst[1]), int(inst[2]), int(inst[3])])

in_bounds = True
instruction_pointer = registers[instruction_register]
while in_bounds:
    if instruction_pointer == 28:
        # Forensics : Halts after instruction 28 if registers[0] == registers[1]
        print(registers[1])
        break
    registers[instruction_register] = instruction_pointer
    registers = globals()[instructions[registers[instruction_register]][0]](instructions[registers[instruction_register]], registers)
    instruction_pointer = registers[instruction_register] + 1
    if instruction_pointer >= len(instructions):
        in_bounds = False