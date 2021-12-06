from aoc2021.day02 import solution
from aoc2021.util import get_input


input_data = get_input("tests/testinput.day02", "split")


def test_solve_part1():
    expected = 150
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = 900
    actual = solution.solve_part2(input_data)
    assert expected == actual
