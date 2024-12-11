def parse_file(filename: str):
    with open(filename) as f:
        lines = f.read().splitlines()
    return process_lines(lines)


def process_lines(lines: list) -> list:
    return lines


def main():
    # lines = parse_file("2024/08/example.txt")
    lines = parse_file("2024/08/input.txt")

    length = len(lines)
    width = len(lines[0])

    antennas = {}
    coords = set()
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            coords.add((x, y))
            if char != '.':
                antennas[(x, y)] = char

    antinodes = set()
    for coord, signal in antennas.items():
        for other in [coords for coords, s in antennas.items() if s == signal]:
            if other == coord:
                continue
            for i in range(max(length, width)):
                a1 = (coord[0] + i * (coord[0] - other[0]), coord[1] + i * (coord[1] - other[1]))
                if a1 in coords:
                    antinodes.add(a1)
                a2 = (coord[0] - i * (coord[0] - other[0]), coord[1] - i * (coord[1] - other[1]))
                if a2 in coords:
                    antinodes.add(a2)
    return len(antinodes)


if __name__ == "__main__":
    print(main())
