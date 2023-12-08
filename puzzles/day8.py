''' Created: 08/12/2023 '''

DAY = 8

# External imports
from typing import Dict, List, Union
import math
from functools import reduce
import re

# Internal imports
from aoc import AOC

def parse_data(puzzle: str) -> Dict[str, Union[int, List[Dict[str, str]]]]:
    list_of_lines = puzzle.split('\n')
    keys, nodes = list_of_lines[0], []
    for line in list_of_lines[2:]:
        node = re.findall(r'([A-Z0-9]+)', line)
        node_data = {'name': node[0], 'L': node[1], 'R': node[2]}
        nodes.append(node_data)
    return {'keys':keys, 'nodes':nodes}

def part_1(puzzle: str):
    data = parse_data(puzzle)
    keys_length = len(data['keys'])
    node = 'AAA'
    node_index = {node['name']: node for node in data['nodes']}
    index = 0
    while True:
        key = data['keys'][index % keys_length]
        node_data = node_index.get(node)
        node = node_data[key]
        index += 1
        if node == 'ZZZ':
            break
    return index

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def part_2(puzzle: str):
    data = parse_data(puzzle)
    node_index = {node['name']: node for node in data['nodes']}
    keys_length = len(data['keys'])
    starting_nodes = [node for node in node_index if node.endswith('A')]
    node_index = {node['name']: node for node in data['nodes']}
    cycle_lengths = []
    for start_node in starting_nodes:
        node = start_node
        index = 0
        while True: # We know each cycle to Z ending node is the same length
            key = data['keys'][index % keys_length]
            node_data = node_index.get(node)
            node = node_data[key]
            index += 1
            if node.endswith('Z'):
                cycle_lengths.append(index)
                break
    return reduce(lcm, cycle_lengths)

if __name__ == '__main__':
    aoc = AOC(DAY)
    puzzle = aoc.get_puzzle()
    
    print(part_1(puzzle))
    print(part_2(puzzle))
