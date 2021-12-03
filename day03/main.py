
class Solver:

    def __init__(self, lines):
        self.binaries = [line.strip() for line in lines]
        self.binary_len = len(self.binaries[0])

    def _frequency(self, binaries):
        counters = [{'0': 0, '1': 0} for _ in range(self.binary_len)]

        for binary in binaries:
            for idx, digit in enumerate(binary.strip()):
                counters[idx][digit] += 1

        return counters

    @staticmethod
    def _max_min(counter):
        # default values when frequency is the same
        _max, _min = '1', '0'
        if counter['0'] > counter['1']:
            _max, _min = '0', '1'

        return _max, _min

    def _get_rating(self, binaries, bit_criteria):
        for idx in range(self.binary_len):
            if len(binaries) == 1:
                break

            counter = self._frequency(binaries)[idx]
            filter_value = self._max_min(counter)[bit_criteria]
            binaries = list(filter(lambda item: item[idx] == filter_value, binaries))

        assert len(binaries) == 1
        return binaries.pop()

    def part1(self):
        gamma, epsilon = [], []
        for counter in self._frequency(self.binaries):
            _max, _min = self._max_min(counter)
            gamma.append(_max)
            epsilon.append(_min)

        return int(''.join(gamma), 2) * int(''.join(epsilon), 2)

    def part2(self):
        oxygen = self._get_rating(self.binaries.copy(), 0)
        co2 = self._get_rating(self.binaries.copy(), 1)

        return int(oxygen, 2) * int(co2, 2)


if __name__ == '__main__':
    with open('input.txt') as fd:
        solver = Solver(fd.readlines())

        print('Day 3, part 1: %s' % solver.part1())
        print('Day 3, part 2: %s' % solver.part2())
