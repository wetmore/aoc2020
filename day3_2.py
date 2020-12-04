lines = []

with open('day3_input.txt', 'r') as f:
    for line in f:
        lines.append(line)

def slope(right, down):
    x = 0
    y = 0
    count = 0
    while y < len(lines):
        line = lines[y]
        char = line[x % (len(line) - 1)]
        if char == '#':
            count += 1
        x += right
        y += down
    return count

answer = slope(1,1)*slope(3,1)*slope(5,1)*slope(7,1)*slope(1, 2)
print(answer)
