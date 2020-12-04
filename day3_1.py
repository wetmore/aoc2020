count = 0
x = 0

with open('day3_input.txt', 'r') as f:
    for line in f:
        char = line[x % (len(line) - 1)]
        print(char)
        if char == '#':
            count += 1
        x += 3

print(count)

