from collections import defaultdict

class Solver:
    def __init__(self):
        self.pos_cnt = self.read_input()

    @staticmethod
    def read_input():
        pos_cnt = defaultdict(int)
        with open('input.txt') as fd:
            crabs = map(int, fd.read().strip().split(','))

        for crab_pos in crabs:
            pos_cnt[crab_pos] += 1

        return dict(pos_cnt)

    def part1(self):
        min_fuel = float('inf')
        for dest_pos in self.pos_cnt:
            fuel = 0
            for pos, count in self.pos_cnt.items():
                fuel += abs(pos-dest_pos) * count

            min_fuel = min(fuel, min_fuel)

        return min_fuel


if __name__ == '__main__':
    print('Day 7, part 1: ', Solver().part1())
