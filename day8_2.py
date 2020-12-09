import re

def parse_program(f):
    instructions = []
    for line in f:
        m = re.search(r'(...) ([\+-][0-9]+)', line)
        instructions.append((m.group(1), int(m.group(2))))
    return instructions

def terminates(program):
    acc = 0
    i = 0
    executed_lines = set()

    while True:
        if i == len(program):
            return acc
        if i in executed_lines:
            return None
        executed_lines.add(i)
        instruction, value = program[i]
        if instruction == 'acc':
            acc += value
            i += 1
        if instruction == 'jmp':
            i += value
        if instruction == 'nop':
            i += 1

def tweaked_programs(program):
    for i in range(len(program)):
        instruction, value = program[i]
        if instruction == 'jmp':
            tweaked_program = program.copy()
            tweaked_program[i] = ('nop', value)
            yield tweaked_program
        if instruction == 'nop':
            tweaked_program = program.copy()
            tweaked_program[i] = ('jmp', value)
            yield tweaked_program

with open('day8_input.txt', 'r') as f:
    program = parse_program(f)
    evaluations = map(terminates, tweaked_programs(program))
    print(next(filter(lambda x: x is not None, evaluations)))


         
        

