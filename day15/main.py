import heapq


class Cost:
  def __init__(self, x, y, value):
    self.x = x
    self.y = y
    self.value = value

  def __lt__(self, other):
    return self.value < other.value

  def __gt__(self, other):
    return self.value > other.value


class Solver:
  def __init__(self):
    self.matrix = self.read_input()
    self.x_max = len(self.matrix)
    self.y_max = len(self.matrix[0])
    self.cost_matrix = [[float('inf')] * self.y_max for _ in range(self.x_max)]
    self.cost_matrix[0][0] = 0

  @staticmethod
  def read_input():
    matrix = []
    with open('input.txt') as fd:
      for i, line in enumerate(fd.readlines()):
        matrix.append(map(int, list(line.strip())))

    return matrix

  def part1(self):
    self.cost_matrix[0][0] = 0
    self.cost_matrix[0][1] = self.matrix[0][1]
    self.cost_matrix[1][0] = self.matrix[1][0]

    pqueue = []
    heapq.heappush(pqueue, Cost(0, 1, self.cost_matrix[0][1]))
    heapq.heappush(pqueue, Cost(1, 0, self.cost_matrix[1][0]))

    known = {(0, 0)}

    while pqueue:
      cost = heapq.heappop(pqueue)
      i, j = cost.x, cost.y

      if (i, j) in known:
        continue

      neighbours = [
        (i-1, j), (i+1, j),
        (i, j-1), (i, j+1)
      ]

      for x, y in neighbours:
        if 0 <= x < self.x_max and 0 <= y < self.y_max:
          self.cost_matrix[x][y] = min(
            self.cost_matrix[x][y],
            self.cost_matrix[i][j] + self.matrix[x][y]
          )
          if (x, y) not in known:
            heapq.heappush(pqueue, Cost(x, y, self.cost_matrix[x][y]))
      known.add((i, j))

    return self.cost_matrix[self.x_max-1][self.y_max-1]


if __name__ == '__main__':
  print('Day 15, part 1: %s' % Solver().part1())
