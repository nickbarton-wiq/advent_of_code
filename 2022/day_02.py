with open("day_02.input") as f:
    lines = f.read().split("\n")

shape = {
    "A": "rock",
    "X": "rock",
    "B": "paper",
    "Y": "paper",
    "C": "scissors",
    "Z": "scissors",
}


def rpc(p1, p2) -> int:
    """
    rock > scissors
    scissors > paper
    paper > rock
    """

    if p1 == "rock":
        shape_score = 1
        if p1 == p2:  # draw
            return shape_score + 3
        elif p2 == "scissors":  # win
            return shape_score + 6
        elif p2 == "paper":  # loss
            return shape_score + 0
        else:
            return 0
    elif p1 == "paper":
        shape_score = 2
        if p1 == p2:  # draw
            return shape_score + 3
        elif p2 == "rock":  # win
            return shape_score + 6
        elif p2 == "scissors":  # loss
            return shape_score + 0
        else:
            return 0
    elif p1 == "scissors":
        shape_score = 3
        if p1 == p2:  # draw
            return shape_score + 3
        elif p2 == "paper":  # win
            return shape_score + 6
        elif p2 == "rock":  # loss
            return shape_score + 0
        else:
            return 0
    else:
        return 0


def how_to_win(opponent, how_to_win):
    """
    X = lose
    Y = draw
    Z = win
    """
    if how_to_win == "draw":
        return opponent
    elif how_to_win == "lose":
        if opponent == "rock":
            return "scissors"
        elif opponent == "paper":
            return "rock"
        elif opponent == "scissors":
            return "paper"
    elif how_to_win == "win":
        if opponent == "rock":
            return "paper"
        elif opponent == "paper":
            return "scissors"
        elif opponent == "scissors":
            return "rock"


def part1():
    total_score = 0
    for line in lines:

        opponent = shape[line[0]]
        me = shape[line[2]]

        score = rpc(me, opponent)
        total_score += score
    return total_score


def part2():
    htw = {"X": "lose", "Y": "draw", "Z": "win"}
    total_score = 0
    for line in lines:

        opponent = shape[line[0]]
        dir = htw[line[2]]

        me = how_to_win(opponent, dir)
        score = rpc(me, opponent)
        total_score += score
    return total_score


print(part1())
print(part2())
