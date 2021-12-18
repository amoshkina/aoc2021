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

  def read_input(self):
    with open('input.txt') as fd:
      result = []
      for hex_value in list(fd.read().strip()):
        result.append(self.HEX_MAP[hex_value])

    return ''.join(result)

  def parse_literal(self, literal):
    start = 0
    while literal[start] == '1':
      start += 5

    start += 5
    return start

  def parse_next_packet(self, message):
    start = 0
    versions = []
    if '1' not in message:
      # this is the remainder of the message containing only 0s
      return len(message), versions

    p_version, p_type = message[start:start + 3], message[start + 3:start + 6]
    versions.append(int(p_version, 2))

    if p_type == '100':
      literal_len = self.parse_literal(message[start+6:])
      start += 6 + literal_len
    else:
      len_type_idx = start + 6
      if message[len_type_idx] == '0':
        operands_len = int(message[len_type_idx + 1:len_type_idx + 16], 2)
        versions_add = self.parse_message(message[len_type_idx + 16:len_type_idx + 16 + operands_len])
        versions.extend(versions_add)
        start += len_type_idx + 16 + operands_len
      else:  # self.message[len_type_idx] == 1
        packets_num = int(message[len_type_idx + 1:len_type_idx+12], 2)
        start = len_type_idx+12

        for _ in range(packets_num):
          start_add, versions_add = self.parse_next_packet(message[start:])
          start += start_add
          versions.extend(versions_add)

    return start, versions

  def parse_message(self, message):
    start = 0
    versions = []
    while start < len(message):
      start_add, versions_add = self.parse_next_packet(message[start:])
      start += start_add
      versions.extend(versions_add)

    return versions

  def part1(self):
    return sum(self.parse_message(self.message))


if __name__ == '__main__':
  print('Day 16, part 1: %s' % Solver().part1())
