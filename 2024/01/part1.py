def open_file(file):
    with open(file, "r") as f:
        return f.readlines()


def main():
    input = open_file("2024/01/example.txt")
    # input = open_file("2024/01/input.txt")
    list1 = []
    list2 = []
    for line in input:
        line = line.strip().split("   ")
        list1.append(int(line[0]))
        list2.append(int(line[1]))

    list1.sort()
    list2.sort()
    distance = sum([abs(list1[i] - list2[i]) for i in range(len(list1))])
    print(distance)


if __name__ == "__main__":
    main()
