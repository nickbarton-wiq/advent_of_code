import re


def get_data():
    with open('day_01.input') as f:
        return f.read().splitlines()


def part1(data):
    output = []
    for line in data:
        code = ""
        numbers = re.findall(r'-?\d', line)
        code += numbers[0]
        code += numbers[-1]
        output.append(int(code))
    return sum(output)


def part2(data):
    mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    pattern = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))')
    output = []
    for line in data:
        code = ""
        translation = ""
        numbers = re.findall(pattern, line)
        for x in numbers:
            if x in mapping.keys():
                translation += mapping[x]
            elif x in mapping.values():
                translation += x
            else:
                continue
        code += translation[0]
        code += translation[-1]
        output.append(int(code))
    return sum(output)


if __name__ == '__main__':
    data = get_data()
    # print(part1(data))
    print(part2(data))
