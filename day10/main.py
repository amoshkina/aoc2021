from collections import defaultdict


class Solver:
    OPEN = {'(', '[', '<', '{'}

    PAIR = {
        ')': '(',
        ']': '[',
        '>': '<',
        '}': '{'
    }

    SCORER = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    def __init__(self):
        self.nav_matrix = self.read_input()

    @staticmethod
    def read_input():
        nav_matrix = []
        with open('input.txt') as fd:
            for line in fd.readlines():
                nav_matrix.append(list(line.strip()))

        return nav_matrix

    def score(self, illegal):
        result = 0
        for item, count in illegal.items():
            result += self.SCORER[item] * count

        return result

    def part1(self):
        illegal = defaultdict(int)
        for line in self.nav_matrix:
            stack = []
            for item in line:
                if item in self.OPEN:
                    stack.append(item)
                else:
                    last = stack.pop()
                    if last != self.PAIR[item]:
                        illegal[item] += 1

        return self.score(illegal)


if __name__ == '__main__':
    print('Day 10, part 1: ', Solver().part1())
