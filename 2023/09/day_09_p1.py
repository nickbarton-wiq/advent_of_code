from typing import List
from copy import deepcopy


def get_data(file) -> List[str]:
    with open(file) as f:
        return f.read().splitlines()


class Report:
    def __init__(self, data: str):
        self.data = [[int(x) for x in data.split()]]

    def rev(self):
        self.data[0].reverse()

    def get_data(self):
        self.report = deepcopy(self.data)
        while True:
            lst = self.report[-1]
            a = [lst[i:i+2] for i in range(len(lst)) if len(lst[i:i+2]) == 2]
            b = [x[1] - x[0] for x in a]
            self.report.append(b)
            if all([x == 0 for x in b]):
                break
        return self

    def make_predictions(self):
        for i in range(len(self.report)-1, 0, -1):
            self.report[i-1].append(self.report[i][-1] + self.report[i-1][-1])
        return self

    def result(self):
        return self.report[0][-1]


def main():
    data = get_data('2023/day_09.input')

    reports = [Report(line) for line in data]

    output = []
    for report in reports:
        report.get_data().make_predictions()
        output.append(report.result())

    return sum(output)


if __name__ == '__main__':
    print(main())
