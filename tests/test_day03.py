from aoc2021.day03 import solution
from aoc2021.util import get_input


input_data = get_input("tests/testinput.day03", "int-matrix")

def test_solve_part1():
    expected = 198
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = 230
    actual = solution.solve_part2(input_data)
    assert expected == actual
