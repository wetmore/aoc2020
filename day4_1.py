count = 0
needed_pairs = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

def get_keys(line):
    pairs = line.split(' ')
    return map(lambda p: p.split(':')[0], pairs)

with open('day4_input.txt', 'r') as f:
    key_sets = []
    key_set = set()
    for line in f:
        if line == '\n':
            key_sets.append(key_set)
            key_set = set()
        else:
            key_set.update(get_keys(line))

    if len(key_set) > 0:
        key_sets.append(key_set)

    for ks in key_sets:
        if ks.issuperset(needed_pairs):
            count += 1


print(count)

