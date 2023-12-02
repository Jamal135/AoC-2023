''' Created: 02/12/2023 '''

day = 2

# External imports
import re

# Internal imports
from aoc import AOC

def part_1(puzzle: str):
    given_game = {'red': 12, 'green': 13, 'blue': 14}
    list_of_lines = puzzle.split('\n')
    game_data = {}
    for line in list_of_lines:
        game_number = int(re.search(r'Game\s+(\d+):', line).group(1))
        game_data[game_number] = {}
        for index, round in enumerate(line.split(';')):
            game_data[game_number][index] = {}
            for colour in given_game.keys():
                pattern = rf'\b(\d+)\s+{colour}\b'
                game_data[game_number][index][colour] = sum(map(int, re.findall(pattern, round)))
    tally = 0
    for game_number, rounds in game_data.items():
        if all(not any(color_totals[color] > given_game[color] for color in color_totals) for _, color_totals in rounds.items()):
            tally += game_number
    return tally
    
def part_2(puzzle: str):
    given_game = {'red': 12, 'green': 13, 'blue': 14}
    list_of_lines = puzzle.split('\n')
    game_data = {}
    for line in list_of_lines:
        game_number = int(re.search(r'Game\s+(\d+):', line).group(1))
        game_data[game_number] = {}
        for colour in given_game.keys():
            pattern = rf'\b(\d+)\s+{colour}\b'
            game_data[game_number][colour] = max(map(int, re.findall(pattern, line)))
    power_sum = 0
    for game_number, color_totals in game_data.items():
        power = 1
        for _, total in color_totals.items():
            power *= total
        power_sum += power
    return power_sum

if __name__ == '__main__':
    aoc = AOC(day)
    puzzle = aoc.get_puzzle()
    
    print(part_1(puzzle))
    print(part_2(puzzle))
