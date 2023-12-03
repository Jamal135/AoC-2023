''' Created: 02/12/2023 '''

DAY = 1

# External imports
import re

# Internal imports
from aoc import AOC

def part_1(puzzle: str) -> int:
    list_of_lines = puzzle.split('\n')
    calibration_value_sum = 0
    for line_text in list_of_lines:
        line_digits = ''.join(c for c in line_text if c.isdigit())
        if len(line_digits) > 1:
            calibration_value = int(line_digits[0] + line_digits[-1])
        else:
            calibration_value = int(line_digits * 2)
        calibration_value_sum += calibration_value
    return calibration_value_sum

def part_2(puzzle: str) -> int:
    numbers_dictionary = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    list_of_lines = puzzle.split('\n')
    calibration_value_sum = 0
    for line in list_of_lines:
        numbers_in_line = {}
        for number in numbers_dictionary:
            number_indexs = [m.start() for m in re.finditer(number, line)]
            for number_index in number_indexs:
                numbers_in_line[number_index] = number
        numbers_in_line = sorted(numbers_in_line.items())
        for _, number in numbers_in_line:
            line = line.replace(number, number[0] + numbers_dictionary[number] + number[1:], 1)
        line_digits = ''.join(c for c in line if c.isdigit())
        if len(line_digits) > 1:
            calibration_value = int(line_digits[0] + line_digits[-1])
        else:
            calibration_value = int(line_digits * 2)
        calibration_value_sum += calibration_value
    return calibration_value_sum

if __name__ == '__main__':
    aoc = AOC(DAY)
    puzzle = aoc.get_puzzle()

    print(part_1(puzzle))
    print(part_2(puzzle))
