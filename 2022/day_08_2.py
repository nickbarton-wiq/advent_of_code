with open("day_08.input") as f:
    lines = f.read().split("\n")


trees = []
for line in lines:
    trees.append([int(x) for x in line])

width = len(trees[0])
length = len(trees)


def score(current_tree, view_list):
    score = 0
    if len(view_list) == 0:
        return score

    for t in view_list:
        if t < current_tree:
            score += 1
        elif t >= current_tree:
            score += 1
            return score
    return score


best_score = 0
for x in range(width):
    for y in range(length):
        # x = 3
        # y = 2
        # print(x, y)
        current_tree = trees[x][y]

        down = score(current_tree, [trees[i][y] for i in range(x, length)][1:])
        up = score(current_tree, [trees[i][y] for i in range(x, -1, -1)][1:])
        right = score(current_tree, [trees[x][i] for i in range(y, width)][1:])
        left = score(current_tree, [trees[x][i] for i in range(y, -1, -1)][1:])

        current_score = up * left * down * right

        if current_score > best_score:
            best_score = current_score

print(best_score)
