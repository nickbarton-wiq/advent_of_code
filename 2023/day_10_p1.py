from typing import List


def get_data(file) -> List[str]:
    with open(file) as f:
        return f.read().splitlines()


def find_start(data):
    return [(x, line.index('S')) for x, line in enumerate(data) if 'S' in line][0]


def main():
    data = get_data('2023/day_10.input')
    start = find_start(data)
    print(start)


if __name__ == '__main__':
    print(main())
