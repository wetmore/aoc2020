count = 0
needed_pairs = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

def is_valid_key(key, value):
    if key == 'byr':
        year = int(value)
        return year >= 1920 and year <= 2002
    elif key == 'iyr':
        year = int(value)
        return year >= 2010 and year <= 2020
    elif key == 'eyr':
        year = int(value)
        return year >= 2020 and year <= 2030
    elif key == 'hgt':
        i = value.find('cm')
        if i > -1:
            height = int(value[:i])
            print('height is', height)
            return height >= 150 and height <= 193
        i = value.find('in')
        if i > -1:
            height = int(value[:i])
            return height >= 59 and height <= 76
        return False
    elif key == 'hcl':
        if len(value) != 7 or value[0] != '#':
            return False
        for c in value[1:]:
            if c not in char_range('0','9') and c not in char_range('a','f'):
                return False
        return True
    elif key == 'ecl':
        return value in ['amb','blu','brn','gry','grn','hzl','oth']
    elif key == 'pid':
        if len(value) != 9:
            return False
        return all(map(lambda c: c in char_range('0','9'), value))
    else:
        return False

def get_keys(line):
    keys = []
    for pair in line.split(' '):
        key, value = pair.split(':')
        if is_valid_key(key.strip(), value.strip()):
            print(f"{key}:{value} is valid")
            keys.append(key)
        else:
            print(f"{value} not valid for {key}")
    print(keys)
    return keys

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

