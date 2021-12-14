from collections import defaultdict


class Elem:
    def __init__(self, value, prev=None, nxt=None):
        self.value = value
        self.prev = prev
        self.next = nxt


class Solver:
    def __init__(self):
        self.polymer, self.rules = self.read_input()

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

        with open('input.txt') as fd:
            for line in fd.readlines():
                line = line.strip()
                if not line:
                    continue
                elif ' -> ' not in line:
                    polymer = self.build_polymer(line)
                else:
                    pair, elem = line.strip().split(' -> ')
                    rules[pair] = elem

        return polymer, rules

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

    def part1(self):

        for _ in range(10):
            current = self.polymer
            while current.next:
                nxt = current.next
                pair = current.value + nxt.value
                if pair in self.rules:
                    elem = Elem(self.rules[pair], prev=current, nxt=nxt)
                    current.next = elem
                    nxt.prev = elem

                current = nxt

        return self.score()


if __name__ == '__main__':
    print('Day 14, part 1: ', Solver().part1())
