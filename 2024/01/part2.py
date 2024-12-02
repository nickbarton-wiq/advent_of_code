from collections import defaultdict


def open_file(file):
    with open(file, "r") as f:
        return f.readlines()


def main():
    # input = open_file("2024/01/example.txt")
    input = open_file("2024/01/input.txt")
    left_list = []
    right_list = []
    for line in input:
        line = line.strip().split("   ")
        left_list.append(int(line[0]))
        right_list.append(int(line[1]))

    right_list_hist = defaultdict(int)
    for i in right_list:
        right_list_hist[i] += 1

    similarity_score = sum([right_list_hist[i] * i for i in left_list])
    print(similarity_score)


if __name__ == "__main__":
    main()
