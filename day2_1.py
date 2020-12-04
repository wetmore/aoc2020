import re

count = 0
regex = r"(\d+)-(\d+) ([a-z]): ([a-z]+)"

def valid(line):
    match = re.search(regex, line)
    lb =int(match.group(1))
    ub = int(match.group(2))
    letter = match.group(3)
    password = match.group(4)

    num_occurences = password.count(letter)
    return num_occurences <= ub and num_occurences >= lb

with open('day2_1_input.txt', 'r') as f:
    for line in f:
        if valid(line):
            count += 1

print(count)

