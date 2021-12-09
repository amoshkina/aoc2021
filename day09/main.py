class Solver:

    def __init__(self):
        self.matrix = self.read_input()
        self.max_row = len(self.matrix)
        self.max_col = len(self.matrix[0])

    @staticmethod
    def read_input():
        matrix = []
        with open('input.txt') as fd:
            for row in fd.readlines():
                matrix.append(list(map(int, list(row.strip()))))

        return matrix

    def part1(self):
        result = 0
        for i, row in enumerate(self.matrix):
            for j, height in enumerate(row):
                neighbours = [
                    (i-1, j), (i+1, j),
                    (i, j-1), (i, j+1)
                ]

                local_min = True
                for i1, j1 in neighbours:
                    if 0 <= i1 < self.max_row and 0 <= j1 < self.max_col and self.matrix[i1][j1] <= height:
                        local_min = False
                        break

                if local_min:
                    result += height + 1

        return result


if __name__ == '__main__':
    print('Day 9, part 1: ', Solver().part1())
