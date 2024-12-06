from multiprocessing import Pool
from copy import deepcopy


def parse_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return process_file(lines)


def process_file(lines):

    map = Map(
        length=len(lines),
        width=len(lines[0]),
    )
    for x, line in enumerate(lines):
        for y, indicator in enumerate(line):
            if indicator == "#":
                map.obstacles.add((x, y))
            elif indicator == '^':
                map.starting_pos = (x, y)
    return map


class Map:
    def __init__(self, length, width, starting_pos=None):
        self.length = length
        self.width = width
        self.obstacles = set()
        self.starting_pos = starting_pos

    def on_map(self, pos):
        return pos[0] >= 0 and pos[0] < self.length and pos[1] >= 0 and pos[1] < self.width


class Guard:
    def __init__(self, position, map):
        self.position = position
        self.map = map
        self.direction = self.up
        self.path = {self.position}
        self.visited = {(self.position, self.direction)}

    def up(self):
        return (self.position[0] - 1, self.position[1])

    def down(self):
        return (self.position[0] + 1, self.position[1])

    def left(self):
        return (self.position[0], self.position[1] - 1)

    def right(self):
        return (self.position[0], self.position[1] + 1)

    def turn_right(self):
        if self.direction == self.up:
            return self.right
        elif self.direction == self.right:
            return self.down
        elif self.direction == self.down:
            return self.left
        elif self.direction == self.left:
            return self.up

    def move_on_map(self):
        next_pos = self.direction()  # type: ignore
        if next_pos in self.map.obstacles:
            self.direction = self.turn_right()
        else:
            self.position = next_pos
            self.path.add(self.position)
        return self.map.on_map(self.position)

    def add_to_visited(self):
        self.visited.add((self.position, self.direction))  # type: ignore

    def entering_loop(self):
        return (self.position, self.direction) in self.visited


def generate_obstacles(map):
    guard = Guard(map.starting_pos, map)
    while True:
        if not guard.move_on_map():
            break
    guard.path.remove(map.starting_pos)
    print("total obstacle options:", len(guard.path))
    return guard.path


def move_guard(args):
    map, new_obstacle = args
    map.obstacles.add(new_obstacle)
    guard = Guard(map.starting_pos, map)
    while True:
        if not guard.move_on_map():
            return False
        elif guard.entering_loop():
            return True
        else:
            guard.add_to_visited()


def main():
    # map = parse_file("2024/06/example.txt")
    map = parse_file("2024/06/input.txt")
    with Pool() as pool:
        args = [(deepcopy(map), obstacle) for obstacle in generate_obstacles(deepcopy(map))]
        results = pool.map(move_guard, args)
    return f"{sum(1 for result in results if result)}"


if __name__ == '__main__':
    print(main())
