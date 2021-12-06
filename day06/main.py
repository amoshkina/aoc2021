from collections import defaultdict

class Solver:

    def __init__(self):
        self.fish_map = self.read_input()

    def read_input(self):
        with open('input.txt') as fd:
            fish_list = list(map(int, fd.read().strip().split(',')))

        fish_map = defaultdict(int)

        for fish_value in fish_list:
            fish_map[fish_value] += 1

        return fish_map

    def score(self):
        return sum(self.fish_map.values())

    def live(self, days):
        for day in range(days):
            assert len(self.fish_map) <= 9
            new_fish_map = defaultdict(int)
            for fish_value, count in self.fish_map.items():
                if fish_value == 0:
                    fish_value = 6
                    new_fish_map[8] += count
                else:
                    fish_value -= 1

                new_fish_map[fish_value] += count

            self.fish_map = new_fish_map

        return self.score()

    def part1(self):
        return self.live(80)

    def part2(self):
        return self.live(256)


if __name__ == '__main__':
    print('Day 6, part 1:', Solver().part1())
    print('Day 6, part 2:', Solver().part2())
