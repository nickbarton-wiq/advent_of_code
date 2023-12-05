def get_data():
    with open('day_04.input') as f:
        return f.read().splitlines()


def parse_data(data):
    output = []
    for line in data:
        game = int(line.split(":")[0].replace("Card ", ""))
        line = line.split(":")[1]
        numbers = line.split("|")[0].strip().split()
        winners = line.split("|")[1].strip().split()
        numbers = [int(number) for number in numbers]
        winners = [int(winner) for winner in winners]
        output.append({'game': game, 'numbers': numbers, 'winners': winners, 'score': 0})
    return output


def check_game(game_list):
    for game in game_list:
        for number in game['numbers']:
            if number in game['winners']:
                game['score'] += 1
    return game_list


def scoring_algorithm(input):
    if input < 1:
        return 0
    # Initialize the score
    score = 1  # for the first match
    # Calculate the score for the remaining matches
    for _ in range(1, input):
        score *= 2
    return score


def score(data):
    total_score = 0
    for game in data:
        total_score += scoring_algorithm(game['score'])
    return total_score


def part1(data):
    checked = check_game(data)
    total_scored = score(checked)
    return total_scored


def tally_cards(game, tally):
    if game["game"] in tally.keys():
        tally[game["game"]] += 1
    else:
        tally[game["game"]] = 1
    return tally


def add_cards(data):
    tally = {}
    for game in data:
        tally = tally_cards(game, tally)
        if game["score"] > 0:
            copies_won = []
            copies_won = data[game["game"]:game["game"]+game["score"]]
            data.extend(copies_won)

    output = 0
    for x in tally.values():
        output += x
    print(output)
    return


def part2(data):
    checked = check_game(data)
    for game in checked:
        del game["winners"]
        del game["numbers"]
    add_cards(checked)
    return checked


if __name__ == '__main__':
    data = get_data()
    data = parse_data(data)
    # print(part1(data))
    part2(data)
