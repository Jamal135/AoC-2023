''' Created: 09/12/2023 '''

DAY = 9

# External imports
from typing import List
import re

# Internal imports
from aoc import AOC

def parse_data(puzzle: str) -> List[List[int]]:
    list_of_lines = puzzle.split('\n')
    data = []
    for line in list_of_lines:
        data.append(list(map(int, re.findall(r'([0-9-]+)', line))))
    return data

def compute_pattern(sequence: List[int]) -> List[List[int]]:
    sequence_layers = [sequence]
    base_length = len(sequence_layers[0]) - 1
    index = 0
    while True:
        current_layer = sequence_layers[index]
        size = range(base_length - index)
        next_layer = [current_layer[i + 1] - current_layer[i] for i in size]
        sequence_layers.append(next_layer)
        if all(value == next_layer[0] for value in next_layer):
            break
        index += 1
    return sequence_layers

def compute_next_value(pattern_data: List[List[int]], forward: bool = True) -> int:
    if forward: # Compute next value in sequence.
        return sum(pattern[-1] for pattern in pattern_data)
    else: # Compute previous value in sequence.
        value = 0
        for pattern in pattern_data[::-1]:
            value = pattern[0] - value
        return value

def part_1(puzzle: str):
    data = parse_data(puzzle)
    results = []
    for sequence in data:
        pattern_data = compute_pattern(sequence)
        results.append(compute_next_value(pattern_data))
    return sum(results)

def part_2(puzzle: str):
    data = parse_data(puzzle)
    results = []
    for sequence in data:
        pattern_data = compute_pattern(sequence)
        results.append(compute_next_value(pattern_data, False))
    return sum(results)

if __name__ == '__main__':
    aoc = AOC(DAY)
    puzzle = aoc.get_puzzle()

    print(part_1(puzzle))
    print(part_2(puzzle))
