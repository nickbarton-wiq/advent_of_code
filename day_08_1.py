with open("day_08.input") as f:
    lines = f.read().split("\n")

trees = []
for line in lines:
    trees.append([{"val": int(x), "counted": False} for x in line])

width = len(trees[0])
length = len(trees)

total_trees_visible = 0


def check_tree_line(tree_line):
    tallest_tree = 0
    trees_visible = 0
    for i, t in enumerate(tree_line):
        if i == 0 and not t["counted"]:
            trees_visible += 1
            t["counted"] = True
            tallest_tree = t["val"]

        elif t["val"] > tallest_tree and not t["counted"]:
            trees_visible += 1
            tallest_tree = t["val"]
            t["counted"] = True

        elif t["val"] > tallest_tree:
            tallest_tree = t["val"]

    print(f"{trees_visible=}")
    print(tree_line)
    return trees_visible


print("LEFT")
# from left
for l in range(length):
    tree_line = [trees[l][w] for w in range(width)]
    total_trees_visible += check_tree_line(tree_line)

print(total_trees_visible)
print(trees)

print("TOP")
# from top
for w in range(width):
    tree_line = [trees[l][w] for l in range(length)]
    total_trees_visible += check_tree_line(tree_line)

print(total_trees_visible)
print(trees)

print("RIGHT")
# from right
for l in range(length):
    tree_line = [trees[l][w] for w in range(width - 1, 0, -1)]
    total_trees_visible += check_tree_line(tree_line)

print(total_trees_visible)
print(trees)

print("BOTTOM")
# from bottom
for w in range(width):
    tree_line = [trees[l][w] for l in range(length - 1, 0, -1)]
    total_trees_visible += check_tree_line(tree_line)

print(total_trees_visible)
print(trees)

print(f"{total_trees_visible=}")
