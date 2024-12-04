def parse_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


def main():
    # word_search = parse_file('2024/04/example.txt')
    word_search = parse_file('2024/04/input.txt')

    rows = len(word_search)
    columns = len(word_search[0])

    answer = 0
    for row in range(1, rows - 1):
        for column in range(1, columns - 1):
            if word_search[row][column] == "A":
                surrounds = [
                    word_search[row - 1][column - 1],
                    word_search[row + 1][column + 1],
                    word_search[row - 1][column + 1],
                    word_search[row + 1][column - 1],
                ]
                if set(surrounds[0:2]) == {'M', 'S'} and set(surrounds[2:4]) == {'M', 'S'}:
                    answer += 1
    return answer


if __name__ == '__main__':
    print(main())
