from collections import defaultdict


class Solver:
    OPEN = {'(', '[', '<', '{'}

    PAIR = {
        ')': '(',
        ']': '[',
        '>': '<',
        '}': '{'
    }

    ILLEGAL_SCORES = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    INCOMPLETE_SCORES = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
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

    def score_illegal(self, illegal):
        result = 0
        for item, count in illegal.items():
            result += self.ILLEGAL_SCORES[item] * count

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

        return self.score_illegal(illegal)

    def part2(self):
        scores = []
        for line in self.nav_matrix:
            stack = []
            illegal = False
            for item in line:
                if item in self.OPEN:
                    stack.append(item)
                else:
                    last = stack.pop()
                    if last != self.PAIR[item]:
                        illegal = True
                        break
            local_score = 0
            if not illegal and len(stack) > 0:
                for item in reversed(stack):
                    local_score *= 5
                    local_score += self.INCOMPLETE_SCORES[item]
                scores.append(local_score)

        return sorted(scores)[int(len(scores) / 2)]


if __name__ == '__main__':
    print('Day 10, part 1: ', Solver().part1())
    print('Day 10, part 2: ', Solver().part2())
