''' Created: 03/12/2023 '''

day = 3

# External imports
import re

# Internal imports
from aoc import AOC

def part_1(puzzle: str):
    line_length = puzzle.find('\n')
    symbols = set(char for char in puzzle if not char.isdigit() and char != '.')
    puzzle = puzzle.replace('\n', '')
    total = 0
    for index, char in enumerate(puzzle):
        if char in symbols:
            get_slice = lambda offset: puzzle[(index + offset - 3):(index + offset + 4)]
            data = ' '.join(['' + get_slice(-line_length), get_slice(0), get_slice(line_length) + ''])
            matches = map(int, re.findall(r'\d{3}|(?<=\S)\d{2}(?=\S)|(?<=\S{2})\d{1}(?=\S{2})', data))
            total += sum(matches)
    return total

def part_2(puzzle: str):
    line_length = puzzle.find('\n')
    puzzle = puzzle.replace('\n', '')
    total = 0
    for index, character in enumerate(puzzle):
        if character == '*':
            get_slice = lambda offset: puzzle[(index + offset - 3):(index + offset + 4)]
            data = ' '.join(['' + get_slice(-line_length), get_slice(0), get_slice(line_length) + ''])
            matches = list(map(int, re.findall(r'\d{3}|(?<=\S)\d{2}(?=\S)|(?<=\S{2})\d{1}(?=\S{2})', data)))
            if len(matches) == 2:
                gear_ratio = matches[0] * matches[1]
                total += gear_ratio
    return total

if __name__ == '__main__':
    aoc = AOC(day)
    puzzle = aoc.get_puzzle()
    
    print(part_1(puzzle))
    print(part_2(puzzle))
