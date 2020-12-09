from math import floor

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
    all_ids = set()
    for row in range(0, 128):
        for col in range(0, 8):
            all_ids.add(row*8+col)
    
    boarding_list = set()
    for line in f:
        boarding_list.add(get_id(line))

    for id_ in all_ids.difference(boarding_list):
        if id_ +1 in boarding_list and id_-1 in boarding_list:
            print(id_)

