
def part1(lines):
    counters = [{'0': 0, '1': 0} for _ in range(len(lines[0].strip()))]

    for binary in lines:
        for idx, digit in enumerate(binary.strip()):
            counters[idx][digit] += 1

    gamma, epsilon = [], []
    for counter in counters:
        gamma.append('0' if counter['0'] > counter['1'] else '1')
        epsilon.append('1' if counter['0'] > counter['1'] else '0')

    return int(''.join(gamma), 2) * int(''.join(epsilon), 2)


if __name__ == '__main__':
    with open('input.txt') as fd:
        lines = fd.readlines()

        print('Day 1, part 1: %s' % part1(lines))
