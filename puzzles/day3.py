''' Created: '''

day = 3

# External imports
import re

# Internal imports
from aoc import AOC

def part_1(puzzle: str):
    line_length = len(puzzle.split('\n')[0])
    symbols = set(char for char in puzzle if not char.isdigit() and char != '.')
    puzzle = puzzle.replace('\n', '')
    total = 0
    for index, character in enumerate(puzzle):
        if character in symbols:
            x, y = divmod(index, line_length)
            base_index = x * line_length + y
            get_slice = lambda offset: puzzle[(base_index + offset - 3):(base_index + offset + 4)]
            data = " ".join(["", get_slice(-line_length), get_slice(0), get_slice(line_length), ""])
            matches = re.findall(r'\d{3}|(?<=\.)\d{2}(?=\.)|(?<=\.\S)\d(?=\S\.)', data)
            total += sum(map(int, matches))
    return total

def part_2(puzzle: str):
    pass

if __name__ == '__main__':
    aoc = AOC(day)
    puzzle = aoc.get_puzzle()

    print(part_1(puzzle))
    print(part_2(puzzle))
