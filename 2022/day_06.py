with open("day_06.input") as f:
    lines = f.read().split("\n")

for line in lines:
    print(line)
    start = 14
    finish = 0
    for _ in range(len(line)):
        letters = [l for l in line[finish:start]]
        if len(set(letters)) == 14:
            print(start)
            break
        else:
            start += 1
            finish += 1
