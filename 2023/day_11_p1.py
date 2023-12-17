from typing import List


class GalaxyMap:
    def __init__(self, data):
        self.data = data

    def expand_galaxy(self):
        for i, row in enumerate(self.data):
            print(row)
            if set(row) == {'.'}:
                self.data.insert(i-1, ['.' for _ in range(len(row))])
                i += 1
        print(self.data)

        for i in range(len(self.data[0])):
            col = [x[i] for x in self.data]
            print(col)


def get_data(file) -> List[str]:
    with open(file) as f:
        return f.read().splitlines()


def main():
    data = get_data('2023/day_11.input')
    galaxy = GalaxyMap(data)
    galaxy.expand_galaxy()
    return


if __name__ == '__main__':
    print(main())
