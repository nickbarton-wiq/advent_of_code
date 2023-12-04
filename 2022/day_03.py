import string

with open("day_03.input") as f:
    lines = f.read().split("\n")


def part1():
    total_score = 0
    for line in lines:
        line_length = len(line) // 2
        left = line[:line_length]
        left_list = [x for x in left]
        right = line[line_length:]
        right_list = [x for x in right]
        print(left_list, "|", right_list)

        for a in left_list:
            if a in right_list:
                if a.islower():
                    score = string.ascii_lowercase.index(a) + 1
                else:
                    score = string.ascii_uppercase.index(a) + 1 + 26
                total_score += score
    return total_score


def part2():
    total_score = 0
    for x in range(3, len(lines) + 1, 3):
        # print(f"{x=}")
        group = lines[x - 3 : x]
        # print(f"{group=}")
        for i in group[0]:
            if i in group[1] and i in group[2]:
                # print(i)
                if i.islower():
                    score = string.ascii_lowercase.index(i) + 1
                else:
                    score = string.ascii_uppercase.index(i) + 1 + 26
                total_score += score
                break
    return total_score


print(part2())
