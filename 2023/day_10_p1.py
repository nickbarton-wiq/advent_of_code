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
        if self.x-1 >= 0:
            pipe = self.data[self.x - 1][self.y]
            if pipe in ['|', '7', 'F', 'S']:
                return (self.x - 1, self.y)

    def look_south(self):
        if self.x+1 < len(self.data):
            pipe = self.data[self.x + 1][self.y]
            if pipe in ['|', 'J', 'L', 'S']:
                return (self.x + 1, self.y)

    def look_east(self):
        if self.y+1 < len(self.data[0]):
            pipe = self.data[self.x][self.y + 1]
            if pipe in ['-', 'J', '7', 'S']:
                return (self.x, self.y + 1)

    def look_west(self):
        if self.y-1 >= 0:
            pipe = self.data[self.x][self.y - 1]
            if pipe in ['-', 'L', 'F', 'S']:
                return (self.x, self.y - 1)

    def valid_moves(self):
        if self.pipe == 'S':
            moves = [self.look_north(), self.look_south(), self.look_east(), self.look_west()]
            return [move for move in moves if move is not None]
        elif self.pipe == '|':
            moves = [self.look_north(), self.look_south()]
            return [move for move in moves if move is not None]
        elif self.pipe == '-':
            moves = [self.look_east(), self.look_west()]
            return [move for move in moves if move is not None]
        elif self.pipe == 'L':
            moves = [self.look_north(), self.look_east()]
            return [move for move in moves if move is not None]
        elif self.pipe == 'J':
            moves = [self.look_north(), self.look_west()]
            return [move for move in moves if move is not None]
        elif self.pipe == '7':
            moves = [self.look_south(), self.look_west()]
            return [move for move in moves if move is not None]
        elif self.pipe == 'F':
            moves = [self.look_south(), self.look_east()]
            return [move for move in moves if move is not None]

    def __eq__(self, other):
        return self.coordinates == other.coordinates


def get_data(file) -> List[str]:
    with open(file) as f:
        return f.read().splitlines()


def create_positions(data):
    positions = {}
    for x, line in enumerate(data):
        for y in range(len(line)):
            positions[(x, y)] = Position(x, y, data)
    return positions


def get_next_position(positions, current_position, previous_position):
    next_position_candidates = current_position.valid_moves()
    for coordinate in next_position_candidates:
        next_position = positions[coordinate]
        if next_position != previous_position:
            return next_position


def find_starting_position(positions):
    for position in positions.values():
        if position.pipe == 'S':
            return position


def main():
    data = get_data('2023/day_10.input')
    positions = create_positions(data)
    pipe = [find_starting_position(positions)]

    while True:
        next_position = get_next_position(positions, pipe[-1], pipe[-2 if len(pipe) > 1 else -1])
        if next_position is not None and next_position.pipe == 'S':
            break
        pipe.append(next_position)

    return len(pipe) // 2


if __name__ == '__main__':
    print(main())
