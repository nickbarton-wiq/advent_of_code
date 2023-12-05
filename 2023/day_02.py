import re


def get_data():
    with open('day_02.input') as f:
        return f.read().splitlines()


def part1(data):
    output = set()
    all_games = set()
    for line in data:
        id = re.findall(r'\d+', line)[0]
        all_games.add(int(id))
        game = {"green": 0, "red": 0, "blue": 0}
        line = line.split(':')[1]
        line = [x.strip() for x in line.split(';')]
        line = [x.split(',') for x in line]
        for sub_game in line:
            for dice in sub_game:
                dice = dice.strip().split()
                color = dice[1]
                number = int(dice[0])
                game[color] = number
                if game["green"] > 13 or game["red"] > 12 or game["blue"] > 14:
                    output.add(int(id))
    output = all_games - output
    return output


def part2(data):
    output = []
    all_games = set()
    for line in data:
        id = re.findall(r'\d+', line)[0]
        all_games.add(int(id))
        game = {"green": 0, "red": 0, "blue": 0}
        line = line.split(':')[1]
        line = [x.strip() for x in line.split(';')]
        line = [x.split(',') for x in line]
        for sub_game in line:
            for dice in sub_game:
                dice = dice.strip().split()
                color = dice[1]
                number = int(dice[0])
                game[color] = number if number > game[color] else game[color]
        output.append(game["red"] * game["green"] * game["blue"])
    return output


if __name__ == '__main__':
    data = get_data()
    # print(sum(part1(data)))
    print(sum(part2(data)))
