import numpy

class Card:
    def __init__(self, matrix):
        self.matrix = numpy.array(matrix)
        self.marked = numpy.zeros_like(self.matrix)

    def mark(self, number):
        result = numpy.where(self.matrix == number)
        if result:
            self.marked[result] = 1

    def check(self):
        for index, row in enumerate(self.marked):
            if all(row) == 1:
                return self.matrix[index]
        for index, row in enumerate(self.marked.T):
            if all(row) == 1:
                return self.matrix.T[index]
    
    def sum_unmarked(self):
        result = 0
        for r_index, row in enumerate(self.marked):
            for c_index, mark in enumerate(row):
                if mark == 0:
                    result += self.matrix[r_index, c_index]
        return result
