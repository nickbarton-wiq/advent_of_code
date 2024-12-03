import re


def parse_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return ''.join(lines)


def main():
    output = 0
    # instructions = parse_file('2024/03/example.txt')
    instructions = parse_file('2024/03/input.txt')
    multiples = re.findall(r'mul\(\d{1,3},\d{1,3}\)', instructions)
    for multiple in multiples:
        pairs = re.findall(r'\d{1,3}', multiple)
        output += int(pairs[0]) * int(pairs[1])
    print(output)


if __name__ == '__main__':
    main()
