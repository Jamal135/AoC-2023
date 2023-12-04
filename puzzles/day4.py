''' Created: 04/12/2023 '''

DAY = 4

# External imports
import re

# Internal imports
from aoc import AOC

def part_1(puzzle: str):
    list_of_lines = puzzle.split('\n')
    total = 0
    for line in list_of_lines:
        _, data = line.split(':', maxsplit=1) # Remove start text
        win_nums, game_nums = data.split('|', maxsplit=1)
        list_win_nums = re.findall(r'([0-9]+)', win_nums)
        list_game_nums = re.findall(r'([0-9]+)', game_nums)
        num_wins = sum(list_game_nums.count(win_num) for win_num in list_win_nums)
        if num_wins != 0:
            total += 2 ** (num_wins - 1)
    return total

def part_2(puzzle: str):
    list_of_lines = puzzle.split('\n')
    game_data = []
    for line in list_of_lines:
        _, data = line.split(':', maxsplit=1) # Remove start text
        win_nums, game_nums = data.split('|', maxsplit=1)
        list_win_nums = re.findall(r'([0-9]+)', win_nums)
        list_game_nums = re.findall(r'([0-9]+)', game_nums)
        num_wins = sum(list_game_nums.count(win_num) for win_num in list_win_nums)
        game_data.append({'wins':num_wins, 'copies':1})
    for index, game in enumerate(game_data):
        if game['wins'] == 0:
            continue
        pos = index + 1
        for next_game in game_data[pos:pos + game['wins']]:
            next_game['copies'] += 1 * game['copies']
    return sum(game['copies'] for game in game_data)

if __name__ == '__main__':
    aoc = AOC(DAY)
    puzzle = aoc.get_puzzle()
    
    print(part_1(puzzle))
    print(part_2(puzzle))
