def move_tail():
    if direction == "R":
        if head[1] - tail[1] >= 2:
            tail[1] = head[1] - 1
            tail[0] = head[0]

    elif direction == "L":
        if head[1] - tail[1] >= -2:
            tail[1] = head[1] + 1
            tail[0] = head[0]

    elif direction == "U":
        if head[0] - tail[0] <= -2:
            tail[0] = head[0] + 1
            tail[1] = head[1]

    elif direction == "D":
        if head[0] - tail[0] >= 2:
            tail[0] = head[0] - 1
            tail[1] = head[1]

    tail_positions.add(tuple(tail))


with open("day_09.input") as f:
    lines = f.read().split("\n")

head = [0, 0]
tail = [0, 0]
tail_positions = set(tuple(tail))

for line in lines:
    direction, moves = line.split()
    moves = int(moves)

    for _ in range(moves):
        if direction == "R":
            head[1] += 1
            move_tail()

        elif direction == "L":
            head[1] -= 1
            move_tail()

        elif direction == "D":
            head[0] += 1
            move_tail()

        elif direction == "U":
            head[0] -= 1
            move_tail()

print(tail_positions)
print(len(tail_positions))
