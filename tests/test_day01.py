from aoc2021.day01 import solution
from aoc2021.util import get_input


input_data = get_input("tests/testinput.day01", "int")


def test_solve_part1():
    expected = 7
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = 5
    actual = solution.solve_part2(input_data)
    assert expected == actual
