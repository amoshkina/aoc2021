class Solver(object):
  HEX_MAP = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
  }

  def __init__(self):
    self.message = self.read_input()
    self.expr = []
    self.versions = []

    self.OP_TYPE = {
      0: self.sum,
      1: self.mul,
      2: self.min,
      3: self.max,
      5: self.gt,
      6: self.lt,
      7: self.eq
    }

  def read_input(self):
    with open('input.txt') as fd:
      result = []
      for hex_value in list(fd.read().strip()):
        result.append(self.HEX_MAP[hex_value])

    return ''.join(result)

  def parse_literal(self, literal):
    start = 0
    number = []
    while literal[start] == '1':
      number.append(literal[start+1:start+5])
      start += 5

    number.append(literal[start+1:start+5])
    self.expr.append(int(''.join(number), 2))

    start += 5
    return start

  def parse_next_packet(self, message):
    start = 0
    # versions = []
    if '1' not in message:
      # this is the remainder of the message containing only 0s
      return len(message)

    p_version, p_type = message[start:start + 3], message[start + 3:start + 6]
    self.versions.append(int(p_version, 2))

    if p_type == '100':
      literal_len = self.parse_literal(message[start+6:])
      start += 6 + literal_len
    else:
      self.expr.append('(')
      self.expr.append(self.OP_TYPE[int(p_type, 2)])
      len_type_idx = start + 6
      if message[len_type_idx] == '0':
        operands_len = int(message[len_type_idx + 1:len_type_idx + 16], 2)
        self.parse_message(message[len_type_idx + 16:len_type_idx + 16 + operands_len])
        start += len_type_idx + 16 + operands_len
      else:  # self.message[len_type_idx] == 1
        packets_num = int(message[len_type_idx + 1:len_type_idx+12], 2)
        start = len_type_idx+12

        for _ in range(packets_num):
          start_add = self.parse_next_packet(message[start:])
          start += start_add

      self.expr.append(')')
    return start

  def parse_message(self, message):
    start = 0
    while start < len(message):
      start_add = self.parse_next_packet(message[start:])
      start += start_add

  def sum(self, *args):
    return sum(args)

  def mul(self, *args):
    return reduce(lambda x, y: x*y, args)

  def min(self, *args):
    return min(args)

  def max(self, *args):
    return max(args)

  def gt(self, x, y):
    return 1 if x > y else 0

  def lt(self, x, y):
    return 1 if x < y else 0

  def eq(self, x, y):
    return 1 if x == y else 0

  def eval(self, expr):
    args = []
    while len(expr) > 1:
      item = expr.pop()
      if isinstance(item, int):
        args.append(item)
      else:
        expr.append(item(*args))
        args = []

    return expr.pop()

  def part1(self):
    self.parse_message(self.message)
    return sum(self.versions)

  def part2(self):
    self.parse_message(self.message)
    # print(self.expr)
    return self.eval(self.expr)


if __name__ == '__main__':
  # print('Day 16, part 1: %s' % Solver().part1())
  print('Day 16, part 2: %s' % Solver().part2())
