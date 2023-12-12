from typing import List


class Position:
    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.data = data

    @property
    def coordinates(self):
        return (self.x, self.y)

    @property
    def pipe(self):
        return self.data[self.x][self.y]

    def look_north(self):
        pipe = self.data[self.x - 1][self.y]
        if pipe in ['|', '7', 'F', 'S']:
            return (self.x - 1, self.y)

    def look_south(self):
        pipe = self.data[self.x + 1][self.y]
        if pipe in ['|', 'J', 'L' 'S']:
            return (self.x + 1, self.y)

    def look_east(self):
        pipe = self.data[self.x][self.y + 1]
        if pipe in ['-', 'J', '7', 'S']:
            return (self.x, self.y + 1)

    def look_west(self):
        pipe = self.data[self.x][self.y - 1]
        if pipe in ['-', 'L', 'F' 'S']:
            return (self.x, self.y - 1)

    def look_around(self):
        return [self.look_north(), self.look_south(), self.look_east(), self.look_west()]

    def valid_moves(self):
        return [move for move in self.look_around() if move in ('|', '-', 'L', 'J', '7', 'F', 'S')]


def get_data(file) -> List[str]:
    with open(file) as f:
        return f.read().splitlines()


def create_positions(data):
    positions = {}
    for x, line in enumerate(data):
        for y, pipe in enumerate(line):
            positions[(x, y)] = Position(x, y, data)
    return positions


def get_next_position(positions, previous_position):
    for move in previous_position.valid_moves():
        print(move)
        x = positions(move.coordinates)
        print(x)
        if x != previous_position:
            next_move = x
            print(next_move)
            return next_move


def find_starting_position(positions):
    for position in positions.values():
        if position.pipe == 'S':
            return position


def main():
    data = get_data('2023/day_10.sample')
    positions = create_positions(data)
    pipe = [find_starting_position(positions)]

    while True:
        next_position = get_next_position(positions, pipe[-1])
        print(next_position.coordinates)
        if next_position.pipe == 'S':
            break
        pipe.append(next_position)
        print(pipe)


if __name__ == '__main__':
    print(main())
