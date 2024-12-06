from multiprocessing import Pool
from copy import deepcopy


def parse_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return process_file(lines)


class Positions:
    def __init__(self, length, width, starting_pos=None):
        self.length = length
        self.width = width
        self.obstacles = set()
        self.starting_pos = starting_pos


def process_file(lines):

    positions = Positions(
        length=len(lines),
        width=len(lines[0]),
    )
    for x, line in enumerate(lines):
        for y, indicator in enumerate(line):
            if indicator == "#":
                positions.obstacles.add((x, y))
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


def generate_path(positions):
    path = set()
    current_dir = up
    pos = positions.starting_pos
    path.add(pos)
    while True:
        next_pos = current_dir(*pos)  # type: ignore
        if next_pos in positions.obstacles:
            current_dir = turn_right(current_dir)
        else:
            pos = next_pos
        if not on_map(pos, positions.length, positions.width):
            break
        path.add(pos)
    path.remove(positions.starting_pos)
    print("total obstacle options:", len(path))
    return path


def process_obstacle(args):
    positions, new_obstacle = args
    positions.obstacles.add(new_obstacle)
    visited = set()
    current_dir = up
    pos = positions.starting_pos
    visited.add((pos, current_dir))

    while True:
        next_pos = current_dir(*pos)  # type: ignore
        if next_pos in positions.obstacles:
            current_dir = turn_right(current_dir)
        else:
            pos = next_pos

        if not on_map(pos, positions.length, positions.width):
            return False
        elif (pos, current_dir) in visited:
            return True
        else:
            visited.add((pos, current_dir))


def main():
    # positions = parse_file("2024/06/example.txt")
    positions = parse_file("2024/06/input.txt")

    path = generate_path(deepcopy(positions))
    with Pool() as pool:
        args = [(deepcopy(positions), obstacle) for obstacle in path]
        results = pool.map(process_obstacle, args)

    possible_obstacles_positions = sum(1 for result in results if result)
    return f"{possible_obstacles_positions=}"


if __name__ == '__main__':
    print(main())
