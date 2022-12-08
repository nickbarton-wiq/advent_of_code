with open("day_04.input") as f:
    lines = f.read().split("\n")

answer = 0
for line in lines:
    assignments = line.split(",")
    x1 = assignments[0].split("-")
    x2 = assignments[1].split("-")
    print(x1, x2)
    e1 = [i for i in range(int(x1[0]), int(x1[1]) + 1)]
    e2 = [i for i in range(int(x2[0]), int(x2[1]) + 1)]

    if any(elem in e1 for elem in e2) or any(elem in e2 for elem in e1):
        # print(e1, e2)
        answer += 1

print(answer)
