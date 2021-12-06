from aoc2021.util import get_input


def solve_part1(entries):
    tally = 0
    current = entries[0]
    for entry in entries:
        if entry > current:
            tally += 1
        current = entry
    return tally

def solve_part2(entries):
    tally = 0
    current = sum(entries[0:3])
    for index, entry in enumerate(entries):
        try:
            entries[index+2]
            value = sum(entries[index:index+3])
            if value > current:
                tally +=1 
            current = value
        except IndexError:
            break
    return tally


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2021/day01/input", "int")
    print(solve_part1(entries))
    print(solve_part2(entries))
