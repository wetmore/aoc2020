total= 0

def score(questions, responses):
    total = 0
    for key in questions:
        if questions[key] == responses:
            total += 1
    return total


with open('day6_input.txt', 'r') as f:
    questions = {}
    responses = 0
    for line in f:
        if line == '\n':
            total += score(questions, responses)
            responses = 0
            questions = {}
        else:
            for c in line.strip():
                if c not in questions:
                    questions[c] = 0
                questions[c] += 1
            responses += 1
    total += score(questions, responses)

            
print(total)

