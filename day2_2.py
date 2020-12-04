import re

count = 0
regex = r"(\d+)-(\d+) ([a-z]): ([a-z]+)"

def valid(line):
    match = re.search(regex, line)
    i = int(match.group(1))
    j = int(match.group(2))
    letter = match.group(3)
    password = match.group(4)
    
    return bool(password[i-1] == letter) ^ bool(password[j-1] == letter)    


with open('day2_1_input.txt', 'r') as f:
    for line in f:
        if valid(line):
            count += 1

print(count)

