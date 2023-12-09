from functools import reduce

def get_data():
    with open('2023/day_06.input') as f:
        return f.read().splitlines()


def part1(data):
    time_list = ["".join(data[0].split(":")[1].strip().split())]
    distince_list = ["".join(data[1].split(":")[1].strip().split())]
    print(time_list)
    print(distince_list)

    winning_list = []
    winning_amount = []
    for i in range(0, len(time_list)):
        time = int(time_list[i])
        record = int(distince_list[i])

        for t in range(1, time):
            distince_travelled = t * (time - t)
            if distince_travelled > record:
                winning_list.append(t)
        winning_amount.append(len(winning_list))
        winning_list = []
    print(winning_amount)
    output = reduce(lambda x, y: x * y, winning_amount)
    print(output)


if __name__ == '__main__':
    data = get_data()
    part1(data)
