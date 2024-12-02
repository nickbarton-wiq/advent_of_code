def parse_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return [[int(x) for x in line.split()] for line in lines]


def main():
    # reports = parse_file('2024/02/example.txt')
    reports = parse_file('2024/02/input.txt')
    safe_reports = 0
    for report in reports:
        variances = [report[level + 1] - report[level] for level in range(len(report)-1)]
        if (
            (all(v < 0 for v in variances) or all(v > 0 for v in variances))
            and all(abs(v) >= 1 and abs(v) <= 3 for v in variances)
        ):
            safe_reports += 1

    print(f"{safe_reports=}")


if __name__ == '__main__':
    main()
