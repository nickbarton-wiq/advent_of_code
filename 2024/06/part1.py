def parse_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return process_file(lines)


class Positions:
    def __init__(self, length, width, obstacles=[], starting_pos=None):
        self.length = length
        self.width = width
        self.obstacles = obstacles
        self.starting_pos = starting_pos


def process_file(lines):

    positions = Positions(
        length=len(lines),
        width=len(lines[0]),
    )
    for x, line in enumerate(lines):
        for y, indicator in enumerate(line):
            if indicator == "#":
                positions.obstacles.append((x, y))
            elif indicator == '^':
                positions.starting_pos = (x, y)
    return positions


def up(x, y):
    return (x - 1, y)


def down(x, y):
    return (x + 1, y)


def left(x, y):
    return (x, y - 1)


def right(x, y):
    return (x, y + 1)


def turn_right(current_dir):
    if current_dir == up:
        return right
    elif current_dir == right:
        return down
    elif current_dir == down:
        return left
    elif current_dir == left:
        return up


def on_map(pos, length, width):
    return pos[0] >= 0 and pos[0] < length and pos[1] >= 0 and pos[1] < width


def main():
    # positions = parse_file("2024/06/example.txt")
    positions = parse_file("2024/06/input.txt")

    visited = set()
    current_dir = up
    pos = positions.starting_pos
    visited.add(pos)
    while True:
        next_pos = current_dir(*pos)  # type: ignore
        if next_pos in positions.obstacles:
            current_dir = turn_right(current_dir)
        else:
            pos = next_pos
        if not on_map(pos, positions.length, positions.width):
            break
        visited.add(pos)
    return len(visited)


if __name__ == '__main__':
    print(main())
