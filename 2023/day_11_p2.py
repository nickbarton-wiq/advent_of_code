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
        self.map = self.get_map()
        self.blank_rows = self._get_blank_rows()
        self.blank_columns = self._get_blank_columns()

        self.expansion_rate = 999999

    def get_map(self):
        map: List = []
        with open(self.file) as f:
            map_rows = f.read().splitlines()
            for row in map_rows:
                map.append([x for x in row])
        return map

    def expand_galaxy(self):
        self._expand_rows()
        self._expand_columns()

    def _get_blank_rows(self):
        blank_rows = []
        for i, row in enumerate(self.map):
            if set(row) == {'.'}:
                blank_rows.append(i)
        return blank_rows

    def _get_blank_columns(self):
        blank_columns = []
        for i in range(len(self.map[0])):
            if set([row[i] for row in self.map]) == {'.'}:
                blank_columns.append(i)
        return blank_columns

    def _expand_rows(self):
        while len(self.blank_rows) > 0:
            row_to_expand = self.blank_rows.pop()
            for galaxy in self.galaxies.values():
                if galaxy.x >= row_to_expand:
                    galaxy.x += self.expansion_rate

    def _expand_columns(self):
        while len(self.blank_columns) > 0:
            column_to_expand = self.blank_columns.pop()
            for galaxy in self.galaxies.values():
                if galaxy.y >= column_to_expand:
                    galaxy.y += self.expansion_rate

    def find_galaxies(self):
        galaxy_id = 1
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
        return abs(galaxy_1.x - galaxy_2.x) + abs(galaxy_1.y - galaxy_2.y)

    def calculate_distances(self):
        self.distances = {}
        for combination in self.galaxy_combinations:
            galaxy_1, galaxy_2 = combination
            self.distances[combination] = self.calculate_distance(galaxy_1, galaxy_2)

    def calculate_total_distance(self):
        distances = [self.distances[combination] for combination in self.galaxy_combinations]
        return sum(distances)

    def find_distance(self, galaxy_1: int, galaxy_2: int):
        galaxy_1 = self.galaxies[galaxy_1]
        galaxy_2 = self.galaxies[galaxy_2]
        return self.distances[tuple(sorted([galaxy_1, galaxy_2]))]


def main():
    galaxy_map = GalaxyMap('2023/day_11.input')
    galaxy_map.find_galaxies()
    galaxy_map.expand_galaxy()
    galaxy_map.find_galaxy_combinations()
    galaxy_map.calculate_distances()

    # galaxy_map.find_distance(1, 7)
    return galaxy_map.calculate_total_distance()


if __name__ == '__main__':
    print(main())
