import sys
from collections import defaultdict


class Solver:
    def __init__(self):
        self.pos_cnt, self.max_pos = self.read_input()
        self.dp = defaultdict(int)
        self.dp[0] = 0

    @staticmethod
    def read_input():
        pos_cnt = defaultdict(int)
        with open('input.txt') as fd:
            crabs = list(map(int, fd.read().strip().split(',')))

        max_pos = max(crabs)

        for crab_pos in crabs:
            pos_cnt[crab_pos] += 1

        return dict(pos_cnt), max_pos

    def part1(self):
        min_fuel = float('inf')
        for dest_pos in self.pos_cnt:
            fuel = 0
            for pos, count in self.pos_cnt.items():
                fuel += abs(pos-dest_pos) * count

            min_fuel = min(fuel, min_fuel)

        return min_fuel

    def fuel_cost(self, dist):
        if dist not in self.dp:
            self.dp[dist] = dist + self.fuel_cost(dist-1)

        return self.dp[dist]

    def part2(self):
        min_fuel = float('inf')
        for dest_pos in range(self.max_pos+1):
            fuel = 0
            for pos, count in self.pos_cnt.items():
                dist = abs(pos-dest_pos)
                fuel += self.fuel_cost(dist) * count
            min_fuel = min(fuel, min_fuel)

        return min_fuel


if __name__ == '__main__':
    sys.setrecursionlimit(2000)

    print('Day 7, part 1: ', Solver().part1())
    print('Day 7, part 2: ', Solver().part2())
