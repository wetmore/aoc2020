import re
from collections import defaultdict


total= 0

def parse_contained(bag_string):
    m = re.search(r'([0-9]+) (.+?) bag', bag_string)
    return int(m.group(1)), m.group(2)

def parse_line(line):
    m = re.search(r'^(.+?) bags contain (.+?)\.', line)
    bag = m.group(1)

    rest = m.group(2)
    if rest == 'no other bags':
        return bag, []
    else:
        return bag, map(parse_contained, rest.split(', '))

with open('day7_input.txt', 'r') as f:
    graph = defaultdict(list)
    for line in f:
        bag, pairs = parse_line(line)
        for num_bag, contained_bag in pairs:
            graph[contained_bag].append(bag)

    visited = set()
    to_visit = ['shiny gold']

    while len(to_visit) > 0:
        bag = to_visit.pop()
        for containing_bag in graph[bag]:
            if containing_bag not in visited:
                to_visit.append(containing_bag)
        visited.add(bag)

    print(len(visited) - 1)
    
        

