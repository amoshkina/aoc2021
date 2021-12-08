from collections import defaultdict


class Solver:
    VALID_MAPPING = {
        'abcefg': '0',
        'cf': '1',
        'acdeg': '2',
        'acdfg': '3',
        'bcdf': '4',
        'abdfg': '5',
        'abdefg': '6',
        'acf': '7',
        'abcdefg': '8',
        'abcdfg': '9'
    }

    def __init__(self):
        self.signal_patterns, self.output_values = self.read_input()

    @staticmethod
    def read_input():
        output_values, signal_patterns = [], []
        with open('input.txt') as fd:
            for line in fd.readlines():
                signal, output = [item.strip().split(' ') for item in line.split('|')]
                signal_patterns.append(signal)
                output_values.append(output)

        return signal_patterns, output_values

    def part1(self):
        unique_len = {2, 4, 3, 7}
        counter = 0
        for digits in self.output_values:
            for digit in digits:
                if len(digit) in unique_len:
                    counter += 1

        return counter

    @staticmethod
    def symm_diff_3(a, b, c):
        return (a ^ b) | (b ^ c) | (a ^ c)

    def untangle_wires(self, signals):
        signal_map = defaultdict(list)
        for signal in signals:
            signal_map[len(signal)].append(set(signal))

        signal_map = dict(signal_map)

        diff_6 = self.symm_diff_3(signal_map[6][0], signal_map[6][1], signal_map[6][2])
        e_g = signal_map[7][0] - signal_map[3][0] - signal_map[4][0]
        b_d = signal_map[4][0] - signal_map[2][0]

        wires_mapping = {
            (signal_map[3][0] - signal_map[2][0]).pop(): 'a',
            (b_d - (b_d & diff_6)).pop(): 'b',
            (signal_map[2][0] & diff_6).pop(): 'c',
            (b_d & diff_6).pop(): 'd',
            (e_g & diff_6).pop(): 'e',
            (e_g - (e_g & diff_6)).pop(): 'g',
        }
        wires_mapping[(set('abcdefg') - set(wires_mapping.keys())).pop()] = 'f'

        return wires_mapping

    def part2(self):
        values = []
        for idx, signals in enumerate(self.signal_patterns):
            wires_mapping = self.untangle_wires(signals)

            value = []
            for digit in self.output_values[idx]:
                acc = []
                for ch in digit:
                    acc.append(wires_mapping[ch])

                value.append(''.join(self.VALID_MAPPING[''.join(sorted(acc))]))

            values.append(int(''.join(value)))

        return sum(values)


if __name__ == '__main__':
    print('Day 8, part 1: ', Solver().part1())
    print('Day 8, part 2: ', Solver().part2())
