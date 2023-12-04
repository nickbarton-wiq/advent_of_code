with open("day_01.input") as f:
    lines = f.read().split("\n")

elves = []
calories = 0
for line in lines:
    if line != "":
        calories += int(line.strip())
    elif line == "":
        elves.append(calories)
        calories = 0
elves = sorted(elves, reverse=True)

print(f"Part1: {elves[0]}")
print(f"Part2: {sum(elves[:3])}")
