import re

with open("day_05.input") as f:
    lines = f.read().split("\n")

# containers = lines[:3]
# intructions = lines[5:]

containers = lines[:8]
intructions = lines[10:]


def parse_containers(containers):

    stacks = 9
    index = [i for i in range(1, 4 * stacks, 4)]

    container_stacks = {}
    for i, v in enumerate(index, start=1):
        container_stacks[i] = []
        for c in containers:
            if c[v] != " ":
                container_stacks[i].append(c[v])

    return container_stacks


def parse_instructions(instructions):
    digits = re.compile(r"\d+")
    instruction_list = []
    for instruction in instructions:
        a = re.findall(digits, instruction)
        instruction_list.append(a)
    return instruction_list


container_dict = parse_containers(containers)
# print(container_dict)
instruction_list = parse_instructions(intructions)


def part1():

    for inst in instruction_list:
        how_many = inst[0]
        from_stack = inst[1]
        to_stack = inst[2]

        for _ in range(int(how_many)):
            container_dict[int(to_stack)].insert(
                0, container_dict[int(from_stack)].pop(0)
            )
            # print(container_dict)

    answer = ""
    for c in container_dict.values():
        answer += c[0]

    return answer


def part2():
    print(container_dict)
    for inst in instruction_list:
        how_many = int(inst[0])
        from_stack = inst[1]
        to_stack = inst[2]

        moving = container_dict[int(from_stack)][:how_many]
        if len(moving) > 1:
            moving.reverse()
        print(moving)
        for m in moving:
            container_dict[int(to_stack)].insert(0, m)
        for i in range(how_many):
            container_dict[int(from_stack)].pop(0)
        print(container_dict)

    answer = ""
    for c in container_dict.values():
        answer += c[0]

    return answer


print(part2())
