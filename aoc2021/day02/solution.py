from aoc2021.util import get_input
from aoc2021.day02 import submarine


def solve_part1(entries):
    sub = submarine.Submarine()
    sub.navigate(entries)
    return sub.position.horizontal * sub.position.depth


def solve_part2(entries):
    sub = submarine.Submarine2()
    sub.navigate(entries)
    return sub.position.horizontal * sub.position.depth


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2021/day02/input", "split")
    print(solve_part1(entries))
    print(solve_part2(entries))
