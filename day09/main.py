from collections import defaultdict


class Solver:

    def __init__(self):
        self.matrix = self.read_input()
        self.max_row = len(self.matrix)
        self.max_col = len(self.matrix[0])
        self.component_size = defaultdict(int)

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
                    cond = (
                        0 <= i1 < self.max_row and
                        0 <= j1 < self.max_col and
                        self.matrix[i1][j1] <= height
                    )

                    if cond:
                        local_min = False
                        break

                if local_min:
                    result += height + 1

        return result

    def bfs(self, i, j, component):
        neighbours = [
            (i-1, j), (i+1, j),
            (i, j-1), (i, j+1)
        ]

        for i1, j1 in neighbours:
            cond = (
                0 <= i1 < self.max_row and
                0 <= j1 < self.max_col and
                0 <= self.matrix[i1][j1] < 9
            )

            if cond:
                self.matrix[i1][j1] = component
                self.component_size[component] += 1
                self.bfs(i1, j1, component)

    def score(self):
        sorted_sizes = sorted(self.component_size.values(), reverse=True)
        assert len(sorted_sizes) >= 3
        return sorted_sizes[0] * sorted_sizes[1] * sorted_sizes[2]

    def part2(self):
        component = -1
        for i, row in enumerate(self.matrix):
            for j, height in enumerate(row):
                if height < 0 or height == 9:
                    continue
                self.bfs(i, j, component)
                component -= 1

        return self.score()


if __name__ == '__main__':
    print('Day 9, part 1: ', Solver().part1())
    print('Day 9, part 2: ', Solver().part2())
