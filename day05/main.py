class Segment:
    def __init__(self, start, end):
        self.x1 = start[0]
        self.y1 = start[1]
        self.x2 = end[0]
        self.y2 = end[1]

    @property
    def horizontal(self):
        return self.y1 == self.y2

    @property
    def vertical(self):
        return self.x1 == self.x2

    def __str__(self):
        return f'{self.x1},{self.y1} -> {self.x2}, {self.y2}'


class Solver:
    def __init__(self):
        segments, max_x, max_y = self.read_input()

        self.segments = segments
        self.height = max_x + 1
        self.width = max_y + 1
        self.matrix = [[0] * self.width for _ in range(self.height)]

    @staticmethod
    def read_input():
        with open('input.txt') as fd:
            segments = []
            max_x, max_y = 0, 0
            for line in fd.readlines():
                points = []
                for item in line.split('->'):
                    x, y = map(int, item.strip().split(','))
                    points.append((x, y))
                    max_x, max_y = max(x, max_x), max(y, max_y)

                segments.append(Segment(*points))

            return segments, max_x, max_y

    def part1(self):
        for segment in self.segments:
            if segment.horizontal or segment.vertical:
                dir_x = 1 if segment.x1 <= segment.x2 else -1
                dir_y = 1 if segment.y1 <= segment.y2 else - 1

                for x in range(segment.x1, segment.x2 + dir_x, dir_x):
                    for y in range(segment.y1, segment.y2 + dir_y, dir_y):

                        self.matrix[x][y] += 1

        counter = 0
        for line in self.matrix:
            for value in line:
                if value > 1:
                    counter += 1

        return counter


if __name__ == '__main__':
    solver = Solver()

    print('Day 5, part 1: ', solver.part1())
