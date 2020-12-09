from math import floor

max_id = 0

def get_id(line):
    row_range = [0, 127]
    col_range = [0, 7]

    for c in line:
        if c == 'F':
            lo, hi = row_range
            row_range = [lo, floor((hi+lo)/2)]
        elif c == 'B':
            lo, hi = row_range
            row_range = [floor((hi+lo)/2)+1, hi]
        elif c == 'L':
            lo, hi = col_range
            col_range = [lo, floor((hi+lo)/2)]
        elif c == 'R':
            lo, hi = col_range
            col_range = [floor((hi+lo)/2)+1, hi]
    
    print(row_range, col_range)

    return row_range[0] * 8 + col_range[0]

with open('day5_input.txt', 'r') as f:
    for line in f:
        max_id = max(get_id(line), max_id)

print(max_id)

