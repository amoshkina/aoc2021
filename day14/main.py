from collections import defaultdict


class Elem:
    def __init__(self, value, prev=None, nxt=None):
        self.value = value
        self.prev = prev
        self.next = nxt


class Solver:
    def __init__(self):
        self.line_polymer, self.polymer, self.rules = self.read_input()

    @staticmethod
    def build_polymer(chain):
        if not chain:
            return

        head = Elem(chain[0])
        current = head
        for value in chain[1:]:
            elem = Elem(value, prev=current)
            current.next = elem
            current = elem

        return head

    def read_input(self):
        rules = {}
        polymer = None
        line_polymer = None
        with open('input.txt') as fd:
            for line in fd.readlines():
                line = line.strip()
                if not line:
                    continue
                elif ' -> ' not in line:
                    line_polymer = line
                    polymer = self.build_polymer(line)
                else:
                    pair, elem = line.strip().split(' -> ')
                    rules[pair] = elem

        return line_polymer, polymer, rules

    def print_polymer(self):
        current = self.polymer
        chain = []
        while current:
            chain.append(current.value)
            current = current.next

        print(''.join(chain))

    def score(self):
        current = self.polymer
        frequency = defaultdict(int)
        while current:
            frequency[current.value] += 1
            current = current.next

        values = set(frequency.values())
        return max(values) - min(values)

    def run(self, steps):
        for _ in range(steps):
            current = self.polymer
            while current.next:
                nxt = current.next
                pair = current.value + nxt.value
                if pair in self.rules:
                    elem = Elem(self.rules[pair], prev=current, nxt=nxt)
                    current.next = elem
                    nxt.prev = elem

                current = nxt

            self.print_polymer()

    def part1(self):
        self.run(10)
        return self.score()

    def part2(self):
        pairs = defaultdict(int)
        idx = 0
        while idx + 1 < len(self.line_polymer):
            pairs[self.line_polymer[idx:idx+2]] += 1
            idx += 1

        for _ in range(40):
            new_pairs = defaultdict(int)
            for pair, number in pairs.items():
                if pair not in self.rules:
                    new_pairs[pair] = number
                else:
                    middle = self.rules[pair]
                    new_pairs[pair[0]+middle] += number
                    new_pairs[middle+pair[1]] += number

            pairs = new_pairs

        print(pairs)

        score = defaultdict(int)
        for pair, number in pairs.items():
            score[pair[0]] += number
            score[pair[1]] += number

        score[self.line_polymer[0]] += 1
        score[self.line_polymer[-1]] += 1

        values = list(map(lambda value: value/2, score.values()))

        return max(values) - min(values)




if __name__ == '__main__':
    print('Day 14, part 1: ', Solver().part1())
    print('Day 14, part 2: ', Solver().part2())
