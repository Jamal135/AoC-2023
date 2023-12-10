''' Created: 10/12/2023 '''

DAY = 10

# External imports
from typing import List, Union
import math

# Internal imports
from aoc import AOC

def find_character(data: List[List[str]], target: str) -> List[int]:
    for y, row in enumerate(data):
        for x, character in enumerate(row):
            if character == target:
                return [x, y]
    raise Exception('No target character in data...')

def discover_start(data: List[List[str]], origin: List[int]) -> List[Union[List[int], str]]:
    x, y = origin[0], origin[1]
    if data[y - 1][x] in '|7F':
        return [[x, y - 1], 'N']
    elif data[y + 1][x] in '|LJ':
        return [[x, y + 1], 'S']
    elif data[y][x + 1] in '-LF':
        return [[x + 1, y], 'E']
    elif data[y][x - 1] in '-J7':
        return [[x - 1, y], 'W']
    else: raise Exception('How did we get here...')

def construct_loop(data: List[List[str]], start: List[int], facing: str) -> List[str]:
    positions = [start]
    while True:
        x, y = positions[-1][0], positions[-1][1]
        character = data[y][x]
        match character:
            case '|':
                if facing == 'N':
                    positions.append([x, y - 1])
                elif facing == 'S':
                    positions.append([x, y + 1])
                else: raise Exception('Bad entry point...')
            case '-':
                if facing == 'E':
                    positions.append([x + 1, y])
                elif facing == 'W':
                    positions.append([x - 1, y])
                else: raise Exception('Bad entry point...')
            case 'L':
                if facing == 'S':
                    positions.append([x + 1, y])
                    facing = 'E'
                elif facing == 'W':
                    positions.append([x, y - 1])
                    facing = 'N'
                else: raise Exception('Bad entry point...')
            case 'J':
                if facing == 'E':
                    positions.append([x, y - 1])
                    facing = 'N'
                elif facing == 'S':
                    positions.append([x - 1, y])
                    facing = 'W'
                else: raise Exception('Bad entry point...')
            case '7':
                if facing == 'E':
                    positions.append([x, y + 1])
                    facing = 'S'
                elif facing == 'N':
                    positions.append([x - 1, y])
                    facing = 'W'
                else: raise Exception('Bad entry point...')
            case 'F':
                if facing == 'N':
                    positions.append([x + 1, y])
                    facing = 'E'
                elif facing == 'W':
                    positions.append([x, y + 1])
                    facing = 'S'
                else: raise Exception('Bad entry point...')
            case '.':
                raise Exception('Bad position...')
            case 'S':
                break
            case _:
                raise Exception('How did we get here...')
    return positions

def part_1(puzzle: str):
    data = [[char for char in string] for string in puzzle.split('\n')]
    origin_position = find_character(data, 'S')
    start_position, facing = discover_start(data, origin_position)
    loop_positions = construct_loop(data, start_position, facing)
    return math.ceil(len(loop_positions[:-1]) / 2)

def find_interior(positions: List[List[int]], width: int, height: int) -> int:
    interior_matrix = [[0 for _ in range(width)] for _ in range(height)]
    x_values = []
    for y in range(height):
        x_values.append(sorted([pos[0] for pos in positions if pos[1] == y]))
    for y in range(height):
        if x_values[y] == []:
            continue
        max_x = x_values[y][-1] + 1
        min_x = x_values[y][0]
        for x in range(min_x, max_x):
            if x in x_values[y]:
                interior_matrix[y][x] += 3
            if x not in x_values[y]:
                interior_matrix[y][x] += 1
    for line in interior_matrix:
        print(line)
    # Need to account for gaps between pipes somehow...
    return sum(cell == 1 for row in interior_matrix for cell in row)

def part_2(puzzle: str):
    data = [[char for char in string] for string in puzzle.split('\n')]
    origin_position = find_character(data, 'S')
    start_position, facing = discover_start(data, origin_position)
    loop_positions = construct_loop(data, start_position, facing)
    return find_interior(loop_positions, len(data[0]), len(data))

if __name__ == '__main__':
    aoc = AOC(DAY)
    puzzle = aoc.get_puzzle()
    
    print(part_1(puzzle))
    print(part_2(puzzle))
