''' Created: 05/12/2023 '''

DAY = 5

# External imports
import re
from typing import Dict, List, Union
from tqdm import tqdm

# Internal imports
from aoc import AOC

def parse_data(puzzle: str) -> Dict[str, Union[List[int], List[Dict[str, List[int]]]]]:
    list_of_lines = puzzle.split('\n')
    seeds = list(map(int, re.findall(r'([0-9]+)', list_of_lines[0])))
    data = {'seeds': seeds, 'maps':[]}
    for line in list_of_lines[1:]:
        if line == '':
            continue
        elif 'map' in line:
            data['maps'].append({'target':[], 'source':[], 'length':[], 'size':0})
        else:
            numbers = re.findall(r'([0-9]+)', line)
            if len(numbers) != 3:
                raise Exception(f'Bad puzzle data... {line}')
            data['maps'][-1]['target'].append(int(numbers[0]))
            data['maps'][-1]['source'].append(int(numbers[1]))
            data['maps'][-1]['length'].append(int(numbers[2])) 
            data['maps'][-1]['size'] += 1     
    return data

def part_1(puzzle: str):
    data = parse_data(puzzle)
    results = []
    for value in data['seeds']:
        for map in data['maps']:
            for index in range(map['size']):
                map_min = map['source'][index]
                map_max = map_min + map['length'][index]
                if map_min <= value < map_max:
                    value = map['target'][index] + (value - map_min)
                    break
        results.append(value)
    return min(results)

def part_2(puzzle: str):
    pass
    # data = parse_data(puzzle)
    # seed_pairs = [data['seeds'][i:i + 2] for i in range(0, len(data['seeds']), 2)]
    # values = []
    # for seed_min, length in seed_pairs:
    #     seed_max = seed_min + length
    #     for map in data['maps']:
    #         for index in range(map['size']):
    #             map_min = map['source'][index]
    #             map_max = map_min + map['length'][index]
    #             if max(seed_min, map_min) < min(seed_max, map_max):
                    
    #                 break
    
if __name__ == '__main__':
    aoc = AOC(DAY)
    puzzle = aoc.get_puzzle()
    
    print(part_1(puzzle))
    print(part_2(puzzle))
