class Segment:
    def __init__(self, p1, p2):
        self.x1 = p1[0]
        self.y1 = p1[1]
        self.x2 = p2[0]
        self.y2 = p2[1]

        self.dir_x = self.get_dir(self.x1, self.x2)
        self.dir_y = self.get_dir(self.y1, self.y2)

    @staticmethod
    def get_dir(c1, c2):
        if c1 == c2:
            return 0

        if c1 < c2:
            return 1

        return -1

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

    def score(self):
        counter = 0
        for line in self.matrix:
            for value in line:
                if value > 1:
                    counter += 1
        return counter

    def draw_segment(self, segment):
        x = segment.x1 + segment.dir_x * -1
        y = segment.y1 + segment.dir_y * -1
        while x != segment.x2 or y != segment.y2:
            x += segment.dir_x
            y += segment.dir_y
            self.matrix[x][y] += 1

        assert x == segment.x2 and y == segment.y2

    def part1(self):
        for segment in self.segments:
            if segment.horizontal or segment.vertical:
                self.draw_segment(segment)

        return self.score()

    def part2(self):
        for segment in self.segments:
            self.draw_segment(segment)

        return self.score()


if __name__ == '__main__':
    print('Day 5, part 1: ', Solver().part1())
    print('Day 5, part 2: ', Solver().part2())
