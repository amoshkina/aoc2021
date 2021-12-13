class Folder:
    def __init__(self, axis, coord):
        if axis == 'y':
            self.x = int(coord)
            self.y = 0
        else:
            self.x = 0
            self.y = int(coord)

    def fold(self, i, j):
        if self.x:
            return self.x - abs(self.x - i), j

        # y
        return i, self.y - abs(self.y - j)


class Solver:
    def __init__(self):
        self.matrix, self.folders = self.read_input()

    def print_matrix(self):
        for line in self.matrix:
            print(''.join(line))

    @staticmethod
    def read_input():
        max_x = max_y = 0
        dots = []
        folders = []
        with open('input.txt') as fd:
            for line in fd.readlines():
                line = line.strip()
                if not line:
                    continue
                elif line.startswith('fold along '):
                    folders.append(Folder(*line[len('fold along '):].split('=')))
                else:
                    y, x = list(map(int, line.split(',')))
                    dots.append((x, y))
                    max_x = max(max_x, x)
                    max_y = max(max_y, y)

        matrix = [['.' for _ in range(max_y+1)] for _ in range(max_x + 1)]
        for (i, j) in dots:
            matrix[i][j] = '#'

        return matrix, folders

    def score(self):
        counter = 0
        for line in self.matrix:
            counter += len(list(filter(lambda item: item == '#', line)))

        return counter

    def part1(self):
        folder = self.folders[0]
        for i, line in enumerate(self.matrix):
            for j, value in enumerate(line):
                if (0 < folder.x < i or 0 < folder.y < j) and self.matrix[i][j] == '#':
                    self.matrix[i][j] = '.'
                    i1, j1 = folder.fold(i, j)
                    self.matrix[i1][j1] = '#'

        return self.score()


if __name__ == '__main__':
    print('Day 13, part 1: ', Solver().part1())
