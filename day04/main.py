class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.marked = False


class Board:
    def __init__(self, rows):
        self.won = False
        self.rows = [0] * 5
        self.cols = [0] * 5

        self.matrix = {}

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                self.matrix[value] = Coord(i, j)


class Solver:
    def __init__(self):
        self.numbers, self.boards = self.read_input()
        self.play = self._play()

    @staticmethod
    def read_input():
        with open('input.txt') as fd:
            data = fd.read()
            data = data.split('\n\n')
            numbers = data[0].split(',')
            boards = []
            for idx, board in enumerate(data):
                if idx == 0:
                    continue

                rows = map(lambda x: x.split(), board.split('\n'))
                boards.append(Board(rows))

            return numbers, boards

    def _play(self):
        for number in self.numbers:
            for board in self.boards:
                if number not in board.matrix or board.won:
                    continue

                coord = board.matrix[number]
                coord.marked = True
                board.rows[coord.x] += 1
                board.cols[coord.y] += 1

                if board.rows[coord.x] == 5 or board.cols[coord.y] == 5:
                    board.won = True
                    yield board, int(number)

            self.boards = list(filter(lambda item: not item.won, self.boards))

    @staticmethod
    def score(board, number):
        unmarked_sum = 0
        for value, coord in board.matrix.items():
            if not coord.marked:
                unmarked_sum += int(value)

        return unmarked_sum * number

    def part1(self):
        return self.score(*next(self.play))

    def part2(self):
        return self.score(*list(self.play)[-1])


if __name__ == '__main__':
    solver = Solver()

    print('Day 4, part 1: ', solver.part1())
    print('Day 4, part 2: ', solver.part2())
