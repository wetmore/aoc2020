import re
from collections import defaultdict

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

def num_bags(graph, bag, n):
    total = n
    for m, contained_bag in graph[bag]:
        total += n * num_bags(graph, contained_bag, m)
    return total

with open('day7_input.txt', 'r') as f:
    graph = defaultdict(list)
    for line in f:
        bag, pairs = parse_line(line)
        for num_bag, contained_bag in pairs:
            graph[bag].append((num_bag, contained_bag))

    print(num_bags(graph, 'shiny gold', 1) - 1)
    
        

