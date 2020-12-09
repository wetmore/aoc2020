total= 0

with open('day6_input.txt', 'r') as f:
    questions = set()
    for line in f:
        if line == '\n':
            total += len(questions)
            questions = set()
        else:
            for c in line.strip():
                questions.add(c)
    total += len(questions)

            
print(total)

