class Solver:

    def __init__(self, days):
        with open('input.txt') as fd:
            self.fish_list = list(map(int, fd.read().strip().split(',')))

        self.days = days

    def part1(self):
        for day in range(self.days):
            new_fish_counter = 0
            for idx, fish in enumerate(self.fish_list):
                if fish == 0:
                    new_fish_counter += 1
                    fish = 6
                else:
                    fish -= 1

                self.fish_list[idx] = fish

            self.fish_list.extend([8] * new_fish_counter)

        return len(self.fish_list)


if __name__ == '__main__':
    print('Day 6, part 1:', Solver(80).part1())
