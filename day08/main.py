
class Solver:
    def __init__(self):
        self.output_values = self.read_input()

    @staticmethod
    def read_input():
        output_values = []
        with open('input.txt') as fd:
            for line in fd.readlines():
                output_values.append(line.split('|')[1].strip().split(' '))

        return output_values

    def part1(self):
        unique_len = {2, 4, 3, 7}
        counter = 0
        for digits in self.output_values:
            for digit in digits:
                if len(digit) in unique_len:
                    counter += 1

        return counter


if __name__ == '__main__':
    print('Day 8, part 1: ', Solver().part1())
