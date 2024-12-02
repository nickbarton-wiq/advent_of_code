def parse_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return [[int(x) for x in line.split()] for line in lines]


def is_safe(report):
    variances = [report[level + 1] - report[level] for level in range(len(report)-1)]
    return (
        (all(v < 0 for v in variances) or all(v > 0 for v in variances))
        and all(abs(v) >= 1 and abs(v) <= 3 for v in variances)
    )


def main():
    # reports = parse_file('2024/02/example.txt')
    reports = parse_file('2024/02/input.txt')
    safe_reports = 0
    for report in reports:
        if is_safe(report):
            safe_reports += 1
        else:
            for level in range(len(report)):
                dampened = [x for i, x in enumerate(report) if i != level]
                if is_safe(dampened):
                    safe_reports += 1
                    break

    print(f"{safe_reports=}")


if __name__ == '__main__':
    main()
