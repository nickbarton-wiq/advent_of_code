import re


def parse_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


def diagonal(word_search):
    output = []
    columns = len(word_search[0])
    rows = len(word_search)
    for row in range(rows):
        sequence = ''
        x = row
        y = 0
        while x >= 0 and y <= columns:
            sequence += word_search[x][y]
            x -= 1
            y += 1
        output.append(sequence)
    for column in range(1, columns):
        sequence = ''
        x = rows - 1
        y = column
        while x >= 0 and y <= columns-1:
            sequence += word_search[x][y]
            x -= 1
            y += 1
        output.append(sequence)
    return output


def main():
    # word_search = parse_file('2024/04/example.txt')
    word_search = parse_file('2024/04/input.txt')

    lines = {}
    lines["left_to_right"] = word_search
    lines["right_to_left"] = [word[::-1] for word in word_search]
    lines["top_to_bottom"] = [''.join(word) for word in zip(*word_search)]
    lines["bottom_to_top"] = [''.join(word) for word in zip(*word_search[::-1])]
    lines["diagonal_left_to_right"] = diagonal(word_search)
    lines["diagonal_left_to_right_reversed"] = [line[::-1] for line in lines["diagonal_left_to_right"]]
    lines["diagonal_right_to_left"] = diagonal([line[::-1] for line in word_search])
    lines["diagonal_right_to_left_reversed"] = [line[::-1] for line in lines["diagonal_right_to_left"]]

    answer = 0
    for v in lines.values():
        for word in v:
            answer += len([m.start() for m in re.finditer("XMAS", word)])
    return answer


if __name__ == '__main__':
    print(main())
    # test()
