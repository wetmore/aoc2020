map_ = {}

with open('day1_1_input.txt', 'r') as f:
    for line in f:
        n = int(line)
        remainder = 2020 - n
        if str(n) in map_:
            print(map_[str(n)]*n)
        else:
            map_[str(remainder)] = n

