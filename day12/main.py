from copy import deepcopy


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

    def bfs(self, paths):
        if not paths:
            return

        # cave, caves, edges = paths.pop()
        cave, caves = paths.pop()
        if cave.is_end:
            self.path_counter += 1
            return

        for next_cave in cave.connections:
            new_edge = (cave, next_cave)

            if (next_cave.name in caves and not next_cave.is_reentrable):  # or new_edge in edges:
                continue

            new_caves = deepcopy(caves)
            new_caves.add(next_cave.name)

            # new_edges = deepcopy(edges)
            # new_edges.add(new_edge)

            # paths.append((next_cave, new_caves, new_edges))
            paths.append((next_cave, new_caves))

    def part1(self):
        start = self.caves['start']
        # paths = [(start, {start.name}, set())]
        paths = [(start, {start.name})]
        while paths:
            self.bfs(paths)
        return self.path_counter


if __name__ == '__main__':
    print('Day 12, part 1: ', Solver().part1())
