import re


def get_data():
    with open('2023/02/input.txt') as f:
        return f.read().splitlines()


def main(data):
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
    print(sum(main(data)))
