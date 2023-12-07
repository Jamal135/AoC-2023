''' Created: 07/12/2023 '''

DAY = 7

# External imports
from typing import List, Dict
from collections import Counter

# Internal imports
from aoc import AOC

def parse_data(puzzle: str, jokers: bool = False) -> Dict[str, List[List[int]]]:
    list_of_lines = puzzle.split('\n')
    data = {'five_of_a_kind':[],'four_of_a_kind':[],'full_house':[],'three_of_a_kind':[],'two_pair':[],'one_pair':[],'high_card':[]}
    for line in list_of_lines:
        hand, bid = line.split(' ', maxsplit=1)
        number_different_cards = len(set(hand))
        number_jokers = line.count('J')
        if jokers and number_jokers not in [0, 5]:
            most_common_count = Counter(hand.replace('J', '')).most_common(1)[0][1]
            number_different_cards -= 1
            most_common_count += number_jokers
        else:
            most_common_count = Counter(hand).most_common(1)[0][1]
        match number_different_cards:
            case 5:
                data['high_card'].append([hand, bid])
            case 4:
                data['one_pair'].append([hand, bid])
            case 3:
                if most_common_count == 3:
                    data['three_of_a_kind'].append([hand, bid])
                else:
                    data['two_pair'].append([hand, bid])
            case 2:
                if most_common_count == 4:
                    data['four_of_a_kind'].append([hand, bid])
                else:
                    data['full_house'].append([hand, bid])
            case 1:
                data['five_of_a_kind'].append([hand, bid])
    return data

def sort_data(data: Dict[str, List[List[int]]], order: str) -> List[List[int]]:
    rank_map = {char: index for index, char in enumerate(order)}
    for key, list_of_lists in data.items():
        data[key] = sorted(list_of_lists, key=lambda x: [rank_map[char] for char in x[0]])
    return [item for key in data for item in data[key]][::-1]

def sum_values(data: List[List[int]]) -> int:
    result = 0
    for index, game_data in enumerate(data):
        result += int(game_data[1]) * (index + 1)
    return result

def part_1(puzzle: str):
    data = parse_data(puzzle)
    sorted_data = sort_data(data, 'AKQJT98765432')
    return sum_values(sorted_data)

def part_2(puzzle: str):
    data = parse_data(puzzle, True)
    sorted_data = sort_data(data, 'AKQT98765432J')
    return sum_values(sorted_data)
    
if __name__ == '__main__':
    aoc = AOC(DAY)
    puzzle = aoc.get_puzzle()

    print(part_1(puzzle))
    print(part_2(puzzle))
