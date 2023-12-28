import re


def get_data():
    with open('2023/01/input.txt') as f:
        return f.read().splitlines()


def main(data):
    output = []
    for line in data:
        code = ""
        numbers = re.findall(r'-?\d', line)
        code += numbers[0]
        code += numbers[-1]
        output.append(int(code))
    return sum(output)


if __name__ == '__main__':
    data = get_data()
    print(main(data))
