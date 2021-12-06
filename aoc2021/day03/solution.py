from collections import Counter
import numpy
from aoc2021.util import get_input


def solve_part1(entries):
    # convert entries to a matrix
    matrix = numpy.array(entries)
    # transpose it and count most common bit
    gamma_rate = ""
    epsilon_rate = ""
    for row in matrix.T:
        gamma_rate += str(Counter(row).most_common(1)[0][0])
        epsilon_rate += str(Counter(row).most_common()[::-1][0][0])
    #print(gamma_rate)
    #print(epsilon_rate)
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def calculate_oxygen_generator_rate(entries):
    entry_len = len(entries[0])
    matrix = numpy.array(entries)
    for index in range(entry_len):
        if len(matrix) == 1:
            break
        # transpose the entries immediately
        t_matrix = matrix.T
        #print(index)
        #print(matrix)
        #print(t_matrix)
        most_common = Counter(t_matrix[index]).most_common(1)[0]
        least_common = Counter(t_matrix[index]).most_common()[::-1][0]
        if most_common[1] == least_common[1]:
            most_common = 1
        else:
            most_common = most_common[0]
        #print(f"most common: {most_common}")
        # collect all indexes not matching most common value
        rows = list()
        for _index, row in enumerate(matrix):
            if row[index] != most_common:
                rows.append(_index)
        matrix = numpy.delete(matrix, rows, 0)
        #print("done deleting, matrix is now")
        #print(matrix)
    result = ""
    for bit in matrix[0]:
        result += str(bit)
    return result

def calculate_co2_scrubber_rate(entries):
    entry_len = len(entries[0])
    matrix = numpy.array(entries)
    for index in range(entry_len):
        if len(matrix) == 1:
            break
        # transpose the entries immediately
        t_matrix = matrix.T
        most_common = Counter(t_matrix[index]).most_common(1)[0]
        least_common = Counter(t_matrix[index]).most_common()[::-1][0]
        if most_common[1] == least_common[1]:
            least_common = 0
        else:
            least_common = least_common[0]
        # collect all indexes not matching least common value
        rows = list()
        for _index, row in enumerate(matrix):
            if row[index] != least_common:
                rows.append(_index)
        matrix = numpy.delete(matrix, rows, 0)
    result = ""
    for bit in matrix[0]:
        result += str(bit)
    return result


def solve_part2(entries):
    oxygen_generator_rate = calculate_oxygen_generator_rate(entries)
    co2_scrubber_rate = calculate_co2_scrubber_rate(entries)
    #print(oxygen_generator_rate)
    #print(co2_scrubber_rate)
    return int(oxygen_generator_rate, 2) * int(co2_scrubber_rate, 2)


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2021/day03/input", "int-matrix")
    print(solve_part1(entries))
    print(solve_part2(entries))
