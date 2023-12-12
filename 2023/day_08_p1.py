from typing import Dict


def get_data():
    with open('2023/day_08.input') as f:
        return f.read().splitlines()


def get_rl_instructions(data) -> str:
    return data[0]


class Node():
    def __init__(self, node_string: str):
        self.node_string = node_string

    @property
    def node(self) -> str:
        return self.node_string[:3]

    @property
    def left(self) -> str:
        return self.node_string[7:10]

    @property
    def right(self) -> str:
        return self.node_string[12:15]


def get_nodes(data) -> Dict[str, Node]:
    raw_nodes = data[2:]
    nodes = {}
    for node in raw_nodes:
        n = Node(node)
        nodes[n.node] = n
    return nodes


if __name__ == '__main__':
    data = get_data()
    rl_instructions = get_rl_instructions(data)
    nodes = get_nodes(data)

    move = 'AAA'
    i = 0
    while move != 'ZZZ':
        if rl_instructions[i] == 'L':
            move = nodes[move].left
        elif rl_instructions[i] == 'R':
            move = nodes[move].right
        print(move)
        i += 1
        if i == len(rl_instructions):
            rl_instructions += get_rl_instructions(data)

    print(i)
