''' Created: 06/12/2023 '''

DAY = 6

# External imports
import re
from functools import reduce

# Internal imports
from aoc import AOC

def parse_data_1(puzzle: str):
    times, distances = puzzle.split('\n', maxsplit=1)
    numbers = lambda line: [int(num) for num in re.findall(r'([0-9]+)', line)]
    return {'times': numbers(times), 'distances': numbers(distances)}

def part_1(puzzle: str):
    data = parse_data_1(puzzle)
    results = []
    for total_time, record_distance in zip(data['times'], data['distances']):
        tally = 0
        for time in range(0, total_time):
            distance = (total_time - time) * time
            if distance > record_distance:
                tally += 1
        if tally > 0:
           results.append(tally)
    return reduce(lambda x, y: x * y, results, 1)

def parse_data_2(puzzle: str):
    times, distances = puzzle.split('\n', maxsplit=1)
    numbers = lambda line: int(''.join(re.findall(r'([0-9]+)', line)))
    return {'time': numbers(times), 'distance': numbers(distances)}

def part_2(puzzle: str):
    data = parse_data_2(puzzle)
    total_time, record_distance = data['time'], data['distance']
    tally = 0
    for time in range(0, total_time):
        distance = (total_time - time) * time
        if distance > record_distance:
            tally += 1
    return tally

if __name__ == '__main__':
    aoc = AOC(DAY)
    puzzle = aoc.get_puzzle()

    print(part_1(puzzle))
    print(part_2(puzzle))
