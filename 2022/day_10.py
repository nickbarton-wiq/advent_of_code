with open("day_10.input") as f:
    lines = f.read().split("\n")


answer = 0


def do_cycle(cycles):
    cycles += 1
    if cycles in [20, 60, 100, 140, 180, 220]:
        print(f"{cycles=}, {x=}")
        signal_strength = cycles * x
        answer += signal_strength
        print(answer)
    return cycles


x = 1
cycles = 0
for line in lines:
    inst = line.split()
    # print(inst)
    if len(inst) == 1 and inst[0] == "noop":
        cycles = do_cycle(cycles)
    elif len(inst) == 2 and inst[0] == "addx":
        for i in range(2):
            if i == 0:
                cycles = do_cycle(cycles)
            elif i == 1:
                x += int(inst[1])
                cycles = do_cycle(cycles)
