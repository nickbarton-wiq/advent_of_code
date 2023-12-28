import re


def get_data():
    with open('2023/01/input.txt') as f:
        return f.read().splitlines()


def main(data):
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
    print(main(data))
