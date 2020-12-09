import re

def parse_program(f):
    instructions = []
    for line in f:
        m = re.search(r'(...) ([\+-][0-9]+)', line)
        instructions.append((m.group(1), int(m.group(2))))
    return instructions

with open('day8_input.txt', 'r') as f:
    program = parse_program(f)
    acc = 0
    i = 0
    executed_lines = set()

    while True:
        if i in executed_lines:
            print(acc)
            break
        executed_lines.add(i)
        instruction, value = program[i]
        if instruction == 'acc':
            acc += value
            i += 1
        if instruction == 'jmp':
            i += value
        if instruction == 'nop':
            i += 1


         
        

