from typing import List


class Galaxy:
    def __init__(self, id: int, x: int, y: int):
        self.id: int = id
        self.x: int = x
        self.y: int = y
        self.coordinwtes: tuple = (x, y)

    def __eq__(self, other) -> bool:
        return self.id == other.id

    def __ne__(self, other) -> bool:
        return self.id != other.id

    def __gt__(self, other) -> bool:
        return self.id > other.id

    def __lt__(self, other) -> bool:
        return self.id < other.id

    def __hash__(self) -> int:
        return self.id


class GalaxyMap:
    def __init__(self, file: str):
        self.file = file
        self.get_map()

    def get_map(self):
        self.map: List = []
        with open(self.file) as f:
            map = f.read().splitlines()
            for row in map:
                self.map.append([x for x in row])

    def expand_galaxy(self):
        self._expand_rows()
        self._expand_columns()

    def _expand_rows(self):
        rows_to_insert = []
        for i, row in enumerate(self.map):
            if set(row) == {'.'}:
                rows_to_insert.append(i)

        while len(rows_to_insert) > 0:
            row = rows_to_insert.pop()
            self.map.insert(row, ['.' for _ in self.map[0]])

    def _expand_columns(self):
        columns_to_insert = []
        for i in range(len(self.map[0])):
            if set([row[i] for row in self.map]) == {'.'}:
                columns_to_insert.append(i)

        while len(columns_to_insert) > 0:
            column = columns_to_insert.pop()
            for i, row in enumerate(self.map):
                row.insert(column, '.')
                self.map[i] = row

    def find_galaxies(self):
        galaxy_id = 0
        self.galaxies = {}
        for x, row in enumerate(self.map):
            for y, column in enumerate(row):
                if column == '#':
                    self.galaxies[galaxy_id] = Galaxy(galaxy_id, x, y)
                    galaxy_id += 1

    def find_galaxy_combinations(self):
        """finds the combinations of galaxies, Only counta each pair once; order within the pair doesn't matter"""
        self.galaxy_combinations = set()
        for galaxy_1 in self.galaxies.values():
            for galaxy_2 in self.galaxies.values():
                if galaxy_1 != galaxy_2:
                    self.galaxy_combinations.add(tuple(sorted([galaxy_1, galaxy_2])))

    def calculate_distance(self, galaxy_1: Galaxy, galaxy_2: Galaxy):
        # abs(x1 - x2) + abs(y1 - y2)
        return abs(galaxy_1.x - galaxy_2.x) + abs(galaxy_1.y - galaxy_2.y)

    def find_distances(self):
        distances = {}
        for combination in self.galaxy_combinations:
            galaxy_1, galaxy_2 = combination
            distances[combination] = self.calculate_distance(galaxy_1, galaxy_2)

        distances = [distances[combination] for combination in self.galaxy_combinations]
        return sum(distances)


def main():
    galaxy_map = GalaxyMap('2023/11/input.txt')
    galaxy_map.expand_galaxy()
    galaxy_map.find_galaxies()
    galaxy_map.find_galaxy_combinations()
    return galaxy_map.find_distances()


if __name__ == '__main__':
    print(main())
