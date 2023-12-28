from typing import Dict, List
from math import lcm


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


def get_data(file) -> List[str]:
    with open(file) as f:
        return f.read().splitlines()


def get_rl_instructions(data) -> str:
    return data[0]


def get_nodes(data) -> Dict[str, Node]:
    raw_nodes = data[2:]
    nodes = {}
    for node in raw_nodes:
        n = Node(node)
        nodes[n.node] = n
    return nodes


def get_nodes_ending_with(nodes: Dict[str, Node], start: str) -> List[str]:
    """Gets all nodes that end with the given string"""
    return [node for node in nodes if node.endswith(start)]


def get_next_instruction(rl_instructions: str, instruction_index: int) -> str:
    """Yields the next instruction from rl_instructions, looping back to the beginning if needed"""
    return rl_instructions[instruction_index]


def increment_instruction(rl_instructions: str, instruction_index: int) -> int:
    """Increments the instruction_index, looping back to the beginning if needed"""
    if instruction_index + 1 == len(rl_instructions):
        return 0
    else:
        return instruction_index + 1


def all_nodes_end_in_z(nodes: List[str]) -> bool:
    return all([node.endswith('Z') for node in nodes])


def move_nodes(nodes: List[str], instruction: str, all_nodes: Dict[str, Node]) -> List[str]:
    if instruction == 'L':
        return [all_nodes[node].left for node in nodes]
    elif instruction == 'R':
        return [all_nodes[node].right for node in nodes]
    return nodes


def main():
    data: List[str] = get_data('2023/day_08.input')
    rl_instructions: str = get_rl_instructions(data)
    all_nodes: Dict[str, Node] = get_nodes(data)
    nodes: List[str] = get_nodes_ending_with(all_nodes, 'A')
    assert len(nodes) > 0, "No nodes starting with A found"
    # print(f"Step 0: {nodes}")

    steps: int = 1
    instruction_index: int = 0

    node_intervals = {}

    while not len(node_intervals) == len(nodes):
        instruction: str = get_next_instruction(rl_instructions, instruction_index)
        nodes: List[str] = move_nodes(nodes, instruction, all_nodes)
        # print(f"Step {steps}: {nodes}")

        if any([node.endswith('Z') for node in nodes]):
            for node in nodes:
                if node.endswith('Z'):  # and node not in node_intervals:
                    if node not in node_intervals:
                        node_intervals[node] = steps

        steps += 1
        instruction_index = increment_instruction(rl_instructions, instruction_index)

    print(node_intervals)

    return lcm(*node_intervals.values())


if __name__ == '__main__':
    print(main())
