from collections import deque


class Octopus:
    def __init__(self, energy, x, y):
        self.energy = energy
        self.x = x
        self.y = y
        self.flashed = False

    def __repr__(self):
        return "{} ({}, {})".format(self.energy, self.x, self.y)


class Solver:
    def __init__(self):
        self.matrix = self.read_input()
        self.max_idx = 10

    @staticmethod
    def read_input():
        matrix = []
        with open('input.txt') as fd:
            for i, line in enumerate(fd.readlines()):
                row = []
                for j, energy in enumerate(line.strip()):
                    row.append(Octopus(int(energy), i, j))

                matrix.append(row)

        return matrix

    def flash(self, to_flash):
        while len(to_flash) > 0:
            octopus = to_flash.popleft()
            if octopus.flashed:
                continue

            octopus.flashed = True
            for i in range(octopus.x-1, octopus.x+2):
                for j in range(octopus.y-1, octopus.y+2):
                    if i == octopus.x and j == octopus.y:
                        continue

                    if 0 <= i < self.max_idx and 0 <= j < self.max_idx:
                        neighbour = self.matrix[i][j]
                        neighbour.energy += 1
                        if neighbour.energy > 9 and not neighbour.flashed:
                            to_flash.append(neighbour)

    def part1(self):
        counter = 0
        for step in range(100):
            to_flash = deque()
            # 1. increment all octopuses' energy by one
            for row in self.matrix:
                for octopus in row:
                    octopus.energy += 1
                    if octopus.energy > 9:
                        to_flash.append(octopus)

            # 2. flashing octopuses
            self.flash(to_flash)

            # 3. reset flashed octopuses
            for row in self.matrix:
                for octopus in row:
                    if octopus.flashed:
                        counter += 1
                        octopus.flashed = False
                        octopus.energy = 0

        return counter


if __name__ == '__main__':
    print('Day 11, part 1: ', Solver().part1())
