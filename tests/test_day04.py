from aoc2021.day04 import solution
from aoc2021.util import get_input_day04


input_data = get_input_day04("tests/testinput.day04")


def test_solve_part1():
    expected = 4512
    #print(input_data)
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = 1924
    actual = solution.solve_part2(input_data)
    assert expected == actual
