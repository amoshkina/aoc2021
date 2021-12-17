import heapq
from copy import copy


class Cost:
  def __init__(self, x, y, value):
    self.x = x
    self.y = y
    self.value = value

  def __lt__(self, other):
    return self.value < other.value

  def __gt__(self, other):
    return self.value > other.value


class Solver1(object):
  def __init__(self):
    self.matrix = self.read_input()
    self.x_max = len(self.matrix)
    self.y_max = len(self.matrix[0])
    self.cost_matrix = [[float('inf')] * self.y_max for _ in range(self.x_max)]
    self.cost_matrix[0][0] = 0

  def read_input(self):
    matrix = []
    with open('input.txt') as fd:
      for i, line in enumerate(fd.readlines()):
        matrix.append(map(int, list(line.strip())))

    return matrix

  def solve(self):
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


class Solver2(Solver1):
  def read_input(self):
    matrix = super(Solver2, self).read_input()
    new_matrix = []

    x_max = len(matrix)
    for row in matrix:
      new_row = copy(row)
      for step in range(1, 5):
        for value in row:
          new_row.append(sum(divmod(value + step, 10)))

      new_matrix.append(new_row)

    for step in range(1, 5):
      for i, row in enumerate(new_matrix):
        if i >= x_max:
          break

        new_row = []
        for value in row:
          new_row.append(sum(divmod(value + step, 10)))

        new_matrix.append(new_row)

    return new_matrix


if __name__ == '__main__':
  print('Day 15, part 1: %s' % Solver1().solve())
  print('Day 15, part 2: %s' % Solver2().solve())
