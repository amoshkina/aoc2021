from collections import defaultdict
from copy import copy


class Cave:
    def __init__(self, name):
        self.name = name
        self.connections = set()

    @property
    def is_start(self):
        return self.name == 'start'

    @property
    def is_end(self):
        return self.name == 'end'

    @property
    def is_reentrable(self):
        if self.name.lower() != self.name:
            return True

        return False

    def __repr__(self):
        return '%s [%s]' % (self.name, ','.join(cave.name for cave in self.connections))


class Solver:
    def __init__(self):
        self.caves = {}
        self.read_input()
        self.path_counter = 0

    def get_cave(self, name):
        if name not in self.caves:
            cave = Cave(name)
            self.caves[name] = cave

        return self.caves[name]

    def read_input(self):
        with open('input.txt') as fd:
            for line in fd.readlines():
                name1, name2 = line.strip().split('-')
                cave1 = self.get_cave(name1)
                cave2 = self.get_cave(name2)
                cave1.connections.add(cave2)
                cave2.connections.add(cave1)

    def bfs(self, paths, reentrance):
        if not paths:
            return

        cave, caves = paths.pop()
        if cave.is_end:
            self.path_counter += 1
            return

        for next_cave in cave.connections:
            visited = [
                name for name, visits in caves.items()
                if visits == reentrance and name.lower() == name
            ]

            cond = (
                next_cave.name not in caves or
                next_cave.is_reentrable or
                (not visited and not next_cave.is_start and not next_cave.is_end)
            )

            if cond:
                new_caves = copy(caves)
                new_caves[next_cave.name] += 1
                paths.append((next_cave, new_caves))

    def bfs_init(self, reentrance):
        start = self.caves['start']
        caves = defaultdict(int)
        caves[start.name] += 1
        paths = [(start, caves)]
        while paths:
            self.bfs(paths, reentrance)
        return self.path_counter

    def part1(self):
        return self.bfs_init(1)

    def part2(self):
        return self.bfs_init(2)


if __name__ == '__main__':
    print('Day 12, part 1: ', Solver().part1())
    print('Day 12, part 2: ', Solver().part2())
