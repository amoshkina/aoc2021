class Submarine:

    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def forward(self, shift):
        self.horizontal += shift

    def down(self, shift):
        self.depth += shift

    def up(self, shift):
        self.depth -= shift

    def run(self):
        with open("input.txt") as fd:
            commands = [line.strip().split(" ") for line in fd.readlines()]

            for cmd, shift in commands:
                getattr(self, cmd)(int(shift))


if __name__ == '__main__':
    submarine = Submarine()
    submarine.run()
    print("Day2, part 1: %s" % (submarine.horizontal * submarine.depth))
